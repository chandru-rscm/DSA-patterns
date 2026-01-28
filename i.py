n=int(input("enter the number: "))
def pattern(n):
    
    for i in range(1,n+1):
        val=1
        for j in range(1,n-i+2):
            print(val,end="")
            val=val+1
        print(end="\n")
            
pattern(n)
