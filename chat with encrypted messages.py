################################    new project      ###########################################

# Coding:
# if the word contains atleast 3 characters,
# remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# then reverse it 
# else:
#   simply reverse the word

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end.
# Now remove the first letter and append it to the end
# reverse the string

# Your program should ask whether you want to code or decode
import random



def encode(str1):
    random_char = list("qwertyuiopasdfghjklzxcvbnm")
                # print(random_char)
    
    codelist = []
    
    
    for word in str1.split():
        if len(word) >= 3:
            # for char in word:
                prefix = random.sample(random_char,k=3)
                prefix = "".join(prefix)
                # print(prefix)
                suffix = random.sample(random_char,k=3)
                suffix = "".join(suffix)
                # print(suffix)
                
                # removing first char and taking it to end
                first_lvl = word[1:] + word[0]
                # print(first_lvl)
                # adding 3 random characters in the start and end
                second_lvl = prefix + first_lvl + suffix
                # now reversing the secret code 
                final_coded_char =  second_lvl[::-1]            
                codelist.append(final_coded_char)
                
        else:
               rev = word[::-1] 
               codelist.append(rev) 
    return codelist
    
print(encode("secret language"))



def decode(codelist1):
    decodedlist = []
    for x in list(codelist1):
        if len(x) < 3:
            res = x[::-1]
            decodedlist.append(res)
        else:
            decode1 = x[3:-3:1]        # removing 3 random char at terminals
            decode2 = decode1[1:] + decode1[0]      # removing first char and taking it to end           
            decoded = decode2[::-1]     # reversing the code         
            decodedlist.append(decoded)
    return decodedlist

print(decode(['bgesterceizx', 'yhslegaugnadgs']))



                




                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
