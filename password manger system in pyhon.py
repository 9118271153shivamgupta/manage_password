import pickle
import pyperclip

user_id=input("Enter the user ID(press 1 to create account):" )

dictionary = {}

with open("D:\code with harry\project(python\\pass_man.txt","br") as filewrite:
    dictionary = pickle.load(filewrite)

if "1" in user_id:
    email=input("Enter the user ID: ")

    with open("D:\code with harry\project(python\\email.txt","w") as f:
        store_email=f.write(email)
    

    possword = input("Enter the possword: ")

    with open("D:\code with harry\project(python\\pass.txt","w") as a:
        store_pos=a.write(possword)

with open("D:\code with harry\project(python\\email.txt","r") as fr:
        store_email=fr.read()

if  user_id== store_email:
    possword2=input("Enter the your posswors: ")

    with open("D:\code with harry\project(python\\pass.txt","r") as ar:
        store_pos=ar.read()

    if possword2==store_pos:
        conf=input("to know your possword press '1' to save your possword press'2': ")
        if "2"  in conf:
            account=input("entre your account name: ")
            acc_poss=input("enter Your account possword : ")

            confermation =input("woule you like to save it(y/n): ")
            
            if "y" in confermation:
                dictionary[account]=acc_poss

                with open ("D:\code with harry\project(python\\pass_man.txt","bw") as readfile:
                    dictionary=pickle.dump(dictionary,readfile, protocol=2)
                print("Done! your{account}'s possword has been saved")
            
            
            else:
                print("your data has not saved....")
        if "1"in conf:
            email1=input("which account's password you want to know : ")

            with open("D:\code with harry\project(python\\pass_man.txt","bw") as file:
                dictionary=pickle.load(file)
            

            if email1 in dictionary:
                print(f" your{email}'s password is {dictionary[email1]}")
                print("Your password  has been saved to YOur cilpboard")
                pyperclip.copy(dictionary[email1])
            else:
                print("This passord is not saved")



            



        


    



