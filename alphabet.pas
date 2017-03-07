$ Alphabet Printer Program

02 1a 00          $ ADD 26 A    Register A Keeps track of how many letters we have left
02 41 01          $ ADD 'A' B   Register B keeps track of what letter we are on
08 01 f0          $ GET B f0
01 f0             $ OUT f0
03 01 00          $ SUB 1 A 
02 01 01          $ ADD 1 B
07 00 06          $ JNZ A 06
ff                $ END
