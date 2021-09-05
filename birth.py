import random
birth_list=list()
for i in range(0, 23):
    num=random.randint(0,366)
    birth_list.append(num)
from itertools import combinations 
prob_list=list(combinations(birth_list, 2))

print(birth_list)
#print(prob_list)
num=0
cnt=0
for i in prob_list:
    cnt+=1
    print(i)
    print(i[0],i[1])
    if i[0]==i[1]:
       num+=1    
       print(num) 
      
       
print(cnt)       
prob=num/len(birth_list)  
print(num)
print(len(prob_list))  
print(prob)    
