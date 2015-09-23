# Ansible-LXC
### About
This is a dyanmic Ansible inventory for LXC.  LXC by default does not provide labels or tags for grouping hosts.  To use this, you must append '-<group_name>' onto
the name of the container when it is created:

```
lxc-create -n myhost-webservers ...
```

'myhost' is the name of my container followed by the group name '-webservers'.  The overall goal of this inventory is to test Ansible playbooks against LXC containers
on Jenkins.

### Installation
No additional installation.

### Confgiuration
No additional configuration is needed.

### Running With Ansible
>ansible-playbook -i inventory/ansible-lxc/inventory.py --limit "LimitToRole"