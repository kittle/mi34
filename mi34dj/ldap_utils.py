"""
http://stackoverflow.com/questions/2273117/django-python-ldap-unwilling-to-perform-info-00002077-svcerr-dsid-031907b
"""

import ldap
from ldap import modlist

class AD():
    def __init__(self, *args):
        self.ldap_connection = self.get_ldap_connection(*args)

    @staticmethod
    def get_ldap_connection(ldap_url, bind_dn, bind_pass):
        """
        ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, 0)
        ldap_connection = ldap.initialize(ldap_server)
        ldap_connection.simple_bind_s(bind_dn, bind_pass)
        #except ldap.LDAPError, error_message:
        """
        
        ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
        l = ldap.initialize(ldap_url)
        l.set_option(ldap.OPT_REFERRALS, 0)
        l.set_option(ldap.OPT_PROTOCOL_VERSION, 3)
        l.set_option(ldap.OPT_X_TLS,ldap.OPT_X_TLS_DEMAND)
        l.set_option(ldap.OPT_X_TLS_DEMAND, True)
        l.set_option(ldap.OPT_DEBUG_LEVEL, 255)
        l.simple_bind_s(bind_dn, bind_pass)
        return l

    def createuser(self, username, password, base_dn, fname, lname, domain): #, employee_num):
        """
        Create a new user account in Active Directory.
        """
    
        """
      # Check and see if user exists
      try:
          user_results = ldap_connection.search_s(base_dn, ldap.SCOPE_SUBTREE,
                                                  '(&(sAMAccountName=' +
                                                  username +
                                                  ')(objectClass=person))',
                                                  ['distinguishedName'])
      except ldap.LDAPError, error_message:
          print "Error finding username: %s" % error_message
          return False
    
      # Check the results
      if len(user_results) != 0:
          print "User", username, "already exists in AD:", \
                user_results[0][1]['distinguishedName'][0]
          return False
    """
    
        # Lets build our user: Disabled to start (514)
        #user_dn = 'cn=' + fname + ' ' + lname + ',' + base_dn
        user_dn = "cn=%s,%s" % (username, base_dn)
        user_attrs = {}
        user_attrs['objectClass'] = \
                  ['top', 'person', 'organizationalPerson', 'user']
        user_attrs['cn'] = str(username)
        #user_attrs['userPrincipalName'] = username + '@' + domain
        #user_attrs['sAMAccountName'] = username
        # Prep the password
        unicode_pass = unicode('\"' + password + '\"', 'iso-8859-1')
        password_value = unicode_pass.encode('utf-16-le')
        #user_attrs['userPassword'] = password_value
        user_attrs['mail'] = username + '@host.com'
        user_attrs['givenName'] = str(fname)
        user_attrs['sn'] = str(lname)
        #user_attrs['displayName'] = fname + ' ' + lname
        user_attrs['userAccountControl'] = '514'
        #user_attrs['employeeID'] = employee_num
        #user_attrs['homeDirectory'] = '\\\\server\\' + username
        #user_attrs['homeDrive'] = 'H:'
        #user_attrs['scriptPath'] = 'logon.vbs'
        
        
        #user_attrs['unicodePwd'] = [password_value]
        # New group membership
        #add_member = [(ldap.MOD_ADD, 'member', user_dn)]
        # Replace the primary group ID
        #mod_pgid = [(ldap.MOD_REPLACE, 'primaryGroupID', GROUP_TOKEN)]
        # Delete the Domain Users group membership
        #del_member = [(ldap.MOD_DELETE, 'member', user_dn)]
        
        user_ldif = modlist.addModlist(user_attrs)
        
        # Add the new user account
        self.ldap_connection.add_s(user_dn, user_ldif)
        
        # Add the password
        add_pass = [(ldap.MOD_REPLACE, 'unicodePwd', [password_value])]
        self.ldap_connection.modify_s(user_dn, add_pass)
        
        # Change the account back to enabled
        # 512 will set user account to enabled
        mod_acct = [(ldap.MOD_REPLACE, 'userAccountControl', '512')]
        self.ldap_connection.modify_s(user_dn, mod_acct)
        
        # Add user to their primary group
        #ldap_connection.modify_s(GROUP_DN, add_member)
        
        # Modify user's primary group ID
        #ldap_connection.modify_s(user_dn, mod_pgid)
        
        # Remove user from the Domain Users group
        #ldap_connection.modify_s(DU_GROUP_DN, del_member)
        
        # LDAP unbind
        self.ldap_connection.unbind_s()

    
def test():
    import os
    os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
    from django.conf import settings
    base_dn = settings.LDAP_USER_BASE
    fname = "zuka012"
    lname = "Last"
    domain = ''
    username = fname
    ad = AD(settings.LDAP_URL,
                    settings.LDAP_BIND_DN, settings.LDAP_BIND_PASS)
    ad.createuser(username, 'pPG45zdfr', base_dn, fname, lname, domain)
    
    
if __name__ == "__main__":
    test()
    