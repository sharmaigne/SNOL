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


### ADDITIONAL FEATURES
This version of the SNOL interpreter fulfills all features required in the project definition and then some. These are the some:

1. BOOLEAN SUPPORT
A number only language would be much stronger with the addition of boolean operators.

In the spirit of SNOL, true and false are represented as integers (0 and 1) respectively

2. EXPRESSION SUPPORT FOR PRINT
The project definition only required PRINT to be able to process variables and literals. We've extended this to expressions for better user experience.