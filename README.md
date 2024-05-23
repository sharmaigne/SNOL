### What is SNOL?

**Simple Number-Only Language** or **SNOL** is a simplified custom language that only involves integer and real values, operations, and expressions.

This project is a **Read, Evaluate, Print, and Loop (REPL)** interpreter of SNOL written in Python.

### Data Types

SNOL is a static, implicitly typed language with only two data types described by the following EBNF rules:

`Integer` := [-]digit{digit}
``` python
# Valid integers
int1 = 0
int2 = -23
```

`Float` := Integer.{digit}
``` python
# Valid floats
float1 = 43.234
float2 = -4.0
float3 = 2.
```

### Keywords

`BEG`

`PRINT`

`EXIT!
