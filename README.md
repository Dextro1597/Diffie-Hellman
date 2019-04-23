# Diffie-Hellman
Diffie-Hellman is widely known as a Key exchange algorithm or key agreement algorithm. In this two parties (Faizal and Definite) to agree on a shared secret (the symetric key) over an insecure medium where an attacker (Ramadhir) is listening (these names are all common cryptography placeholder names, used to help clarify discussions of cryptography by using common names for various actors in a cryptographic exchange)
First Faizal and Definite agree on a Prime number: P, and a Base: G. These numbers are not secret, and can be known by Ramadhir.
P must be a prime number, and G is a Primitive root modulo.
Then Faizal and Definite then each randomly select their own private integer that they keep secret (even from each other), a and b.
Then Faizal calculates A = g^a mod p. Faizal sends A to Definite over the insecure channel (Ramadhir can see this number).
Then Definite calculates B = g^b mod p. Definite sends B to Faizal over the insecure channel.
Faizal then computes the shared secret, s = B^a mod p.
Definite aslo then computes the shared secret, s = A^b mod p.
Now Faizal and Definite have a shared secret key, s, that Ramadhir does not know, even though Ramadhir knows p, b, A, and B.
And this is how Faizal and Definite plan to kill Ramadhir and then kill him in hospital. #Bhai ka ,Dada ka, Baap ka sab ka badla lega re teri Faizal 
