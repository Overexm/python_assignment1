from src import *
n=input('enter count:')
cnt=0
for i in coins:
    if cnt == int(n):
        break
    print(cnt+1,"-",i)
    cnt+= 1
