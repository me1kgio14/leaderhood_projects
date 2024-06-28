def capitalize(s):
    capitalization0=""
    capitalization1=""
    for index,char in enumerate(s):
        if index%2==0:
            capitalization0+=char.upper()
        else:
            capitalization0+=char
        if index%2!=0:
            capitalization1+=char.upper()
        else:
            capitalization1+=char
            
            
    list=[]
    list.append(capitalization0)
    list.append(capitalization1)
    return list