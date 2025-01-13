import csv
users = {}
#to load data in csv file
def read_csv():
    try:
        with open('question and answers details.csv',mode ="r") as file:            
            csv_reader = csv.reader(file)
            next(csv_reader)
            score = 0

            #name=input("Enter participant name")
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
                    print("Invalid")
                print(f"Your score is {score}") 
        #print(f"Name :{name} and score :{score}")  
    except FileNotFoundError:
        print("File not found")    
def load_csv():
    try:
        with open("email&password.csv",mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                email,password=row
                users[email] = password
    except FileNotFoundError:
        print("File not found")
        return
#to write data in csv file
def write_csv(filename,data):
    with open(filename,mode = "w",newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(data)

#Function for user signup
def signup():
    email = input("Enter email")
    #to check if email exists or not
    if email in users:
        print("Email already exists")
        return
    password = input("Enter password")
    users[email] = password
    write_csv("email&password.csv",[[email,password]])
    print("User registered successfully!")
#function for user login
def login():
    email = input("Enter email")
    if not email in users:
        print("Email not found")
        return
    password = input("Enter password")
    if users[email] == password:
        print("Login Successful!")
        write_csv("email&password.csv",[[email,password]])
        read_csv()
    else:
        print("Incorrect password")
        
#main program
def main():
    load_csv()
    while True:
        print("1.User signup")
        print("2.User login")
        print("3.Exit")
        choice = input("Enter your choice:")
        if choice =="1":
            signup()
        elif choice =="2":
            login()
        elif choice =="3":
            break
        else:
            print("Invalid choice")
if __name__ =="__main__":
    main() 
#calling functions                   
#write_csv(filename='email&password.csv',data=[['email','password'],['moksha123@gmail.com','moksha09']])
