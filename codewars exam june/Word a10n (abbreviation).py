def abbreviate(s):
    s=s.replace("-"," ")
    list=s.split()
    helper=[]
    for i in list:
        if len(i)==1 or len(i)==2:
            helper.append(i)       
        else:
            length=len(i)-2
            word=i[0]+str(length)+i[-1]
            helper.append(word)
            hlp="-".join(helper)
        
        
    return hlp