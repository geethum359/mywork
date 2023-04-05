
st= "ABAABBABAB" # string
s=""
countA=0
countB=0
n=len(st)
for i in range(n):
    if st[i]=='A':
        s+=st[i]
        countA+=1
    elif st[i]=='B':
          s+=st[i]
          countB+=1
    if countA==countB:
         s+=","
         x=s.split(",")
print(x[:-1])
