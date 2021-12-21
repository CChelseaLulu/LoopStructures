#2
n = int(input("enter number:"))
while n > 1:
    n /= 2
    print (n)

#2a

count = 0
n = float(input("enter number"))
while n > 1:
    n //= 2
    print (n)
    count +=1
print (count)

#2b
count = 0
n = float(input("enter number"))
while n > 1:
    print(n)
    n //= 2
    print (n)
    count +=1
print (count)

#2c
count = 0
n = float(input("enter number"))
counter = 1
while n > 1:
    n //= 2
    print (n)
    count +=1
    counter = counter + 1
    print(counter)
print (count)


#2d
#There is no difference. The output is the same.
