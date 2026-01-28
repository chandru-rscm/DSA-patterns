n=int(input("enter number:"))
def pattern(n):
    val=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
            
        print(end="\n")
    val=1
    for k in range(n-1,0,-1):
        for l in range(1,k+1):
            print(l,end="")
            
        print(end="\n")
pattern(n)
