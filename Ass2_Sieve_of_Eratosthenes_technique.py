#Python program for Sieve_of_Eratosthenes_technique

n=int(input("Enter number upto which prime numbers should be printed"))
m=n//2
l=[]#list containing numbers from 2 to n
l1=[]#list containing multiples from 2 upto m
for i in range(2,n+1):
    l.append(i)
for i in range(2,m):
    l1=list(range(i, n+1, i))
    for j in range(1,len(l1)):
        if(l1[j] in l):
            l.remove(l1[j])
print("Prime numbers upto",n,":",l) 