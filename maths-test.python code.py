import random
a=int(input("Enter minimum number:"))
b=int(input("Enter maximum number:"))
c=['+','-','*','/']
print("problems comes on above numbers")
def exam():
    d=random.randint(a,b)
    e=random.randint(a,b)
    f=random.choice(c)
    exp=str(d)+" "+f+" "+str(e)
    ans=eval(exp)
    return exp,ans
vl=0
for v in range(10):
    exp,ans= exam()
    g=float(input(f"problem {(v+1)} -> {exp} ="))
    while vl<10:
        if g==ans:
            print("Answer is Correct")
            vl+=1
            break
        else:
            print("Answer is Wrong")
            break
input("----------------------click Enter see Results-------------------")
mk=10-vl
k=10/2
print(f"Correct Annwers:{vl}")
print(f"Wrong   Answers:{mk}")
if vl>=k:
    print("-------------------------Congratulations You Passed Exam--------------------")
    print("----------------------------Enjoy Pandagoww---------------------------------")
else:
    print("-------------------You Failed Exam---------------------")
    print("-----------------Better luck Next Time-------------------")
