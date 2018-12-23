NextCloud on a Debian Server
---------------------------------

This Ansible playbook will install and configure a complete NextCloud server on a minimal Debian installation, installing all the necessary dependencies and using Apache as the webserver, PostgreSQL as the database and a self-signed SSL certificate.

#### Requirements
The Debian machine must have a SSH server and the non privileged user should be configured to access using by public key and should be able to escalate to root without a password.

#### Usage
Set the names of the Debian machines on the Ansible inventory, optionally edit the variables on the file `nextcloud_debian_server.yml` and run the command:

    ansible-playbook -i your-inventory nextcloud_debian_server.yml

Once the installation has been completed, open the web browser and open `https://your-hostname/`, add a SSL security exception --since it's using a self signed certificate- log in with the username you set on the vars above or the default `ncadmin` password `firstpass3343`, and start using it straight away. 

