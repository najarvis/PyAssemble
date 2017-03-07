$ Double program

02 01 00        $ ADD 1 A
02 08 01        $ ADD 4 B    Number of times we want to run
04 20 f1        $ MOV ' ' f1

08 00 f0        $ GET A f0
0c f0           $ INT f0
01 f1           $ OUT f1

03 01 01        $ SUB 1 B
0a 01 00        $ SLR 1 A

07 01 09        $ JNZ B 06

ff              $ END




