while True:
    a=input("enter your password")
    print(a)
    if  a.isalpha() == False and a.isdigit() == False and len(a)>8 :
        print("loading...")
        break
    else:
        print ("sorry yp is wrong")





