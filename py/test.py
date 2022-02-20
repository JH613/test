#%% case 1
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
