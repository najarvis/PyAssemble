$ Alphabet Printer Program

02 ff 00          $ ADD 256 A    Register A Keeps track of how many letters we have left
02 00 01          $ ADD 0 B   Register B keeps track of what letter we are on
08 01 f0          $ GET B f0
01 f0             $ OUT f0
03 01 00          $ SUB 1 A 
02 01 01          $ ADD 1 B
07 00 06          $ JNZ A 06
ff                $ END
