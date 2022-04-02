
# %%
from unittest import result


for i in range(1,101):
  print(i)
# %%
test_List = [60, 88, 75, 43, 90, 55, 12]
sum = 0
for score in test_List:
  sum += score


average = sum/len(test_List)
print(int(average))

# %%
for i in range(2,10):
  for j in range(1, 10):
    print(i*j, end="")
  print('')
# %%
a = [1,2,3,4]
result=[]
for num in a:
  result.append(num*3)
print(result)
# %%
a =[1,2,3,4]
result = [num*3 for num in a if num % 2 ==0] 
print(result)
# %%
result = [a*b for a in range(2,10) 
for b in range(1,10)]
print(result)
# %%
result = [num*2 for num in range(1,6)
if num % 2 ==1]
print(result)
# %%
num=0
for a in range(1,1001):
  if a % 3 == 0:
    num += a
print(num)
   
# %%
result = [ a for a in range(1,1001)
if a % 3 ==0]
print(sum(result))
# %%
result = 0
for n in range(1, 1000):
    if n % 3 == 0: 
        result += n
print(result)
# %%
result = 0
for n in range(1,1001):
  if n %3 == 0 or n % 5 ==0:
    result += n
print(result)
# %%
