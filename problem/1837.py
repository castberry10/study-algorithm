p, k = map(int, input().split())
t = 0
for i in range(2, k):
    if p % i == 0:
        t = 1
        break
        
        
if t == 0:
    print("GOOD") 
else:
    print("BAD", i)