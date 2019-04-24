#code by Ahad Patel
sharedPrime = input('Enter the value of p:') #p(eg. 23)
sharedBase = input('Enter the value of q:') #q(eg. 5)

aliceSecrect = input('Enter aliceSecret key value(a):') #a(eg. 6)
bobSecrect = input('Enter bobSecrect key value(b):')#b(eg. 3)

print('Shared Variables:')
print('Shared Prime no.:', int(sharedPrime))
print('Shared Base no.:', int(sharedBase))


A =(int(sharedBase) ** int(aliceSecrect)) % int(sharedPrime)
print('Alice sends value over insecure channel:-', str(A))

B =(int(sharedBase) ** int(bobSecrect)) % int(sharedPrime)
print('Bob sends value over insecure channel:-', str(B))

A1 = (B ** int(aliceSecrect)) % int(sharedPrime)
print('Value got by Alice', str(A1))

B1 = (A ** int(bobSecrect)) % int(sharedPrime)
print('Value got by Bob', str(B1))

