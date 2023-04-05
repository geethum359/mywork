def vowel():
    v='aeiou'
    lists=['anu','string','banana']
    newlist=[]
    for k in lists:
        m=''
        for i in k:
            if i in v:  
                m+=i
        newlist.append(m)
    print(newlist)
vowel()
