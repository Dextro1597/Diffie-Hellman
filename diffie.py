sharedPrime = 23 #p
sharedBase = 5 #q

faizalSecrect = 6 #a
definiteSecrect = 3 #b

print('Publically Shared Variables')
print('Value of P:-' +str(sharedPrime))
print('Value of q:-' +str(sharedBase))


A = (sharedBase ** faizalSecrect) % sharedPrime
print('\n Faizal Sends over Public channel:', str(A))

B = (sharedBase ** definiteSecrect) % sharedPrime
print('\n Definite Sends over Public Channel:', str(B))


A1 = (B ** faizalSecrect) % sharedPrime
print('\n Faizal Shared Secrect:', str(A1))

B1 = (A ** definiteSecrect) % sharedPrime
print('\n Definite Shared Secrect:', str(B1))

