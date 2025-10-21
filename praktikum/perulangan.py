
max=0
n=input("masukan nilai n : ")

n=int(n)

while n!=0 : 
    if (n > max) :
        max=n
    n=input("masukan nilai n : ")
    n=int(n)
print("number terbesar",max)