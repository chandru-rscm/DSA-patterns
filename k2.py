n=int(input("enter number: "))
def pattern(n):
    for i in range(1,n+1):
        val=1
        print(" "*(n-i),end="")
        for j in range(1,i+1):
            print(val,end="")
            val=val+1
        print(end="\n")
pattern(n)
