def company():
    sal=int(input("enter salary of employee:"))
    exp=int(input("enter experience of employee:"))
    if exp<5:
        print(sal)
    else:
        bonus=sal*5/100
        print("bonus amount=",bonus)
        sal=sal+bonus
        print("salary of employe plus bonus =",sal)
company()
