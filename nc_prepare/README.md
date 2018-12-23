nc_prepare
=========

Install the necessary packages that are needed to run NextCloud on a minimal debian Debian system. It performs a full upgrade and then proceeds to install the dependencies.

The HTTP server to be installed is apache.
The Relational Database System to be installed is PostgreSQL.

Requirements
------------

No special requirements. The role makes a very straightforward use of the `apt` module.

Role Variables
--------------

The variable `needed_packages` defined in `vars/main.yml` contains a list of the package names to be installed. It is not recommended to override it.

Dependencies
------------

This package does not depend on any other roles.

Example Playbook
----------------
This playbook will upgrade and install the dependencies on a minimal Debian system

    - hosts: all
      roles:
         - nc_prepare

License
-------

BSD

Author Information
------------------

Javier Llopis
