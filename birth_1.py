num=int(input("숫자를 입력하세요"))
prob=1
for i in range(num):
    prob=prob*((365-i)/365)
print(1-prob)