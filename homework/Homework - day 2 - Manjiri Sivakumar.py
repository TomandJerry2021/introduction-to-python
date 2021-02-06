# Homework - Day 2 - Manjiri Sivakumar
#
# Question 1
#
list = [10,20,30,40,100,200,300,400]
temp1 = list[0:4]
temp2 = list[4:8]
list=temp2+temp1
print(list)

# Question 2
#
n=int(input("please enter single digit integer "))
for i in range (0,n+1):
    if i%2==0:
        print(i)
        
