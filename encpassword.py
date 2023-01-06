import hashlib
import os
a = input("Please Enter your password : ")
b = a.encode("utf-8")
# We  can use another format of encrypted password ...
# Here we can use sha256 for encryption
crack = hashlib.md5(b).hexdigest()

# print(f"Your Encrpted passwor is : {crack} ")
print(
        f"""\t\t================= Password is Encrypted ===================

                    Your password is : {crack}
                        
        \t=======================================================                
        """
       )
u =  os.getlogin()
try:
    FILE = f"c:/users/{u}/Encrypted_password.txt"
    with open(FILE , "a") as f:
        f.write(f"Your simple passoword is : {a} \n")
        f.write(f"Your Encrpted passoword is:\n{crack}")
        f.write("\n================================================================\n")
except Exception as e:
    print ( "[ERROR]" , e)
    
print( f"[+] Your password is saved in : {FILE}")
