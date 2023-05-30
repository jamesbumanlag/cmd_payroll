# this is the banner
def payroll_system_banner():
    print()
    print()
    print('----Payroll System----')
    print()

# postion to choose
def position():
   
    while True:
        
             
        # User position
        print(''' 
        Position: 
            1 : General Manager
            2 : Care Manager
            3 : Registered Nurse
            4 : Admin
            5 : Enrolled Nurse
            6 : AIN
            ''')
                
        emp_choice = input('    >>>  ')
        if emp_choice == '1':
            general_manager()
        elif emp_choice == '2':
            care_manager()
        elif emp_choice == '3':
            registered_nurse()
        elif emp_choice == '4':
            admin()
        elif emp_choice == '5':
            enrolled_nurse()
        elif emp_choice == '6':
            ain()
        elif emp_choice not in range (1,7):
            print('Input 1 - 6 only')

        print('--------------')    
        print('Try Again Y/N')  

        tryagain = input('>>> ').upper()

        if tryagain == 'N':
            print('Exiting...')
            break
        elif tryagain == 'Y':
            continue
        elif tryagain != 'Y' and tryagain != 'N':
            input('Invalid Input')
            continue   
    
    return(days_of_work,empNum,empName)
# calculation of general manager salary   
def general_manager():
    rate = 50
    role = 'General Manager'
    calculate_pay(rate,role)
   
# calculation of care manager salary
def care_manager():
    rate = 40
    role = 'Care Manager'
    calculate_pay(rate,role)

# calculation of RN salary
def registered_nurse():
    rate = 35
    role = 'Registered Nurse'
    calculate_pay(rate,role)

# calculation of admin salary
def admin():
    rate = 30
    role = 'Administration'
    calculate_pay(rate,role)

# calculation of EN Salary
def enrolled_nurse():
    rate = 30
    role = 'Enrolled Nurse'
    calculate_pay(rate,role)

# calculation of AIN salary
def ain():
    rate = 25
    role = 'Assistant in Nursing'
    calculate_pay(rate,role)
    
def calculate_pay (rate,role):
    total_pay = int(days_of_work * 8 * rate)
    print(f'Name: {empName}')
    print(f'Employee No. : {empNum}')
    print(f'Position: {role}')
    print(f'Rate: {rate}')
    print(f'Days of Work: {days_of_work}')
    print(f'Salary is {total_pay}')

#main program

payroll_system_banner()
empNum = input('Employee Number: ')
empName = input('Name: ')
days_of_work = int(input('Days of work: '))

position()
