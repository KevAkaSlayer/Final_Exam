class Bank_SYS:
    def __init__(self) -> None:
        self.users = []
        self.balance = 0
        self.loan_gave = 0
        self.loan_op = True
    def create_user(self,name,email,address,types):
        ac_num= len(self.users)+1
        user = USER(name,email,address,types,ac_num)
        self.users.append(user)
        print(f'Your account has been created successfully {name}')
    def check_user(self):
        for user in self.users:
            print(f'User Name : {user.name} and  Acount Number : {user.ac_num} ')
    
    def delete_user(self,ac_num):
        for user in self.users:
            if user.ac_num == ac_num :
                delete = user 
                break
        print(f'Acount of {user.name} has been deleted')
        self.users.remove(delete)

    def check_bal(self):
        print(f'Balance : {self.balance}')
    
    def loan_given(self):
        print(f'Total loan given :{self.loan_gave}')
    def loan_on(self):
        self.loan_op = True 
        print('Loan option Turned on successfully')
    def loan_off(self):
        print('loan option turned off successfully')
        self.loan_op = False

class USER:
    def __init__(self,name,email,address,types,ac_num) -> None:
        self.name = name 
        self.email = email 
        self.address = address
        self.types = types 
        self.ac_num = ac_num 
        self.balance = 0
        self.loan = 0
        self.num_of_loan = 0
        self.deposit = 0
        self.history = []

    def check_bal(self):
        print(f'Total Balance : {self.balance}')

    def deposit_am(self,amount):
        self.balance += amount
        nigro.balance += amount 
        self.deposit +=amount 
        print(f'{self.deposit} amount deposited successfully')

    
    def withdraw_am(self,amount):
        if self.balance < amount :
            print(f'Withdrawal amount exceeded') 
        else :
            if self.deposit > amount and amount > nigro.balance :
                print('U are Doomed! This Bank is Done For !') 
            elif amount <= self.deposit :
                self.balance -= amount  
                nigro.balance -= amount 
                print(f'Withdrawed {amount} Successfully')
            elif self.deposit < amount :
                print('Currently The loan cant be withdrawn')

    def take_loan(self,amount):
        if nigro.loan_op == False:
            print('you are not eligible for the loan')
        elif self.num_of_loan > 2:
            print('Sorry ! limit exceeded')
        else :
            if nigro.balance - (self.balance + amount)>=0:
                self.balance += amount 
                self.num_of_loan += 1
                nigro.loan_gave += amount 
                print(f'Loan amount {amount} is added to your account')
                self.history.append(f'loan taken : {amount}')
            else :
                print('You cant take such amount of loan at this moment')


    def transfer_am(self,amount,ac_num):
        flag = False 
        for user in nigro.users:
            if(user.ac_num == ac_num):
                other = user 
                flag = True
        if flag == True :
            if self.balance > amount :
                other.balance += amount 
                self.balance -= amount 
                self.deposit -= amount 
                self.history.append(f'transferred amount {amount} to {ac_num}') 
                other.history.append(f'Received  amount {amount} from {self.ac_num}')
                print(f'Transferred {amount} to {ac_num} successfully')
            else :
                print('Insufficient Balance')
        else :
            print('Account does not exist')
    
    def transection_history(self):
        for i,item  in enumerate(self.history):
            print(f'{i+1}.{item}') 



nigro = Bank_SYS()

#Replica 

while True:
    inpt = input("""
    Options :
    1.Admin 
    2.User
    3.Exit
""")
    if inpt == '3':
        break
    if inpt == '1':
        while True:
            ad_inpt = input("""
    Welcome Admin 
    Options :
    1.Create account 
    2.Delete account 
    3.See Account 
    4.Bank Balance 
    5.Loan Balance 
    6.Turn on Loan Feature 
    7.Turn off Loan Feature
    8. Exit
""")
            if ad_inpt == '1':
                name = input('Enter name : ')
                email = input('Enter Email : ')
                address = input('Enter address : ')
                types = input('Type : ')
                nigro.create_user(name,email,address,types)
            if ad_inpt == '2':
                ac_num = input('Enter account number :')
                ac_num = int(ac_num)
                nigro.delete_user(ac_num)
            if ad_inpt == '3':
                print('The Users : ')
                nigro.check_user()
            if ad_inpt == '4':
                nigro.check_bal()
            if ad_inpt == '5' :
                nigro.loan_given()
            if ad_inpt == '6':
                nigro.loan_on()
            if ad_inpt == '7':
                nigro.loan_off()
            if ad_inpt == '8':
                break
    if inpt == '2':
        while True:
            a_inpt = input('Enter account number : ')
            if a_inpt.isdigit() == False:
                break
            a_inpt = int(a_inpt)
            f = False
            for user in nigro.users:
                if a_inpt == user.ac_num :
                    f = True
                    c_ac = user
            if f == False :
                print('Invalid Account')
                break
            else :
                print(f'Welcome {c_ac.name}')
                while True:
                    u_inpt = input("""Options 
            
            1. Deposit
            2. Cash Withdraw
            3. Check Balance 
            4. Check Trans History
            5. Transfer
            6. Loan
            7. Exit                        
                                               
               """)
                    if u_inpt == '1':
                        amount = input('Enter amount to be deposited :')
                        amount = int(amount)
                        c_ac.deposit_am(amount)
                    if u_inpt == '2':
                        amount = input('Enter amount to be withdrawn :')
                        amount = int(amount)
                        c_ac.withdraw_am(amount)
                    if u_inpt == '3':
                        c_ac.check_bal()
                    if u_inpt == '4':
                        print('Transection history:')
                        c_ac.transection_history()
                    if u_inpt == '5':
                        ac_num = input('Enter account number to transfer money : ')
                        ac_num = int(ac_num)
                        amount = input('Enter amount: ')
                        amount = int(amount)
                        c_ac.transfer_am(amount,ac_num)
                    if u_inpt == '6':
                        amount = input('Enter amount:') 
                        amount = int(amount)
                        c_ac.take_loan(amount)
                    if u_inpt == '7':
                        break


