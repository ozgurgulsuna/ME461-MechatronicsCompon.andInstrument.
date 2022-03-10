#/usr/bin/env python3

import sys

emo = ''
emo_base = 0x1F600

for i in range(0,65):
	emo += chr(emo_base + i) + '  '
	if i % 10 == 9: # 10 emojis per line
		emo += '\n'

print(emo)

