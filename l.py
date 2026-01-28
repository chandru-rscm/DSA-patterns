n=int(input("enter number: "))
def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(" "*(i-1),end="")
            print("*"*(n-i+1),end="")
        print(end="\n")

pattern(n)
