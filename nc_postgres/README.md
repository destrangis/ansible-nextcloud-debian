nc_postgres
=========

This role configures PostgreSQL server so that it can be used to host a NextCloud database.

- Ensures that the local, unix domain users are authenticated using encrypted passwords instead of the Debian default of peer authentication.
- Restarts PostgreSQL so that the change takes efect.
- Creates a non-privileged Postgres role with password.
- Creates a 'nextcloud' database owned by the above role.

Requirements
------------

This role needs that the configuration variable `allow_world_readable_tmpfiles` in `ansible.cfg` be set to `yes`. This is to allow database operations be performed by the underprivileged user `postgres`.

Role Variables
--------------

The following variables should be set by the calling playbook:

variable          |description
------------------|--------------
pg_username |The owner of the nextcloud database
pg_password |The password for the above user


Dependencies
------------

This role does not depend on other roles.

Example Playbook
----------------

    - hosts: servers
      vars:
             pg_username: nextcloudowner 
             pg_password: x342pfzz
      roles:
         - nc_postgres 

License
-------

BSD

Author 
------------------

Javier Llopis