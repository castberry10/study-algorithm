n = int(input())
cnt =0
for i in range(1, n+1):
    temps = str(i)
    tof = True
    ch = True
    ckdl = 10
    for cindex in range(len(temps) - 1):
        if ckdl != int(temps[cindex]) - int(temps[cindex + 1]): #만약 차이가 다르다면 
            if ch:#만약 갱신이 처음이면 
                ch = False
                ckdl = int(temps[cindex]) - int(temps[cindex + 1])
            else: #만약 갱신이 처음이 아니라면 
                tof = False
    if tof:
        cnt += 1
print(cnt)        