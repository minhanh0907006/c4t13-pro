while True:
    txt=input("Enter a number")
    print(txt)
    if txt.isdigit():
        print("year of birth")
        break
    else:
        print("not a number") 

print(2019-int(txt))