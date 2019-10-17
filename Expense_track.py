import numpy as np
import pandas as pd
def create_category(category,category_name):
    name=input("\n\tEnter the Category Name : ")
    category_name.append(name)
    category[name]=[]
def allocate_expense(category,category_name):
    print("\n\n\tSelect the category : \n")
    for i in range(len(category_name)):
        print(f"\t{i+1}.{category_name[i]}")
    select=int(input("\n\tSelect your Category : "))
    amount=float(input("\n\t\tEnter the Expense amount : "))
    category[category_name[select-1]].append(-amount)
def daily_expense_chart():
    pass
def monthly_expense_chart():
    pass
def yearly_expense_chart():
    pass
print("\n\n*****Expense Tracker*****\n\n")
print("\n\nMENU\n\n")
category={}
category_name=[]
while True:
    print("\n0.To exit from Interface\n1.Set Catagories\n2.Enter Expense for current Date\n3.Show Daily Expense Chart\n4.Show Monthly Expense Chart\n5.Show Yearly Expense Chart\n\n")
    choice=int(input("\nEnter Your Choice : "))
    if choice==1:
        create_category(category,category_name)
    elif choice==2:
        allocate_expense(category,category_name)
    elif choice==3:
        daily_expense_chart()
    elif choice==4:
        monthly_expense_chart()
    elif choice==5:
        yearly_expense_chart()
    else:
        break
chart=pd.DataFrame(category)
print(chart)
print("\n\nThank You!\n")