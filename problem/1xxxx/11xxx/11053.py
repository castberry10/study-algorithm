# N = int(input())
# # A = []
# A = list(map(int, input().split()))

# dp = [0] * N 
# maxdata = 0
# maxdp = 0
# # for i in range(N):
# #     if A[i] > maxdata:
# #         if i == 0:
# #             maxdata = A[0]
# #             dp[0] = 1
# #             continue
# #         # print()
# #         maxdata = A[i]
# #         maxdp = max(dp[:i])
# #         dp[i] = maxdp + 1
# for 
# # print(dp)
# # print(A)
# print(max(dp))

N = int(input())

A = list(map(int, input().split()))
A.insert(0, 0)
dp = [0] * (N + 2)

maxdp = 0
for i in range(1, N + 1):  #시작 부분 결정
    for j in range(i):
        if A[i] > A[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    if dp[i] > maxdp:
        maxdp = dp[i]


print(maxdp)
