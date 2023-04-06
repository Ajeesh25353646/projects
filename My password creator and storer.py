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
    
    password = "".join(map(str,password))
    print(f"Id: {id}")
    print(f"created password: {password}")

    
    ### making panda series for the password    
    pass_data = pd.DataFrame(data={ "password": password, "website or app": website}, columns=["password","website or app"], index=[id]).reset_index().rename(columns={"index":"id"}).set_index("id")
    print(pass_data)


    # path where passwords will be saved
    path = "D:/my password.csv"
    with open(path , "w") as file:
        pass_data.to_csv(file, header=not file.tell())
    print("Password data saved to file {path}")
create_pass()