#ATM interface - TASK 1 - Octanet internship - May 2024
'''
The ATMs in our cities are built on Python, as we have all seen them.
It is a console-based application with five different classes.
In order to use the system, the user must enter his or her user ID and pin when it starts.
Once the details are entered successfully, ATM functionality is unlocked. As a result of the project,
the following operations can be performed:
Transactions History
Withdraw
Deposit
Transfer
Quit
'''
import time
import datetime

print("Please insert your card!")
time.sleep(1)
print("-----", end='')
time.sleep(1)
print("-----",end='')
time.sleep(1)
print("-----",end='')
time.sleep(1)
print("-----",end='')
time.sleep(1)
print("-----")
time.sleep(1)
#wait for the user to insert ATM card

balance = 10000
transaction_history=[]

pin = int(input("Enter 4 digit pin: "))
if(pin==1234):
    print("Login successful.")
    x=1
    while(x==1):
        print("-"*25)
        print("1. Check balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Quit")
        try:
            print("-"*25)
            opt = int(input("Choose the option(1/2/3/4/5/6): "))
        except:
            print("-"*25)
            print("You have entered invalid choice! Please try again.")
            exit()

        if(opt==1):
            print("-"*25)
            print("Current Balance : $", balance)
        elif(opt==2):
            print("-"*25)
            withdraw = int(input("Enter the amount to withdraw : $"))
            if(withdraw>balance):
                print("Insufficient Balance!")
            else:
                balance = balance - withdraw
                d = datetime.date.today()
                transaction_history.append(" Withdrawal  \n         Amount : {} \n         Balance : {} \n         Date : {}".format(withdraw,balance,d))
                print("$",withdraw," debited from your account successfully.")
                print("New balance : $",balance)
        elif(opt==3):
            print("-"*25)
            deposit = int(input("Enter the amount to deposit : $"))
            balance = balance + deposit
            d = datetime.date.today()
            transaction_history.append(" Deposit  \n         Amount : {} \n         Balance : {} \n         Date : {}".format(deposit,balance,d))
            print("$",deposit," credited to your account successfully.")
            print("New balance : $",balance)
        elif(opt==4):
            print("-"*25)
            print("1. UPI transfer")
            print("2. Account Transfer")
            print("3. Phone Transfer")
            try:
                opt_t = int(input("Choose transfer type : "))
            except:
                print("-"*25)
                print("Invalid Choice! Please try again")
                exit()
            match(opt_t):
                case 1:
                    username = input("Enter Recipient name : ")
                    upi = input("Enter UPI id : ")
                    upi_t = int(input("Enter the amount to transfer : $"))
                    if(upi_t>balance):
                        print("Insufficient Balance!")
                    else:
                        balance = balance - upi_t
                        d = datetime.date.today()
                        transaction_history.append("UPI Transfer \n         Recipient Name : {} \n         Recipient UPI : {}\n         Amount : {} \n         Balance : {} \n         Date : {}".format(username,upi,upi_t,balance,d))
                        print("$",upi_t," tranferred to ",username," with UPI id : ",upi ," from your account successfully.")
                        print("New balance : $",balance)
                case 2:
                    username = input("Enter Recipient name : ")
                    acc = int(input("Enter 10 digit Account Number : "))
                    acc_t = int(input("Enter the amount to transfer : $"))
                    if(acc_t>balance):
                        print("Insufficient Balance!")
                    else:
                        balance = balance - acc_t
                        d = datetime.date.today()
                        transaction_history.append("Account Transfer \n         Recipient Name : {} \n         Recipient Account No. : {} \n         Amount : {} \n         Balance : {} \n         Date : {}".format(username,acc,acc_t,balance,d))
                        print("$",acc_t," tranferred to ",username," with Account No. : ",acc ," from your account successfully.")
                        print("New balance : $",balance)
                case 3:
                    username = input("Enter Recipient name : ")
                    phn = input("Enter Phone No. : ")
                    phn_t = int(input("Enter the amount to transfer : $"))
                    if(phn_t>balance):
                        print("Insufficient Balance!")
                    else:
                        balance = balance - phn_t
                        d = datetime.date.today()
                        transaction_history.append("Phone Tranfer \n         Recipient Name : {} \n         Recipient Phone No. : {} \n         Amount : {} \n         Balance : {} \n         Date : {}".format(username,phn,phn_t,balance,d))
                        print("$",phn_t," tranferred to ",username," with Phone No. : ",phn ," from your account successfully.")
                        print("New balance : $",balance)
        elif(opt==5):
            print("Transaction History".center(50,"-"))
            print("|| # ||           Transaction           ||")
            print("-"*50)
            j=1
            for i in transaction_history:
                print("|| {} ||".format(j), i,)
                j=j+1
                print("-"*50)
        elif(opt==6):
            print("Thank you for visiting us!".center(50,"-"))
            x=0
            


else:
    print("Incorrect pin entered! Please try again.")
    