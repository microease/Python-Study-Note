# 下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，给你一个n行m列网格棋盘，
# 棋盘的左下角有一匹马，请你计算至少需要几步可以将它移动到棋盘的右上角，若无法走到，则输出-1.
# 如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。

# BFS 广度优先算法
# 首先我们需要一个队列Q存储待访问的点，一个map记录访问过的点visited[maxL][maxH]，起始点为vs=[0,0,0]0,1两点记录坐标，2点记录index步长, 结束点为vd=[n,m], Q.append(vs), 把起始点丢进队列里。
# 马走日，创建两个list列出x和y可走的方向dx=[1,1,2,2,-1,-1,-2,-2], dy=[2,-2,1,-1,2,-2,1,-1]
# while Q: 只要有未访问的点，就执行循环。
# vn=Q.pop(0), 取出队列第一个点并抛掉, if [vn[0],vn[1]] == vd: return vn[2] 如果发现此点就是想要的点，直接返回index步长，得到结果。
# 如果不是结果，就寻找与此节点相邻的未访问的点：
#coding=utf-8
from collections import deque
def steps(n,m):
    dx = [1, 1, 2, 2, -1, -1, -2, -2]
    dy = [2, -2, 1, -1, 2, -2, 1, -1]
