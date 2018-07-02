s = sum([n**2 for n in range(10**8)])  # this is killed
s = sum(n**2 for n in range(10**8))  # this succeeds

print(s)  # prints: 333333328333333350000000
