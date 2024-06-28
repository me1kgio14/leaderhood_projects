import random
#step 1 crate acount

user_name=input("enter name:")
user_email=input("enter your email:")
password=input("enter password:")
confirm_pass=input("confirm your password:")

#step 2 crate function to sign in





#step 3 crate function to transaction
def perform_transaction(transaction,):
    list=[50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000] #this list is for choose random balance 
    balance=random.choice(list) #this function random chosing amount of balance
    print("your balance is "+str(balance))
    input("enter acount id to make transaction:")
    if balance>=transaction:
        balance-=transaction
        
    else:
        print("you dont have enough balance")
    return "your curent balance is "+str(balance)






#4 crating a function to confirm user choice
def bank_system(choice):
    choice=input("you are in bank!!   enter '1' to do transation,enter '2' to delete this ecount")
    if choice=="1":
        print(perform_transaction(int(input("enter amoun of cash,you want to transfer:"))))
    
    elif choice=="2":
        input("click enter to delete your acc")
        print("your acount deleted")

    else:
        return "you entered wrong number"


user_choice=input("you are in bank!!   enter '1' to do transation,enter '2' to delete this ecount")
print (bank_system(user_choice))