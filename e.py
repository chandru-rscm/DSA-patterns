n=int(input("enter number: "))

def pattern(n):
    for i in range(1,n+1):
        if i%2==0:
            val=0
        else:
            val=1
        for j in range(1,i+1):
            print(val,end="")
            val=1-val
                
                
        print(end="\n")

pattern(n)
