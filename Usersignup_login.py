import csv
import re
import bcrypt
import getpass

users = {}

def read_csv():
    try:
        with open('question and answers details.csv',mode ="r") as file:            
            csv_reader = csv.reader(file)
            next(csv_reader)
            score = 0
            email = input("Enter email")
            for row in csv_reader:
                question_text = row[1]
                optionA = row[2]
                optionB = row[3]
                optionC = row[4]
                optionD = row[5]
                print(f"{question_text}")
                print(f"(A){optionA}")
                print(f"(B){optionB}")
                print(f"(C){optionC}")
                print(f"(D){optionD}")
                input_answer = input("Enter options[A/B/C/D]").upper()
                for option in question_text:
                    if option in ['A','B','C','D']:
                        return True 
                answer = row[6]
                print(f"Correct answer is:")
                if not option == answer:
                    print(answer)
                if input_answer == answer:
                    score+=1
                    print("The answer is correct")
                else:
                    print("Incorrect answer")
                if not input_answer in ['A','B','C','D']:
                    print("Invalid")                
                print(f"Your score is {score}") 
        print(f"Email :{email} and score :{score}")
        write_csv("Email and score.csv",[[email,score]])          
                    
    except FileNotFoundError:
        print(f"File {file} not found")
def read2_csv():
    data =[]
    try:
        with open('Email and score.csv',mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("File not found") 
        return data
    #to write the data in csv file
def write_csv(filename,data):
    with open(filename,mode = 'w',newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(data)             
def load_csv():
    try:
        with open("email&password.csv",mode ='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    email,password =row
                    users[email]=password
    except FileNotFoundError:
        print("File not found")
        return
def write_csv(filename,data):
        with open(filename,mode="a",newline ="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
#to check the validation of the password
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'\d',password):
        return False
    if not re.search(r'[#_@%]',password):
        return False
    return True                       
def signup():
    email = input("Enter email:")
    #to check if the email exists or not
    if email in users:
        print("Email already exists")
        return
    password = getpass.getpass("Enter password:").strip()
    if not validate_password(password):
        print("Password must be of 8 characters,contains atleast one digit,one uppercase letter and a special character")
    else:
        hashed_password = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt())
        print("Registered successfully")
        write_csv("email&password.csv",[[email,hashed_password.decode("utf-8")]])#adds the multiple email and password to the csv file
#function for user login
def login():
    email = input("Enter email:")
    if not email in users:
        print("Email not found")
        return   
    password = getpass.getpass("Enter password:").strip()
    stored_hashed_password = users[email].encode("utf-8")
    if bcrypt.checkpw(password.encode("utf-8"),stored_hashed_password):
        #if users[email]==password:
        print("Passwords match")
        print("Login successful!")
        read_csv()
    else:
        print("Incorrect password")
#main program
def main():
    read2_csv()
    while True:
         print("1.User signup")
         print("2.User login")
         print("3.Exit") 
         choice = input("Enter your choice")
         if choice == "1":
            load_csv()
            signup()
         elif choice == "2":
            load_csv()
            login()
         elif choice == "3":
            break
         else:
            print("Invalid choice")
if __name__=="__main__":
    main()                 









