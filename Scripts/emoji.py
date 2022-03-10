#/usr/bin/env python3

import sys

emo=''
emo_base = 0x1f600
for i in range (0,65):
    emo +=chr(emo_base+i)
    print(emo)
    
