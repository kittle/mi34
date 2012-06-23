
This is PoC of temporary remote desktop sessions from browser to windows server. Some kind of kiosk mode.

###The workflow (don't ask me why ;) ):

	
1.   Recapcha
2.   Create temporary user in Windows Active Directory(AD) via:

    * ssh to Windows + PowerShell
    * python-ldap to AD

3. Redirecting user to EricomAccessNowWebComponent which acts as Remote Desktop in browser.

	
###Install
	
    pip install django django-recaptcha paramiko uwsgi


###Running

Via nginx + uwsgi .

