# This programe crack the ecrypted password....
# author : AQIB_ALI
# Location : Earth 
# time : 11:43 pm
try:
    import hashlib
except:
    print("Install 'hashlib' on your device") 

hash_pass =  input("Enter md5 encrypted password : ")
wordlist = input("Enter Path of your wordlist name : ").strip()
if (len(wordlist) == 0 ):
    wordlist = "wordlist.txt"
flag = 0
try:
    list = open(wordlist , "r")
except:
    print("File not found ")
    quit()
counter = 1
for word in list :
    a = word.encode("utf-8")

    # We  can use another format of encrypted password e.g(sha256,sha1,sha224)
    # Here we can use md5 for encryption

    b = hashlib.md5(a.strip()).hexdigest()
    # print(counter)
    # counter += 1
    if (b == hash_pass.strip()):
        '''
        print(
        f"""\t\t================= Password is found ===================

                        Your password is : {word}
                        
        \t=======================================================                
        """
        )
        '''
        print(f"\n\t [ Found ] Your password is : {word}")
        flag = 1
        break
if flag == 0:
    print("Your password is not found in wordlist")
    print("Please try another wordlist")