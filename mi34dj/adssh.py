#-*- coding: utf-8 -*-

import paramiko
import codecs
from random import choice
import string
import time

from paramiko_ssh import ParamikoSSH


def generate_password(length=8):
    chars = string.letters + string.digits
    return ''.join(choice(chars) for _ in range(length))


def generate_login():
    return "user%s%s" % (time.strftime("%y%m%d%H%M%S"),
                           generate_password(length=4).lower())

 
class ADSsh(ParamikoSSH): 
    
    @staticmethod
    def password_validation(password):
        # TODO: check password for #$@!R%@#$% shit here !!!
        return True
    
    def create_user(self, login, password):
        if not self.password_validation(password):
            raise RuntimeError("invalid password %s" % password)
        cmd = "C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe -InputFormat none " \
"import-module Adaxes;" \
"$pass=convertto-securestring -asplaintext -string '%s' -force;" \
"new-admuser -samaccountname '%s' -name '%s' -accountpassword $pass -path 'ou=test,dc=sys,dc=local' -adaxesservice 'localhost'" \
% (password, login, login)
                
        retcode, stdout, stderr = self.exec_command(cmd)
        decoder = codecs.getdecoder("ibm866")
        return retcode, decoder(stdout)[0], decoder(stderr)[0]


def paramiko_debug_on():
    import paramiko
    paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)
    
    
def test():
    from django.conf import settings
    paramiko_debug_on()

    #cmd = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe  -InputFormat none dir /"
    cmd = "C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe -InputFormat none get-help"
    #cmd = "c:\windows\system32\servermanagercmd.exe -help"

    ad = ADSsh(settings.ADSSH_HOST, user=settings.ADSSH_LOGIN,
               password=settings.ADSSH_PASSWORD,
               allow_agent=False, debug=False)
    ad.connect(check=False)
    #print ad.exec_command(cmd)
    #return
    login = generate_login()
    #print login
    print ad.create_user(login, 'buka002')[2]
    

if __name__ == "__main__":
    test()
    