nc_nextcloud
=========

This role downloads, installs and personalises a NextCloud server.

Requirements
------------

The roles nc_prepare and nc_postgres need to have been run previous to running this role.

This role requires that the configuration variable `allow_world_readable_tmpfiles` in `ansible.cfg` be set to `yes`. This is to allow nextcloud configuration operations be performed by the underprivileged user `www-data`.

Role Variables
--------------
This role expects the following variables:

variable|description
---------|--------------
nextcloud_releases|Url to the downloads area. E.g. https://download.nextcloud.com/server/releases/
nextcloud_zip| The zip archive to be downloaded. E.g. nextcloud-15.0.0.zip
pg_username |The owner of the nextcloud database
pg_password |The password for the above user
nc_admin     | The NextCloud user that will have admin privileges
nc_password| The password for the above user
config_settings|A list of mappings consisting of key and values corresponding to the settings of the NextCloud's `config.php` files. These include optimisation parameters as well as the SMTP server configuration. See the example below.

Dependencies
------------
 This role does not depend on any other role.

Example Playbook
----------------

    - hosts: all
	  vars:
	     pg_username: ncuser
	     pg_password: dbpasssss99
	     nc_admin: ncadmin
	     nc_password: firstpass3343
	     nextcloud_sw: nextcloud-15.0.0
	     nextcloud_zip: "{{nextcloud_sw}}.zip"
	     nextcloud_releases: https://download.nextcloud.com/server/releases/

	     config_settings:
		  - { "key": "'memcache.local'", "value": "'\\OC\\Memcache\\APCu'" }

		    # notification email settings
		  - { "key": "'mail_smtpmode'", "value": "'smtp'" }
		  - { "key": "'mail_sendmailmode'", "value": "'smtp'" }
		  - { "key": "'mail_smtphost'", "value": "'smtp.someserver.com'" }
		  - { "key": "'mail_from_address'", "value": "'nextcloud'" } 
		  - { "key": "'mail_domain'", "value": "'destrangis.com'" }

	  roles:
	    - nc_prepare
	    - nc_postgres
	    - nc_nextcloud
License
-------

BSD

Author
------------------

Javier Llopis
