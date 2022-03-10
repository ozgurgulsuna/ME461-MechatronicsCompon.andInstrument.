#/usr/bin/env python
from optparse import OptionParser
import itertools
import time

def findTurkish()

def IsTurkish(L, allowPrint = False):
    trChar=['A','B','C','Ç','D','E','F','G','Ğ','H','I','İ','J','K','L','M','N','O','Ö','P','R','S','Ş','T','U','Ü','V','Y','Z','Â']
    trchar=['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş','t', 'u', 'ü', 'v', 'y', 'z','â',' ']
    trList=[];
    A=[];
    A2=[];
    a=time.time()
    
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
                            print(i," Too much letter repetition, only 5 of them are included!")
                            count = 5
                        for k in range(count):
                            if i[0] in trChar:
                                trList.append(trchar[trChar.index(i[0])])
                            else: trList.append(i[0])
                        break
                    else: 
                        print(i," is not a valid letter, ignoring it!") 
                        break
                except:
                    print(i," is not a single letter, ignoring it!")
                    break
            else:
                if i[0] in trchar or i[0] in trChar:
                    
                    if i == j:
                        trList.append(i)
                        break
                    
                else: 
                    print(i," is not a valid letter, ignoring it!") 
                    break
                
                
    b=time.time()
    print(time.time()-a) 
    
    
    for i in range(len(trList)+1):
        t=list(itertools.permutations(trList,i))
        for j in range(len(t)):
            A.append(''.join(t[j]))
                 
                 
    print(time.time()-b)      
    c=time.time()
    
    A.sort()
    A2.append(A[0])
    for i in range(1,len(A)):
        if A[i]!=A[i-1]:
            A2.append(A[i])
    
    tk = list(open("tk.txt","r"))
    tk.sort()


    #if allowPrint == True:
        #for i in A2:
            #print(i)        

        
    print(time.time()-c)
    return None

if __name__ == '__main__':
    parser = OptionParser()
    (options, args) = parser.parse_args()
    if len(args) < 1:
        print("Please pass some lettuce!")
    else:
        IsTurkish(args, allowPrint=True)
            
#IsTurkish(["a","b555","c"],False)
