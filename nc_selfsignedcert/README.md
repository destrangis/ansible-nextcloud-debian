nc_selfsignedcert
=========

This role creates a self-signed SSL certificate to be used on a secure HTTPS website.

Requirements
------------

The package `python-openssl` should have been installed on the server.

Role Variables
--------------

The role needs the variables below to be defined. However, reasonable defaults are provided in the vars/main.yaml file.

variable|description|default value
---------|----------------|-----------------
certificate_path|Directory where certificates are stored|/usr/local/etc/ssl_certificates 
server_hostname|The hostname. The different files are named based on the hostname|The same as the predefined variable`{{inventory_hostname}}` i.e. The name defined on Ansible's inventory.

Dependencies
------------

This role does not depend on any other role.

Example Playbook
----------------

    - hosts: ssl_servers
      vars:
          certificate_path: /etc/certificates
      roles:
         - nc_selfsignedcert

License
-------

BSD

Author
------------------
Javier Llopis
