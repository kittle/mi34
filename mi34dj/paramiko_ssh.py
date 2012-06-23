import random
from pprint import pprint

import paramiko

# TODO: timeout in _waiting_for_exit_status()


class ParamikoSSH():
    
    ssh = None
    #sudo_cmd = "sudo -s"
    #exit_cmd = "exit"
    
    def __init__(self, host, port=22, user="root", password=None, pkey=None,
                 allow_agent=True, debug=False):
        assert int(bool(password)) + int(bool(pkey))  == 1, "only one authentication method allowed"
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.pkey = pkey
        self.allow_agent = allow_agent
        self.debug = debug
    
    def connect(self, check=True):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if self.pkey:
            ssh.connect(self.host, port=self.port, username=self.user, pkey=self.pkey,
                        allow_agent = self.allow_agent)
        elif self.password:
            ssh.connect(self.host, port=self.port, username=self.user, password=self.password,
                        allow_agent = self.allow_agent)
        self.ssh = ssh
        if check:
            d = str(random.randint(1, 100000))
            _, ret = self.exec_command("echo '%s'" % d, expect_status = 0)
            assert ret.strip() == d, "ssh validation failed. got '%s' instead '%s'" % (ret, d)


    def close(self):
        if self.ssh:
            self.ssh.close()
            self.ssh = None

    
    def scp_data(self, stdin_data, remote_filename, chmod=None, use_sudo=False):
        #cmd = "cat > '%s'" % remote_filename
        cmd = "rm -f '%s'; cat > '%s'" % (remote_filename, remote_filename)

        self.exec_command(cmd, stdin_data=stdin_data, expect_status=0)

        if chmod:
            self.exec_command("chmod '%s' '%s'" % (chmod, remote_filename), 
                              expect_status=0)
        

    def exec_command(self, cmd, stdin_data=None, expect_status=None,
                 bufsize=-1, use_sudo=False):
        # TODO: exec timeout

        assert use_sudo == False, "Not yet implemented"

        if not self.ssh:
            self.connect()

        chan = self.ssh._transport.open_session()
        chan.exec_command(cmd)
        stdout = chan.makefile('rb', bufsize)
        stderr = chan.makefile_stderr('rb', bufsize)

        if stdin_data:
            stdin = chan.makefile('wb', bufsize)
            # TODO: data is file
            stdin.write(stdin_data)
            chan.shutdown_write()

        self._waiting_for_exit_status(stderr)
        exit_status = stderr.channel.exit_status

        # TODO: non blocking
        stdout_data = stdout.read()
        stderr_data = stderr.read()

        if expect_status != None and exit_status != expect_status:
            raise Exception("Cmd: %s . Exit_status: %s . Expected: %s. Stderr: %s" %
                            (cmd, exit_status, expect_status, stderr_data))

        return exit_status, stdout_data, stderr_data


    #def invoke_shell(self):
    #    channel = self.ssh.invoke_shell()
    #    channel.exec_command()
        
        
    def _waiting_for_exit_status(self, f): 
        n = 0
        while not f.channel.exit_status_ready():
            n += 1
            if self.debug and n%10000 == 0:
                print n

        