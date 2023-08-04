name = ("enter the name")
family= ("enter family")
num1=int(input("enter chemistry score"))
num2=int(input("enter math score"))
num3=int(input("enter physic number"))
so = num1 + num2 + num3
avrage = so / 3
if avrage < 12:
    print("fail")
if 12 >avrage<17:
    print ("normal")
    if avrage >=17 :
        print ("great")
        print("your name ","is" , name , family , "your", "avrage" , "is" , avrage ) 
