
# %%
#1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면?
from multiprocessing.spawn import import_main_path


A = [a for a in range(1,1001)
if a % 3 ==0]
B = [b for b in range(1,1001)
if b % 5 ==0]
print(sum(A+B))
# %%
# def fibo(n):
#   if n <=1:
#     return 1
#   else:
#     return (fibo(n-2)+fibo(n-1))   

# result = [fibo(n) for n in range(1,10)]
# # if fibo(n) % 2 ==0
# # if fibo(n) <4000000]
    

# print(result)
#2번 재귀함수

# %%
import math 
###################################오일러2번
#피보나치 수열에서 4백만 이하이면서 짝수인 항의 합
def fibo2(n):
  beta = (1 + (5)**0.5 )/2
  alpha = (1 - (5)**0.5)/2

  an = (5**(-0.5)) * (beta**n - alpha**n)
  return an 

result = [fibo2(n) for n in range(1,200)
if int(fibo2(n))%2==0
if fibo2(n) <=40000]

print(int(sum(result)))
# %%
#가장 큰 소인수 구하기
num = 600851475143
a = 2
while a<num:
  if num % a==0:
    num /= a
  else:
     a += 1
print(num)
# %%
#	세자리 수를 곱해 만들 수 있는 가장 큰 대칭수
result =[a*b for a in range(100,1000)
 for b in range(100,1000) 
 if str(a*b) == str(a*b)[::-1]]

print(max(result))
# %%
#	1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수
import math 
LCM = 1
for a in range(1,21):
  GCD = math.gcd(a, LCM)
  LCM = int(a*LCM/GCD)
print(LCM)
# %%

#1부터 100까지 "제곱의 합"과 "합의 제곱"의 차는?
import math 
A = [a for a in range(1,101)]
S= math.pow(sum(A), 2)
B = [b**2 for b in range(1, 101)]
print(S-sum(B))

# %%
#10001번째의 소수
# prime_number= [a for a in range(1,101)
# if ]


for i in range(1,101):
    for j in range(2, i+1):
        if (j == i):
            print(i)
        elif (i % j == 0):
            break

# %%
