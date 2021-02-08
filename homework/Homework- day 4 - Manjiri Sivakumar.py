#
#Homework - day 4 - Manjiri Sivakumar
#
#Question 1
#
prim_list = []
for i in range (2, 101):
    ctr=0
    for n in range (2, i):
        if  i%n==0 :
            ctr += 1
            break
    if ctr < 1:
        prim_list.append(i)

print(prim_list)
        
    
        
