Firewall role
===============

This is simple role for mmanagement of iptables, which is based on persistent
rule sets defined in template.

Now `filter`, `nat` and `mangle` tables are supported.

**WARNING**: define variable `firewall_rules` with cautions. You can simply
override it if defined in wrong `group_vars`!

Example of rules definition:

```
---
firewall_rules:
  - group: <group 1>
    filter:
      - <rule 1>
      - <rule 2>
    nat:
      - <rule 3>
    mangle:
      - <rule 4>
      - <rule 5>
  - group: <group 2>
    filter:
      - <rule 1>
      - <rule 2>
    nat:
      - <rule 3>
```

