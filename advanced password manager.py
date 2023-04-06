######### advanced password manager ##########
########### MY PASSWORD GENERATOR AND STORER ###########

import random
import pandas as pd


def create_pass():
    id = input("enter the username or gmail account of the account\
 you want the password for: ")
    strength = input("tell how strong the password should be\
 (very strong, strong, weak): ")
    website = input("Enter website or app name for\
 you are creating the password: ")
    
    
    ## password in making
    alphabets = list("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm")
    numbers = range(0,10)
    special_char = list("%#@-_~")

    if strength == "very strong":
        password = random.sample(alphabets, 4) + random.sample(special_char, 1) + random.sample(numbers,4 )
    elif strength == "strong":
        password = random.sample(alphabets, 4) + random.sample(numbers, 4)  
    elif strength == "weak":
        password = random.sample(numbers, 8)
    else: 
        raise ValueError("incorrect strength,ask for very strong or strong or weak")
    
    # converting the passlist to string and then joining them to make a string
    password = "".join(map(str,password))
    print(f"Id: {id}")
    print(f"created password: {password}")


############## encrypting password before saving it to file ############
    ############# encoding password before saving it
    
    # random char list
    random_char = list("qwertyuiopasdfghjklzxcvbnm")

    prefix = random.sample(random_char,k=3)     # 3- digit prefix
    prefix = "".join(prefix)
    # print(prefix)
    suffix = random.sample(random_char,k=3)        # 3- digit suffix
    suffix = "".join(suffix)
    # print(suffix)
    
    # removing first char and taking it to end
    first_lvl = password[1:] + password[0]
    # print(first_lvl)

    # adding 3 random characters in the start and end
    second_lvl = prefix + first_lvl + suffix
    # now reversing the secret code 
    final_coded_char =  second_lvl[::-1]
    global encrypt_pass  
    encrypt_pass = final_coded_char


##################### password becomes encrypted ##########
    
    # encrypted password will get stored to file
    # print(encrypt_pass)

    
    # Making panda series for the password and storing encrypted password to file
    pass_data = pd.DataFrame(data={ "password": encrypt_pass, "website or app": website, "Id":id},index=[0], columns=["password","website or app","Id"])
    print(f"\nThis data has been saved alongwith password in encrypted form:\n{pass_data}")

    with open("D:/advanced passwords.csv", 'w') as file:
        pass_data.to_csv(file, header=not file.tell())
create_pass()



