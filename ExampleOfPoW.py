"""
Simple example to help this sink in.

Let's decide that the hash of some integer X multiplied by another Y must end in 0.
So, hash(x * y) = ac23dc ... 0. For this example, we will fix X (x = 5) for the sake of simplicity.
"""

from hashlib import sha256

x = 5
y = 0 # We don't know what y should be yet

while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1
    

print(f'The solution is y = {y}') # Should return 21
