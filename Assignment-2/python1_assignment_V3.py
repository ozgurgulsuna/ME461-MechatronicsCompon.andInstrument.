def sumem(*arg):
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
    sum=0                                                                                                                 # definitions and initialization
    badlist = []                                                                                                          # definitions and initialization
    origlist = []                                                                                                         # definitions and initialization
    if len(arg)==0:                                                                                                       # Check for no argument case, it acts like its empty
        return sum, badlist                                                                                               # Return empty lists
    l=arg[0];                                                                                                             
    
    
    if isinstance(l,tuple) or isinstance(l,list) or isinstance(l,set) :                                                   # Check for initial list type
        origlist=list(l);                                                                                                 # Copy list       
        for x in origlist:                                                                                                # Check each element for types
            if isinstance(x,int) or isinstance(x,float) or isinstance(x,complex) or isinstance(x,bool)  :                 # If type is summable 
                sum = sum + x;                                                                                            #     sum them
            elif isinstance(x,list) or isinstance(x,tuple) or isinstance(x,set) :                                         # If consists of another list
                presum, prebadlist = sumem(x);                                                                            #     iterate
                sum = sum + presum;                                                                                       #     sum interation
                if prebadlist != []:                                                                                      #     add non summable items in iteration to the bad list
                    for y in prebadlist:                                                                                
                        badlist.append(y);                                                                                      
            else:                                                                                                         # If type is different   
                badlist.append(x);                                                                                        #     add them to bad list
                if not isinstance(l,tuple):                                                                               #     can not remove items in a tuple
                    l.remove(x);                                                                                          #     remove if it is not in tuple 
    else:                                                                                                                 
        return None                                                                                                       # Otherwise return nothing
    return sum, badlist                                                                                                   # Return outputs
