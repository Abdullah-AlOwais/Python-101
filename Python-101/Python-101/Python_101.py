'''
-------> CONTACTS PROJECT <-------
Project descraption:
This project is for one of the "Full Stack Python" Courses 
which consists of several courses and each course contains a simple project,
provided by منصة سطر التعليمية

"You will find the full project explanation at GitHub.."

Credit to Abdullah AlOwais
Email: aalowais@outlook.sa

'''

#book Numbers list
Contacts={
    1111111111:"Amal",
    2222222222:"Mohammed",
    3333333333:"Khadijah",
    4444444444:"Abdullah",
    5555555555:"Rawan",
    6666666666:"Faisal",
    7777777777:"Layla"
    }


#function to add a new numbers
def addToContacts(name,num):
    while(True):
        if num.isdigit() and len(num) == 10: # -> check if the input is 10 digit
            
            for x,y in Contacts.items(): # -> x = key (Phone Number) / y = value(Name)    
                
                if str(x) == num:
                     print("The Contact's Number is Already Exists") 
                     print("Do You Want to Updated again?")
                     ans = input(" >> Yes / No  ? ")
                     if ans in ['n', 'N', 'no', 'No', 'NO']:
                         print("---------------------------------------------------\n")
                         return None
                     elif ans in ['y', 'Y', 'yes', 'Yes', 'YES']:
                         Contacts.update({num:name})
                         print("\n And it Has Been Updated Successfully!"+
                         "\n---------------------------------------------------\n")
                         return None
            else: 
                 Contacts.update({num:name})
                 print("The contact has been added successfully!")
                 return None
        else:
            print("This is invalid number!, Try Again..")
            num=input("Enter the Phone Number : ")    
            print("---------------------------------------------------\n")


#Function to Search in Contacts By Name
def searchInContactsByName(name):
    for x,y in Contacts.items(): # -> x = key (Phone Number) / y = value(Name)    
        if y == name:
            print("The Phone Number is : ",x)
            print("---------------------------------------------------")
            break
    else:
         print("Sorry, the Name is not found!\n")
         print("Do You Want to Search again?")
         ans = input(" >> Yes / No  ? ")
         if ans in ['n', 'N', 'no', 'No', 'NO']:
             print("---------------------------------------------------\n")
             return None
         elif ans in ['y', 'Y', 'yes', 'Yes', 'YES']:
             print("\n---------------------------------------------------\n")
             searchInContactsByName(input("Enter the Name : "))
                    
         else:
            print("Wrong Answer Try Again! \n"+
            "---------------------------------------------------\n")


#function to search in Contacts by Number
def searchInContactsByNumber(num):
    while(True):
        
        if num.isdigit() and len(num) == 10: # -> check if the input is 10 digit 
        
            for x,y in Contacts.items(): # -> x = key (Phone Number) / y = value(Name)
                if str(x) == num:
                    print("The Name of This Phone Number is : "+y)
                    print("---------------------------------------------------")
                    break
            else:
                print("Sorry, the number is not found!")
                print("---------------------------------------------------")
            break   
        else:
            print("---------------------------------------------------")
            print("This is invalid number!, Try Again..")
            num=input("Enter the Phone Number : ")    
            print("---------------------------------------------------\n")


start = True #to control the loop
print("---------------------------------------------------\n"+
      "         >>> Welcome to Contacts <<<\n"+
      "---------------------------------------------------\n")


while(start):
    print("  1 -> Search\n"+
          "\n  2 -> Add\n"+
          "\n  0 -> Exit\n")
    choice= input("\n please Enter your Choice : ")
    print("---------------------------------------------------\n")
    if choice in ['0','1','2']:
       
        if choice == "1":
            print("How do you want to search?\n"+
                  "\n  1- By The Name\n"+
                  "\n  2- By The Number\n"+
                  "\n  0- Go Back\n")
            searchMethod = (input("Enter the Number : "))
            if searchMethod in ['0','1','2']:
                if searchMethod =='1':
                    print("---------------------------------------------------\n")
                    searchInContactsByName(input("Enter the Name : "))
                elif searchMethod == '2':
                    print("---------------------------------------------------\n")
                    searchInContactsByNumber(input("Enter the Phone Number : "))
                elif searchMethod == '0':
                    print("---------------------------------------------------\n")
                    continue  
        
        elif choice == "2":
            addToContacts(input("Enter the Name : "),input("Enter the Phone Number : "))
        
        elif choice == "0":
            print("----------------------\n"+
                  "   >> Thank You! <<   \n"+
                  "     >>> Bye! <<<     \n"+
                  "----------------------\n")
            break #end the program
        


        while(True):
            print("\n >> Do you want another service? <<")      
            ans = input(" >> Yes / No  ? ")
            if ans in ['n', 'N', 'no', 'No', 'NO']:
                print("----------------------\n"+
                      "   >> Thank You! <<   \n"+
                      "     >>> Bye! <<<     \n"+
                      "----------------------\n")
                start=False #end the program
                break
            elif ans in ['y', 'Y', 'yes', 'Yes', 'YES']:
                print("---------------------------------------------------\n")
                break
            else:
                print("Wrong Answer Try Again! "+
                      "---------------------------------------------------\n")
                      

    else:
        print("---------------------------------------------------\n")
        print("  >>> Wrong Choice! Try Again <<<")
        print("---------------------------------------------------\n")
                
