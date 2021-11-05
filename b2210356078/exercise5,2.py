mail= input("please enter a thing that you want it to check e-mail or not:")
x = "@" and "." in mail
if x==True:
    print("That is a e-mail.")
else:
    print("That is not a e-mail.")