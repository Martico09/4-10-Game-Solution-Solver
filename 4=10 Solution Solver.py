#defining Functions for permuting the digits
def toString(List):
  return ''.join(List)

def permute(a, l, r):
    if l == r:
        test.append(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] 


num = input("Enter the digits = ")  #input the digits
res = 10 #Result Digit
arr = []
n = len(num)
a = list(num)
test = []

if input("Do u have All operators ( + - * / ) ?: (y/n) ").upper() == "Y":
    op = "+-*/"
else:
    op = input("Enter the available operators like (*+-) ")


# Function call
permute(a, 0, n)


for z in test:
  for a in op:
      for b in op:
          for c in op:
                  q = z[0]+a+z[1]+b+z[2]+c+z[3]
                  try:
                      eval(q)
                  except ZeroDivisionError:
                      continue
                  if(eval(q) == res):
                      arr.append(q)

#For all possible solutions run --> print(arr[])

try:
    print(f"Solution = {arr[0]}")
except IndexError:
    print(f"No possible Solution for {num}")
