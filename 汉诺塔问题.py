def hanoi(n,src,mid,dest):
    if n == 1:
        print(src + "->" + dest)
        return
    hanoi(n-1,src,dest,mid)
    print(src + "->" + dest)
    hanoi(n-1,mid,src,dest)

n = int(input())
hanoi(n,'A','B','C')

#说实话这个我不是很懂
#一共需要移动（2**n-1）次