x, y, z = map(int ,input().split())
temp = min(x, y, z)
# 문제의 핵심은 최적으로 건포도를 확인할 수 있는 단면의 두께인 2를 최소한으로 만드는 겁니다. 
# 케이크의 가장 얇은 곳을 자르면 되겠죠? 
# 예외 케이스로 3 x 3 x 3 케이크가 있는데 이 케이크는 안잘라도 건포도가 어디있는지 알기에 
# (건포도가 겉에 없으면 안에 있는거니까요)
# 3x3x3 케이크는 안잘라도 알 수 있다는 것에 유의하면 됩니다. 
if temp <= 2:
    print(0)
elif x == y == z == 3:
    print(0) 
else:
    print((temp - 1) // 2)