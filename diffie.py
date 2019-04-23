sharedPrime = 23 #p
sharedBase = 5 #q

aliceSecrect = 6
bobSecrect = 3

print('Publically Shared Variables')
print('Value of P:-' +str(sharedPrime))
print('Value of q:-' +str(sharedBase))


A = (sharedBase ** aliceSecrect) % sharedPrime
print('\n Alice Sends over Public channel:', str(A))

B = (sharedBase ** bobSecrect) % sharedPrime
print('\n Bob Sends over Public Channel:', str(B))


A1 = (B ** aliceSecrect) % sharedPrime
print('\n Alice Shared Secrect:', str(A1))

B1 = (A ** bobSecrect) % sharedPrime
print('\n Bob Shared Secrect:', str(B1))

