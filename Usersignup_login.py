import csv
users = {}
#to load data in csv file
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
    else:
        print("Incorrect password")
#main program
def main():
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
#load_csv()
#write_csv(filename='email&password.csv',data=[['email','password'],['moksha123@gmail.com','moksha09']])