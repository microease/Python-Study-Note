# 下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，给你一个n行m列网格棋盘，
# 棋盘的左下角有一匹马，请你计算至少需要几步可以将它移动到棋盘的右上角，若无法走到，则输出-1.
# 如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。

import random
import sys
sys.setrecursionlimit(100000)
step=0 #计步器
depth=0 #走步深度
m=2   #x轴的大小
n=1   #y轴的大小
maxstep=1000
liststep=[]


def zou():  #每次被调用，生产一个随机的步，
    return random.choice([(2,1),(2,-1),(1,2),(-1,2),(-2,1),(-2,-1),(1,-2),(-1,-2)])
    
def qi(x=1,y=1):    #qi的位置
    z=zou()
    global liststep,step,depth
    if (x+z[0])==m and (y+z[1])==n:         #若走到了(m,n)则
        step+=1                             #计步器+1
        liststep.append(step)               #往方案列表添加本回步数
        step=0 #重置计步器
        return
    if 0<(x+z[0])<=m and 0<(y+z[1])<=m:     #若该步可行并且未到（m,n）
        step+=1                             #则计步器+1
        if step==maxstep:                    #达到最大步数，停止循环
            step=0
            liststep.append(-1)
            return               
        else:
            return qi(x+z[0],y+z[1])              #迭代走下一步
    else:                                          #走出棋盘
        depth+=1
        if depth==10:
            depth=0
            return
        else:
            return qi(x,y)                                    




while n<10000:
    n=n+1
    qi()


liststep=set(liststep)
liststep=list(liststep)
liststep.sort()


print(liststep[0])