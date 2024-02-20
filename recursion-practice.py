#first

def f1(x):
    if (0<x<10):
     result=x+f1(x-1)
     print(result)
    else:result=0
    return result
f1(4)
#Second
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#third : n!

def f3(n):
  if (n>0):
   result=n*f3(n-1)
  else:
    result=1
  return result

print("n! is ",f3(5))

