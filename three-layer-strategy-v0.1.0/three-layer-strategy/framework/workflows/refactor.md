# Workflow profile: refactor

A refactor changes structure without intentionally changing observable behavior.

Before building:

- name the maintainability or performance constraint;
- define the behavior that must remain invariant;
- identify measurements or tests that prove preservation;
- state any deliberate internal API migration.

If user-visible behavior changes, treat that part as a feature with its own spec.
