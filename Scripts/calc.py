#/usr/bin/env python
from optparse import OptionParser
import sys
from math import *

if __name__=='__main__':
    parser=OptionParser()
    (options,args)= parser.parse_args()
    if len(args)<1:
        print("pass smthng")
    else:
        for current_arg in args:
            try:
                res = eval(current_arg)
                print(str(current_arg) + "=" + str(res))
            except:
                print(str(current_arg)+"did not evaluate")
else:
    pass
