# ansible-mailing-solution
Complete mailing solution with dkim signatures, webmail and antispam, just ready to deploy. Tested on Debian Buster. Doesn't support TLS yet!

## repo structure
`/filter_plugins`
`/group_vars` - variables for groups of hosts
`/host_vars` - variables for hosts
`/roles`
`/ansible.cfg` - basic configuration file for ansible
`/hosts` - inventory file

## playbooks

### site.first_run.yml
Playbook for basic setup of new container/server. Should be played on every new host for basic setup.

### site.email.yml
Playbook for setup new email solution. See `hosts` file for info what roles are applied on hosts.

### site.www_loadbalancer.yml
Playbook for setup haproxy as www balancer for webmail and rspamd gui with let's encrypt support.

### site.service_loadbalancer.yml
Playbook for loadbalancer for IMAP and SMTP with fail2ban support

## configuration
Before using this bundle, basic configuration must be done:
- `group_vars/all/all.yml` - provide your domain name for hostnames (used by inventory file)
- `group_vars/all/ansible.yml` - fix your ssh connect command, ie. setup bastion host if used
- `group_vars/all/firewall.yml` - setup your firewall rules, mostly for NAT and routing.
- `group_vars/all/vault.yml` - create valid vault file. See `vault.example` for variables and content used here
- go thru every group_vars direcory and setup your environment according
