import random 
import os 
import datetime
import json 
 
Expenses = "Expense_record.json"

def clrsrc():
    os.system("cls" if os.name == "nt" else "clear" )

def seperator(char = "=", width = 55):
    print("  ",char*width)
    
def seperatar(char = "=", width = 55): 
    print("  ",char*width)
    
def Menu():
    seperator()
    print(f"{  '--- YOUR EXPENSE TRACKER ---':^55}")
    seperator()
    print(f" { 'a. Create Your Account --> 0':^6}")
    print(f" { 'a. Add Your Expense    --> 1':^6}")
    print(f" { 'b. View All Expense    --> 2':^6}")
    print(f" { 'c. View Total Spending --> 3':^6}")
    print(f" { 'd. View By Category    --> 4':^6}")
    print(f" { 'e. Delete an Expense   --> 5':^6}")
    print(f" { 'f. Exit                --> 6':^6}")
    seperatar()
    seperator()
    
def pause():
    input("\n Press the enter for continue!!")

# Json file wale function 
def loadfile():
    if os.path.exists(Expenses):
        with open(Expenses,"r") as f:
            return json.load(f)
    else:
        print("File Doesn't Existed!")
        return {}

def savefile():
    with open(Expenses,"w") as f:
        return json.dump(Expenses_dict,f, indent=4)

Expenses_dict = loadfile()

# Control panel mai use hone wale function
class Control_panel:
    
 def Account_Create(self):
    self.Name = input('Enter Your Name ').strip()
    self.Your_ID = str(random.randint(10000,99999))
    Expenses_dict[self.Your_ID] = {
           "Name" : self.Name,
           "Your_ID": self.Your_ID,
           "expense" : []
        }
    print(self.Your_ID, 'This is Your Account ID!')
    savefile()
    
    
 def ADD_Expenses(self):
    self.Your_ID = input("Enter Your ID please: ")
    if self.Your_ID not in Expenses_dict:
        print("Please Enter the Valid ID! ")
        pause()
        return
    
    else:
        Num = int(input("Enter the Number of Expenses you wanted to add: "))
        for num in range(Num):
         self.Categories = input("Enter the Category of Your Expense: ")
         self.Descrep = input("Enter your Expense: ")
         self.amount = input("Enter the Amount Your Spend: ")
         self.category_ID = random.randint(1000,9999)
         print('Your Category ID is this',self.category_ID)
         self.Date = datetime.datetime.now().strftime("%Y-%m-%d")
         New_Expense  = {
            "Category_ID" : self.category_ID,
            "Description" : self.Descrep,
            "Amount" : self.amount,
            "Category" : self.Categories,
            "Date" : self.Date
         }
         Expenses_dict[self.Your_ID]["expense"].append(New_Expense)
        savefile()
         
         
 def View_all_expense(self):
    self.Your_ID = input("Enter Your ID please: ")
    if self.Your_ID in Expenses_dict:
        seperator()
        print('Your Expenses sir;')
        seperatar()
        for exp in Expenses_dict[self.Your_ID]["expense"]:
            print(f" Your Category ID: {exp['Category_ID']}")
            print(f" Your Description: {exp['Description']}")
            print(f" Your Amount: {exp['Amount']}")
            print(f" Category:  {exp['Category']}")
            print(f" Date Of Expense:  {exp['Date']}")
        seperator()
    else:
        print("Please Enter the Valid ID! ")
        pause()
        return
        
        
 def View_Total_spending(self):
    self.Your_ID = input("Enter Your ID please: ")
    if self.Your_ID in Expenses_dict:
        Total = 0
        for exp in Expenses_dict[self.Your_ID]["expense"]:
            Total = Total + int(exp["Amount"])
        seperatar()
        print(f" Your Total Spending Sir -> ${Total}")
    else:
        print("Please Enter the Valid ID! ")
        pause()
        return
    
        
        
 def View_by_Category(self):
    self.Your_ID = input("Enter Your ID please: ")
    if self.Your_ID in Expenses_dict:
        search = input('Enter the Category of Expense for search: ')
        seperatar()
        for exp in Expenses_dict[self.Your_ID]["expense"]:
            if search == exp["Category"]:
             print(f" Your Category ID: {exp['Category_ID']}")
             print(f" Your Description: {exp['Description']}")
             print(f" Your Amount: {exp['Amount']}")
             print(f" Category:  {exp['Category']}")
             print(f" Date Of Expense:  {exp['Date']}")
        seperatar()
    else:
        print("Please Enter the Valid ID! ")
        pause()
        return
        
    
 def Delete_Expense(self):
    self.Your_ID = input("Enter Your ID please: ")
    if self.Your_ID in Expenses_dict:
        Cate = int(input('Enter your Category ID: '))
        found =False
        for exp in Expenses_dict[self.Your_ID]["expense"]:
            if Cate == exp["Category_ID"]:
                Expenses_dict[self.Your_ID]["expense"].remove(exp)
                found = True
                savefile()
                return
        if not found:
            print('Invalid Category ID!!')
            pause()
    else:
        print("Please Enter the Valid ID! ")
        pause()
        return
        
             
 def Control_Section(self):
    seperator()
    while True:
     Menu()
     
     try:
        Choice = int(input('Enter the Your Option: '))
     except:
        print('Invalid Choice! Please Enter Valid Option')
        pause()
        continue
     if Choice == 0:
         seperator()
         self.Account_Create()
         pause()
         clrsrc()
     elif Choice == 1:
         seperator()
         self.ADD_Expenses()
         pause()
         clrsrc()
     elif Choice == 2:
         seperator()
         self.View_all_expense()
         pause()
         clrsrc()
     elif Choice == 3:
         seperator()
         self.View_Total_spending()
         pause()
         clrsrc()
     elif Choice == 4:
         seperator()
         self.View_by_Category()
         pause()
         clrsrc()
     elif Choice == 5:
         seperator()
         self.Delete_Expense()
         pause()
         clrsrc()
     elif Choice == 6:
         print('Exiting')
         break
     else:
        print('Invalid Choice! Please Enter Valid Option')
        pause()
        clrsrc()

obj = Control_panel()
obj.Control_Section()