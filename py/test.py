#%% case 1
from audioop import add
from ctypes.wintypes import PINT
from re import S
from this import d


test_score = [100, 20, 40 ,37, 41]
num = 0
for a in test_score :
  num = num + 1
  if a >= 60:
    print("%d번 합격." % num)
  else:
   print("%d번 불합격." % num)


# %%
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)
# %%
treeHit = 0
while treeHit <100 :
 treeHit = treeHit +1 
 print("나무를 %d번 찍었습니다" % treeHit)
 if treeHit == 100:
   print("김석환이 죽습니다")
# %%
pocket = ['', 'smartphone','paper' ]
if 'momey' in pocket:
    print("택시를 타고 귀가")
else:
      print("돈을 뺏어서 택시를 타고 귀가")

# %%
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
# %%
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: 
        result += i
    i += 1

print(result) 

# %%
# S skill
ad = 100
add_Ad = ad+(0.58+0.16)*100
add_Damage = 1.2*1.5
skill_Damage_S = 0.5*add_Ad + 1000
s = skill_Damage_S*add_Damage
print(round(s))

# C skill
ad = 180 
add_Ad = ad+(0.12+0.13)*100
add_Damage = 1.05*1.11
skill_Damage_C = 0.2*add_Ad + 1200
c = skill_Damage_C*add_Damage
print(round(c))
if c > s:
    print("C가 S보다 강하다")
else:
    print("S가 C보다 강하다")
     
# %%

# %%
