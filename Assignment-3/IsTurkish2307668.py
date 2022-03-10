#/usr/bin/env python
from optparse import OptionParser
import itertools
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    
def IsTurkish(L, allowPrint = False):
    global tknew
    trChar=['A','B','C','Ç','D','E','F','G','Ğ','H','I','İ','J','K','L','M','N','O','Ö','P','R','S','Ş','T','U','Ü','V','Y','Z','Â']
    trchar=['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş','t', 'u', 'ü', 'v', 'y', 'z','â',' ']
    trList=[];
    A=[];
    W=[];
    A2=[];
    A3=[];    
#    a=time.time()
    
    for index, char in enumerate(L):        
        for i,j in enumerate(trChar):
            if char == j:
                L[index]=trchar[i]
    for i in L:
        for j in trchar:
            if len(i)>1:
                try:
                    if i[0] in trchar or i[0] in trChar:
                        count=int(i[1:]) # number of repetitive char 
                        if count > 5: 
                            if allowPrint == True:
                                print(i," Too much letter repetition, only 5 of them are included!")
                            count = 5
                        for k in range(count):
                            if i[0] in trChar:
                                trList.append(trchar[trChar.index(i[0])])
                            else: trList.append(i[0])
                        break
                    else: 
                        if allowPrint == True:
                            print(i," is not a valid letter, ignoring it!") 
                        break
                except:
                    if allowPrint == True:
                        print(i," is not a single letter, ignoring it!")
                    break
            else:
                if i[0] in trchar or i[0] in trChar:
                    
                    if i == j:
                        trList.append(i)
                        break
                    
                else: 
                    if allowPrint == True:
                        print(i," is not a valid letter, ignoring it!") 
                    break
                
                
#   b=time.time()
#   print(time.time()-a) 
    
    
    for i in range(len(trList)+1):
        t=list(itertools.permutations(trList,i))
        for j in range(len(t)):
            A.append(''.join(t[j]))
                 
                 
#   print(time.time()-b)      
#   c=time.time()
    
    A.sort()
    A2.append(A[0])
    for i in range(1,len(A)):
        if A[i]!=A[i-1]:
            A2.append(A[i])
    
    tk = list(open("tk.txt","r"))
    tknew=[]
    for i in range(len(tk)):
        s=''
        for indexj , j in enumerate(tk[i]):
            done=0
            for indexc , c in enumerate(trChar):
                if c == j:done=indexc+65
            if done:        
                s+=trchar[done-65]
            else:
                s+=j
        tknew.append(s)

    for i in range(len(trList)+1):
        for j in range(len(A2)):
            if len(A2[j])== i:
                A3.append(A2[j])
    print(len(A2),len(A3))
    
    for i in range(len(A3)):
        if len(A3[i])>=2:
            if ((A3[i]+str("\n")) in tknew):
                W.append(A3[i])
                if allowPrint == True:
                    print(bcolors.OKGREEN+ A3[i])
            else:
                if allowPrint == True:
                    print(bcolors.FAIL+A3[i])
                    
    #a=open("tksorted.txt","w")
    #for i in range(len(tknew)):
        #a.write(tknew[i])
    #a.close()

    return A3,W,1

if __name__ == '__main__':
    parser = OptionParser()
    (options, args) = parser.parse_args()
    if len(args) < 1:
        print("Please pass some lettuce!")
    else:
        IsTurkish(args, allowPrint=True)
            
#IsTurkish(["a","hh5","c"],False)

