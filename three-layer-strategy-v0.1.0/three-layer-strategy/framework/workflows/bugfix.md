# Workflow profile: bug fix

The intent may be shorter, but it must include expected behavior, actual behavior and reproduction evidence.

Required sequence:

1. reproduce or explain why reproduction is impossible;
2. identify the violated current spec or create the missing one;
3. add a failing regression check when feasible;
4. implement the smallest safe correction;
5. verify the original reproduction and adjacent risks.

Do not let an agent guess a root cause from symptoms and immediately patch production code.
