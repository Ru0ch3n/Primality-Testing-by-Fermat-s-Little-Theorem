"""
    Primality Testing by Fermat's Little Theorem
    基于费马小定理的素性检测
    @author:Chai
"""

"""
    Dependencies
"""
from random import *
from math import gcd
import sys

"""
    Initialize
"""
if len(sys.argv) == 3:
    target =  eval(sys.argv[1])
    k = eval(sys.argv[2])
else:
    #target储存目标数
    target = eval(input("请输入target number"))
    if(target%2 == 0):
        print("输入的不是奇整数，是偶数")
        exit(2)
    #k存储安全参数k
    k = eval(input("请输入安全参数k\n"))

#用概率ans定义是素数的概率，设初值为0
ans = 0
#a存储[2,m-2]中的一个随机数，先随意设个初值为0
a = 0

"""
    StartTest
"""
#判断k回
for i in range(0,k):
    #选取一个[2,m-2]的数字，即[2,m-1)。注意randint下是左开右闭区间
    a = randint(2,target-1)
    if(gcd(a,target) != 1):
        print("用",a,"与它非互素已经判断出是合数")
        exit(2)
    if(pow(a,target-1,target)!=1):
        print("用",a,"已经判断出是合数")
        exit(2)
print("m是素数的概率是",1-1/2**k)
