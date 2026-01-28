n=int(input("Enter number: "))
def pattern(n):
    for i in range(1,n+1):
        print("*"*i)
    for j in range(n-1,0,-1):
        print("*"*j)


    
pattern(n)


                
