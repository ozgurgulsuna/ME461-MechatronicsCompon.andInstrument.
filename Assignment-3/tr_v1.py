#/usr/bin/env python
from optparse import OptionParser

def IsTurkish(L, allowPrint = False):
    trChar=['A','B','C','Ç','D','E','F','G','Ğ','H','I','İ','J','K','L','M','N','O','Ö','P','R','S','Ş','T','U','Ü','V','Y','Z','Â']
    trchar=['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş','t', 'u', 'ü', 'v', 'y', 'z','â',' ']
    trList=[];
    for index, char in enumerate(L):        
        for i,j in enumerate(trChar):
            if char == j:
                L[index]=trchar[i]
    for i in L:
        for j in trchar:
            if len(i)>1:
                try:
                    count=int(i[1:]) # number of repetitive char 
                    if count > 10: 
                        print(i," Too much letter repetition, only 10 of them are included!")
                        count = 10
                    for k in range(count):
                        trList.append(i[0])
                    break
                        
                except:
                    print(i," is not a single letter, ignoring it!")
                    break
            else:
                
                if i == j:
                    trList.append(i)
                    break

    
    
    if allowPrint == True:
        print(trList)
    return None

if __name__ == '__main__':
    parser = OptionParser()
    (options, args) = parser.parse_args()
    if len(args) < 1:
        print("Please pass some values")
    else:
        IsTurkish(args, allowPrint=True)
            
IsTurkish(["a","b","c"],False)
