Generic External packages
===========================

This role is intended to abstract installation of external software that is
shipped by APT repository.

Any repository templates has to placed in templates of THIS role, cause all
Ansible tasks are agnostic, they do not know anything about current context.
