from User import UserClass

class Login:
    __db = []
    def __init__(self):
        self.print_menu()
    def print_menu(self):
        print("Welcome User")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
    def create_user(self, name, email, password):
        new_user = UserClass(name, email, password)
        self.__db.append(new_user)
        print(self.__db)
        return True
    def validate_user(self, email, password):
        temp=self.__db.copy() 
        for user_obj in temp:
           if email==user_obj.email: 
             if password==user_obj.get_user_password(): 
                return True 
             else: 
                 return False 
             #return false because email not found     
        return False                 

obj = Login()
while True:
    option = input("Enter your choice: ")
    if option == '1':
        name = input("Enter your full name: ")
        email = input("Enter Email: ")
        password = input("create new password: ")
        res = obj.create_user(name,email, password)
        if res == True:
            print("User created successfully")
    elif option == '2':
        email=input("enter email:") 
        password=input("enter password:")
        if obj.validate_user(email,password): 
            print("login success") 
        else: 
             print("login failed") 

    elif option == '3':
        break
    else:
        print("Invalid Input")




