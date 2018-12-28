ansible-role-hosts
=========

An Ansible role for managing the hosts file /etc/hosts

Requirements
------------

None

Role Variables
--------------

**hosts_entries**: A list of both IP addresses and hosts.

* name - canonical_hostname (required)
* ip - IP address that associates name (required)
* aliases - A list of aliases provide for name changes; alternate spellings, shorter hostnames, or generic hostnames. (options).

Dependencies
------------

None

Example Playbook
------------
```
- hosts: all
  vars:
    hosts_entries:
      - name: sakura.ne.jp
        ip: 163.43.24.70
        aliases:
          - sakura
          - skr

  roles:
    - role: ivoamorim.hosts
```

License
-------

BSD
