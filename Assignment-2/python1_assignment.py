
def sumem(l):
    '''
    This will return the sum of element in the passed list l
    along with bad element in l in  a separate list.
    Please send an iterable object with summable items in it
    If the passed iterable has elements that are not summable
    this function will try to delete them from list l, and also return
    the sum of summable objects and a separate list of non-summable elements in l at the end
    if there is an other iterable item (such as another lins in l), you can count it as a bad item by default
    independent of whether there are summable items in it or not
    However, as before, if you also treat them recursively as defined above, you will get upto twice the credit!
    under no condition your code should crash
    '''
    # you might want to check 'pass by value pass by reference 'n python before next class
    sum=0
    badlist = [] 
    origList = []
    
    if isinstance(l,tuple) or isinstance(l,list):
        origList=list(l);
        for x in origList:
            if isinstance(x,int) or isinstance(x,float):
                sum = sum + x;
            elif isinstance(x,tuple) or isinstance(x,list):
                presum, prebadlist = sumem(x);
                sum = sum + presum;
                if prebadlist != []:
                    for y in prebadlist:
                       # origList.remove(x-1);
                        badlist.append(y);
                        origList.remove(y);
                        l.append(origList);
            else:
                badlist.append(x)
               # l.remove(x);
                #l=list(origList);
    else:
        badlist = l
    return sum, badlist


lbad=1;
lbad2=(1);
lbad3="ahmet";
lbad4=[True];
l1=[1,2,("A",3,(4,"B"))];
l2=(5,5,5);
l3=[5,5,5,(5,5,5),[5,"ahmet",["ahmet"],5],"ahmet","mehmet"]
l5=["2","5",5,10,8,"hello",[5,8,8,8,"458","hello,fgf",True,False,5.44,6,215]];
l6=[[[[5,5,"True",],5,5,5,5,"ahmet",True],5,5,5,5],5,5,5,[5,5,5,5]];
list1 = ["abc", 34, True, 40, "male",[5,"ahmet",("mehmet",5,[["cehmet"],5,[["dehmet",10,10,True]],10,()])]]

print(sumem(l1))
print(l1)

