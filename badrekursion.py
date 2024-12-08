import sys
sys.getrecursionlimit()
sys.setrecursionlimit(2000)

def  f(n):
     if n <=1:
          return  1 +f(n)
     else:
          return n * f(n-1)
result = f(2)
print(result)   