n=int(input("enter number: "))
def pattern(n):
    val=n
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*"*val)
            val=val-1
        print(end="\n")
pattern(n)
