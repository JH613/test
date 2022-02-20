#%% case 1
sum=0
while True:
    num = int(input())

    if num < 0:
        break
    else:
       sum += num

print(sum)

#%% case 2
sum = 0

num_list = list(input("값을 입력하세요").split(' '))
print(type(num_list))

for i in num_list: #이거 진짜 중요
    num = int(i)
    print(type(i))
    sum += num

print(sum)

"""
변수의 자료형을 볼수 있는 명령이 잇음
print(type(i))
"""

# %%
