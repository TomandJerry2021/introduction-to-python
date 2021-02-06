# Homework - day 3 - Manjiri Sivakumar
#
#Question
#
un = "spring"
pw = "abcd"
a= input("please provide a user name ")
b= input("plese provide a password ")
if a!=un:
    print("user name is not correct")
elif b!=pw:
    print("password is not correct")
else :
    print("login is success")

#
#Extra
#
my_dict={"emmy":"they", "lou":"wat", "melary":"xyz"}
e=input("please provide a user name ")
f=input("please provide a password ")

if e not in my_dict.keys():
    print("user name is incorrect")
elif f != my_dict[e]:
    print("password is incorrect")
else :
    print("login is success")
    
    




