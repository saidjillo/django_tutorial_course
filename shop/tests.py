from django.test import TestCase

# Create your tests here.
primes = []

for i in range(1,600851475143):
    if type((600851475143 / i)) == int:
    
        item = 600851475143 / i
        primes.append(item)