############### password extractor and decoder #################
import pandas as pd

############## extracting passwords ####################
def get_password():
    Id = input("Enter the username or id or gmail: ")
    website = input("Enter the website or app name associated: ")
    
    
    
    # reading file to extract password 
    pass_data = pd.read_csv("D:/advanced passwords.csv")
    encrypt_password = pass_data.loc[((pass_data["Id"] == Id) & (pass_data["website or app"] == website)), "password"]
    if len(encrypt_password) == 0:
        print(f"No password found for user {Id} and website {website}")
        return
    
############# decrypting password ###########################
    encrypt_pass = str(encrypt_password[0])
    decode1 = encrypt_pass[3:-3:1]   # removing 3 random char at terminals
    decode2 = decode1[1:] + decode1[0]      # removing first char and taking it to end           
    decoded = decode2[::-1]     # reversing the code         
    print(f"password for {Id} is {decoded}")

get_password()





