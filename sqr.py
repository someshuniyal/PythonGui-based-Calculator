from math import sqrt
def finding_operator(mid,l):
    operators=["+","x","-","/","^"]
    for x in operators:
        temp=mid.find(x,0,len(mid))
        if temp!=-1:
            l.append(temp)
            return 1
    return 0
def solve(stri):
    count=stri.count("√")
    for x in range(count):
        index=stri.find("√",0,len(stri))
        if index!=0 and finding_operator(stri[index-1],[]):
            str1=stri[0:index]
            mid=stri[index+1:len(stri)]
            l=[]
            data=finding_operator(mid,l)
            if data:
                result=str(sqrt(float(mid[0:l[0]])))
                stri=str1+result+mid[l[0]:len(mid)]
            else:
                result=str(sqrt(float(mid)))
                stri=str1+result
    return stri
