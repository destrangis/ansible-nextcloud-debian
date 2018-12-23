nc_apache
=========

This role configures the Apache webserver to serve NextCloud.

- Uploads a virtua host configuration that uses nextcloud on a SSL virtual host, as well as a non-secure version.
- Creates the non-secure data directory and uploads an `index.html` file that simply redirects to the secure site.
- Creates a log directory
- Copies the SSL certificate to the place where it is expected
- Adds the hostname to '/etc/hosts' so that it can be resolved by Apache.
- Enables the necessary Apache modules.
- Enables the site.
- Restarts the Apache server.
 

Requirements
------------

There should be a certificate available for the configuration to be successfully performed. Ideally by the role nc_selfsignedcert. NextCloud should also have been installed in /opt/nextcloud

Role Variables
--------------

The following variables need to be defined:

variable|description
---------|----------------
certificate_path|Directory where certificates are stored
server_hostname|The hostname. The different files are named based on the hostname

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

    - hosts: ssl_servers
      vars:
         certificate_path: /usr/local/etc/ssl_certificates
         server_hostname: "{{inventory_hostname}}"
      roles:
         - nc_selfsignedcert
         - nc_apache

License
-------

BSD

Author
------------------

Javier Llopis
