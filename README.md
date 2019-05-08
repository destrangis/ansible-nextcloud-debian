NextCloud on a Debian Server
---------------------------------

This Ansible playbook will install and configure a complete NextCloud server and a Roundcube webmail from scratch on a server. I created it in order to fulfill a specific particular need and now I'm posting it here in case someone finds it useful.

The playbook only needs a minimal Debian installation, installing all the necessary dependencies and using either Apache or [Hiawatha](http://hiawatha-webserver.org)  as the webserver, PostgreSQL as the database and either a self-signed SSL certificate or my existing letsencrypt certificate chain which I was using at my previous server, and for which I am only providing a dummy file in this repository. This is the only part that is not general purpose but specific for my needs, and anyone interested should modify it.

The playbook also installs Roundcube webmail using the same PostgreSQL server and a SSL certificate.

In order for it to work you need your inventory file to be set up as:

    [nextcloud_servers]
    nextcloud.myserver.com

    [webmail_servers]
    webmail.myserver.com
    
where both `nextcloud.myserver.com` and `webmail.myserver.com` must resolve to the same IP address.


#### Requirements
The Debian machine must have a SSH server and the non privileged user should be configured to access using by public key and should be able to escalate to root without a password.

#### Usage
Set the names of the Debian machines on the Ansible inventory, optionally edit the variables on the file `nextcloud_debian_server.yml` and run the command:

    ansible-playbook -i your-inventory nextcloud_debian_server.yml

Once the installation has been completed, open the web browser and open `https://nextcloud.myserver.com/`, add a SSL security exception --if it's using a self signed certificate- log in with the username you set on the vars above or the default `ncadmin` password `firstpass3343`, and start using it straight away.
