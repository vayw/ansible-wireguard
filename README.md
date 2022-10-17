Wireguard Role
=========

Simple wireguard role


Requirements
------------

no requirements

Role Variables
--------------
```
wireguard_iface: wg0

wireguard_net prefix: 24

wireguard_server_ip: 192.168.100.1

wireguard_server_port: 51820

wireguard_nm_connections_folder: /etc/NetworkManager/system-connections

```

Dependencies
------------

no dependencies

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: wireguard
           vars:
             wireguard_clients:
               - ["August", "Thomas", "Lena"]

run with `-t getconfigs` to download .conf and PNG with QRcode for mobile wireguard client

License
-------

BSD

Author Information
------------------

vayw
