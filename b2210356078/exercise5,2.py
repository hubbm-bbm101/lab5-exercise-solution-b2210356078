def isitemail(m):
    if "@" and "." in m:
        return True
    else:
        return False        
email = input("please enter a thing that you want it to check e-mail or not:")
if isitemail==True:
    print("That is a e-mail.")
else:
    print("That is not a e-mail.")
