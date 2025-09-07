
def login():
    max_attempts = 3
    login_attempts = 0

    while max_attempts > login_attempts:
        username = input('Enter username: ')
        password = input('Enter password: ')

        with open('database.txt', 'r') as file:
            lines = file.readlines()
            file.close()

        for line in lines:
            stored_user_type, stored_username, stored_password = line.strip().split(':')
            
            if username == stored_username and password == stored_password:
                print(f'\nLogin successful! Welcome, {stored_user_type} {stored_username}.')
                if stored_user_type == 'admin':
                    menu_admin(username)
    
                elif stored_user_type == 'trainer':
                    menu_trainer(username)
                    
                elif stored_user_type == 'lecturer':
                    menu_lecturer(username)

                elif stored_user_type == 'student':
                    menu_student(username)

                return
            
        login_attempts += 1

        if login_attempts < max_attempts:
            print(f'\nLogin failed. Please check your username and password. Attempt {login_attempts} of {max_attempts}.\n')
        else:
            print('\nAccount locked. Too many failed login attempts. Please contact an admin.')
        #     return

def logout():
    print('You have successfully logged out.')
    login()
              
def menu_admin(username): #menu admin
    
    option = input('''
Operations:
1. Register trainer
2. Delete trainer
3. Register lecturer
4. Delete lecturer                   
5. Assign trainer to respective level
6. View monthly income
7. View trainer feedback
8. Update profile
9. Logout
Select a number: ''')
    
    if option == '1':
        register_trainer()
        print('\nWhat else would you like to do today?')
        menu_admin(username)
            
    elif option == '2':
        delete_trainer()
        print('\nWhat else would you like to do today?')
        menu_admin(username)

    elif option == '3':
        register_lecturer()
        print('\nWhat else would you like to do today?')
        menu_admin(username)
    
    elif option == '4':
        delete_lecturer()
        print('\nWhat else would you like to do today?')
        menu_admin(username)

    elif option == '5':
        assign_levelmodule()
        print('\nWhat else would you like to do today?')
        menu_admin(username)

    elif option == '6':
        view_income(username)
        print('\nWhat else would you like to do today?')
        menu_admin(username)
    
    elif option == '7':
        feedback(username)
        print('\nWhat else would you like to do today?')
        menu_admin(username)

    elif option == '8':
        update_profile(username)
        print('\nWhat else would you like to do today?')
        menu_admin(username)

    elif option == '9':
        logout()
    
    else:
        print('Please enter a valid number')
        menu_admin(username)

def register_trainer(): 
    user_type = 'trainer' #ask for user input
    username = input('Trainer username: ')
    password = input('Trainer password: ')
    
    with open('database.txt','r') as file: #open file read by line and makes a list
        lines = file.readlines()
        
        
    for line in lines:
        stored_user_type, stored_username, stored_password = line.strip().split(':') 
        #split ':' in database.txt & removes any whitespace
        #assigns elements from split(':') e.g. if line = trainer:trainer1:asdasd stored_user_type = trainer, stored_username = trainer1 stored_password = asdasd
        if username == stored_username:
            print(f'\nError: Username "{username}" already exists. Please choose a different username.') #checks if username exists, if exist ask again.
            user_type = 'trainer'
            username = input('Trainer username: ')
            password = input('Trainer password: ')

    with open('database.txt', 'a') as file: #append new trainer to database.txt for login
        file.write(f'{user_type}:{username}:{password}\n')

    with open('profile.txt','a') as file: #append new trainer to profile.txt for update profile func
        file.write(f'{username}:name:jobtitle:email:contact\n')
                
    print(f'\n{user_type} {username} registered successfully.')

def delete_trainer():
    with open('database.txt','r') as file:
        lines = file.readlines()
    
    username = input('Enter username of trainer you would like to delete: ')

    user_exist = False # A flag to see if user exist now set as false

    with open('database.txt','w') as file: #remove trainer from database.txt for login
        
        for line in lines:
            stored_user_type, stored_username, stored_password = line.strip().split(':')
            if username == stored_username and stored_user_type == 'trainer':
                line.rstrip()
                user_exist = True # sets flag to true when username input matches stored username
            else:
                file.write(line)
    
    with open ('trainer_module.txt','r') as file: #remove trainer from trainer_module.txt
        lines = file.readlines()
            
    with open('trainer_module.txt','w') as file:
        for line in lines:
            stored_user_type, stored_username, stored_level, stored_modules = line.strip().split(':')
            if username == stored_username and stored_user_type == 'trainer':
                line.rstrip()
                user_exist = True # sets flag to true when username input matches stored username
            
            else:
                file.write(line)

    with open('profile.txt','r') as file: 
        lines = file.readlines()

    with open('profile.txt','w') as file: #remove trainer from profile.txt
        for line in lines:
            stored_username, stored_name, stored_jobtitle, stored_email, stored_contact = line.strip().split(':')
            if username == stored_username and stored_user_type == 'trainer':
                line.rstrip()
                user_exist = True # user exist set to true as username input same as store_username in database
            
            else:
                file.write(line)
    
    with open('class_info.txt','r') as file:
        lines = file.readlines()

    with open('class_info.txt','w') as file: #remove trainer from class_info.txt
        for line in lines:
            stored_username, stored_level, stored_module, stored_fee, stored_schedule, stored_students = line.strip().split(':')
            if username == stored_username:
                line.rstrip()
                user_exist = True # user exist set to true as username input same as store_username in database
            
            else:
                file.write(line)
    
    with open('module_status.txt','r') as file:
        lines = file.readlines()
    
    with open('module_status.txt','w') as file:
        for line in lines:
            stored_username, stored_studentusername, stored_level, stored_module, module_status = line.strip().split(':') 
            if username == stored_username:
                line.strip()
                user_exist = True
            else:
                file.write(line)

    if user_exist: #when user_exist is true username deleted
            print(f'Trainer {username} has been deleted.')
        
    else:
        print(f'This trainer does not exist.')
        delete_trainer()

def register_lecturer(): 
    user_type = 'lecturer' #ask for user input
    username = input('Lecturer username: ')
    password = input('Lecturer password: ')
    
    with open('database.txt','r') as file: #open file read by line and makes a list
        lines = file.readlines()
        
        
    for line in lines:
        stored_user_type, stored_username, stored_password = line.strip().split(':') 
        if username == stored_username:
            print(f'\nError: Username "{username}" already exists. Please choose a different username.') #checks if username exists, if exist ask again.
            user_type = 'lecturer'
            username = input('Lecturer username: ')
            password = input('Lecturer password: ')

    with open('database.txt', 'a') as file: #append new trainer to database.txt for login
        file.write(f'{user_type}:{username}:{password}\n')

    with open('profile.txt','a') as file: #append new trainer to profile.txt for update profile func
        file.write(f'{username}:name:jobtitle:email:contact\n')
                
    print(f'\n{user_type} {username} registered successfully.')        

def delete_lecturer():
    with open('database.txt','r') as file:
        lines = file.readlines()
        
    
    username = input('Enter username of trainer you would like to delete: ')

    user_exist = False # A flag to see if user exist now set as false

    with open('database.txt','w') as file: #remove trainer from database.txt for login
        
        for line in lines:
            stored_user_type, stored_username, stored_password = line.strip().split(':')
            
            if username == stored_username and stored_user_type == 'lecturer':
                line.rstrip()
                user_exist = True # sets flag to true when username input matches stored username
            else:
                file.write(line)

    with open('profile.txt','r') as file: 
        lines = file.readlines()

    with open('profile.txt','w') as file: #remove lecturer from profile.txt
        for line in lines:
            stored_username, stored_name, stored_jobtitle, stored_email, stored_contact = line.strip().split(':')
             
            if username == stored_username:
                line.rstrip()
                user_exist = True # user exist set to true as username input same as store_username in database
            
            else:
                file.write(line)

    if user_exist: #when user_exist is true username deleted
        print(f'Lecturer {username} has been deleted.')
    
    else:
        print(f'This lecturer does not exist.')
        delete_lecturer()

def view_income(username):
    trainer_name = input('Enter trainer name: ')
    available_module_pairs = set()  # Use set to store unique module and level pairs
    available_trainers = set()

    with open('class_info.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        stored_trainer_username, stored_level, stored_module, stored_fee, stored_schedule, stored_students = line.strip().split(':')
        available_trainers.add(stored_trainer_username)
        if trainer_name == stored_trainer_username:
            available_module_pairs.add((stored_level, stored_module))  # Add unique module and level pairs

    if trainer_name not in available_trainers:
        print(f'Trainer does not exist.')
        return menu_admin(username)

    print(f'Available modules and levels for {trainer_name}:')
    for num, (level, module) in enumerate(available_module_pairs, 1):  # Enumerate available module pairs
        print(f"{num}. {level}: {module}")

    while True: #enter loop
        try:
            option = int(input("Enter the number of the module you want to see income for: "))
            if 1 <= option <= len(available_module_pairs):
                selected_level, selected_module = list(available_module_pairs)[option - 1] #convert set to list for indexing. [option - 1] to adjust index as python start from 0
                break  # Exit loop if option is valid
            else:
                print('Enter a valid number')
        except ValueError:
            print('Enter a valid number.')

    paid_students = []
    for line in lines:
        stored_trainer_username, stored_level, stored_module, stored_fee, stored_schedule, stored_students = line.strip().split(':')
        if trainer_name == stored_trainer_username and selected_level == stored_level and selected_module == stored_module and stored_students is not None:
            fee = stored_fee
            if stored_students != '' and stored_students != 'students/notpaid':
                for student_info in stored_students.strip().split(','):
                    student_name, payment_status = student_info.strip().split('/')
                    if payment_status == 'paid':
                        paid_students.append(student_name)                
            else:
                fee = ''
    try:
        if fee is not None:
            income = float(fee) * len(paid_students)
            print(f'Number of paid students: {len(paid_students)}')
            print(f'Total Monthly income: ${income}')
    except ValueError:
        print('Trainer has not generated any income')

def assign_levelmodule():
    username = input('Enter username of trainer: ')

    trainer_exist = False
    
    with open('database.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            stored_user_type, stored_username, stored_password = line.strip().split(':')
            if username == stored_username and stored_user_type == 'trainer':
                trainer_exist = True
                
    if trainer_exist:
        option = input('''
What level are they teaching? 
1. Beginner
2. Intermediate
3. Advanced
Enter a number: ''')

        # Map the option to the corresponding level
        level_map = {'1': 'Beginner', '2': 'Intermediate', '3': 'Advance'}
        level = level_map.get(option)
        if not level:
            print('Enter a valid number.')
            return

        available_modules = ['Python', 'Java', 'SQL', 'C#', 'C++']
        print(f'Available modules: {available_modules}')

        module_input = input('Enter module: ').strip()

        if module_input not in available_modules:
            print('Invalid module. Please select from the available options.')
            return

        # Check if the trainer already teaches the selected module at the specified level
        trainer_teaches = False
        with open('trainer_module.txt', 'r') as file:
            for line in file:
                stored_user_type, stored_username, stored_level, stored_module = line.strip().split(':')
                if username == stored_username and level == stored_level and module_input == stored_module:
                    trainer_teaches = True
        
        if trainer_teaches:
            print(f'{username} already teaches {level},{module_input}.')
        else:                                                                                                              
            with open('trainer_module.txt', 'a') as file:  
                    updated_modules = f'trainer:{username}:{level}:{module_input}\n'
                    file.write(updated_modules)

            with open('class_info.txt', 'a') as file: # Append to 'class_info.txt' only if the trainer exists
                    file.write(f'{username}:{level}:{module_input}:fee:schedule:students/notpaid\n')

            print(f'Trainer {username} has been assigned to teach {level} {module_input}.')
    else:
        print(f'Trainer {username} does not exist.')

def feedback(username):
    with open('feedback.txt','r') as file:
        lines = file.readlines()

    option = input('''
Operations
1. View feedback
2. Delete feedback
3. Back to menu
Enter number: ''')
    
    if option == '1':
        for line in lines:
            stored_trainer_username, stored_feedback_message = line.strip().split(':')
            print(f'{stored_trainer_username}: {stored_feedback_message}')
        feedback(username)

    elif option == '2':
        trainer_exist = False
        trainer_username = input('Enter trainer username: ')
        with open ('feedback.txt','w') as file:
            for line in lines:
                stored_trainer_username, stored_feedback_message = line.strip().split(':')
                
                if trainer_username == stored_trainer_username:
                    line.rstrip()
                    trainer_exist = True
                
                else:
                    file.write(line)
        
        if trainer_exist:
            print(f'Feedback of {trainer_username} has been deleted.')
            
        else:
            print('Trainer does not exist.')
            
    elif option == '3':
        menu_admin(username)
    
    else:
        print('Enter a valid number.')
        feedback(username)

def menu_trainer(username): #username entered will identify which trainer it is
    
    option = input('''
Operations:
1. Update class info
2. View students
3. Send feedback to admin
4. Update profile
5. Logout
Select a number: ''')
    if option == '1':
        update_classinfo(username)
        print('\nWhat else would you like to do today?')
        menu_trainer(username)

    elif option == '2':
        view_student(username)
        print('\nWhat else would you like to do today?')
        menu_trainer(username)

    elif option == '3':
        send_feedback(username)
        print('\nWhat else would you like to do today?')
        menu_trainer(username)

    elif option == '4':
        update_profile(username)
        print('\nWhat else would you like to do today?')
        menu_trainer(username)
    
    elif option == '5':
        logout()
    
    else:
        print('Enter a valid number')
        menu_trainer(username)

def update_classinfo(username):
    available_modules = []

    with open('trainer_module.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            stored_usertype, stored_username, stored_level, stored_modules = line.strip().split(':')
            if username == stored_username:
                available_modules.append((stored_level,stored_modules))
    
    for num, (level, module) in enumerate(available_modules,1):
        print(f'{num}| Level: {level} | Module: {module}')

    while True: #enter loop
        try:
            option = int(input("Enter the number of the module you want to update: "))
            if 1 <= option <= len(available_modules):
                selected_level, selected_module = list(available_modules)[option - 1] #convert set to list for indexing. [option - 1] to adjust index as python start from 0
                break  
            else:
                print('Enter a valid number')
        except ValueError:
            print('Enter a valid number.')
    while True:

        with open('class_info.txt','r') as file:
            lines2 = file.readlines()
            for line in lines2:
                stored_username, stored_level, stored_module, stored_fee, stored_schedule, student_num = line.strip().split(':')
                if username == stored_username and selected_module == stored_module and selected_level == stored_level:
                    print(f'''
Name: {stored_username}
Level: {stored_level}
Module: {stored_module}
Fee: {stored_fee}
Schedule: {stored_schedule}''')
        
        
            option = input('''
Operations
1. Class fee
2. Class schedule
3. Exit
Select a number: ''')
            with open('class_info.txt','r') as file:
                lines = file.readlines()

        if option == '1':
            with open('class_info.txt', 'w') as file:
                for line in lines:
                    stored_username, stored_level, stored_module, stored_fee, stored_schedule, student_num = line.strip().split(':')
                    if username == stored_username and selected_module == stored_module and selected_level == stored_level:
                        new_fee = input('Enter new fee: ')
                        updated_classfee = f'{stored_username}:{stored_level}:{stored_module}:{new_fee}:{stored_schedule}:{student_num}\n'
                        file.write(updated_classfee)
                        print(f'Class fee has been updated from [{stored_fee}] to [{new_fee}]')
                    else:
                        file.write(line)
        
        elif option == '2':
            with open('class_info.txt', 'w') as file:
                for line in lines:
                    stored_username, stored_level, stored_module, stored_fee, stored_schedule, student_num = line.strip().split(':')
                    if username == stored_username and selected_module == stored_module and selected_level == stored_level:
                        class_day = input('Enter day: ')
                        class_time = input('Enter time: ')
                        new_schedule = f'{class_day},{class_time}'
                        updated_classfee = f'{stored_username}:{stored_level}:{stored_module}:{stored_fee}:{new_schedule}:{student_num}\n'
                        file.write(updated_classfee)
                        print(f'Class schedule has been updated from [{stored_schedule}] to [{new_schedule}]')
                    else:
                        file.write(line)

        elif option == '3':
            menu_trainer(username)
            break
        else:
            print('Enter a valid number.')
            update_classinfo(username)    

def view_student(username):
    available_module_pairs = set()

    with open('class_info.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        stored_trainer_username, stored_level, stored_module, stored_fee, stored_schedule, stored_students = line.strip().split(':')
        if username == stored_trainer_username:
            available_module_pairs.add((stored_level, stored_module))

    print('Your available modules:')
    for num, (level, module) in enumerate(available_module_pairs, 1):  # Enumerate available module pairs
        print(f"{num}. {level}: {module}")

    while True: 
        try:
            option = int(input("Enter the number of the module you want to see income for: "))
            if 1 <= option <= len(available_module_pairs):
                selected_level, selected_module = list(available_module_pairs)[option - 1] #convert set to list for indexing. [option - 1] to adjust index as python start from 0
                break 
            else:
                print('Enter a valid number')
        except ValueError:
            print('Enter a valid number.')

    paid_students = []
    notpaid_students = []

    for line in lines:
        stored_trainer_username, stored_level, stored_module, stored_fee, stored_schedule, stored_students = line.strip().split(':')
        if username == stored_trainer_username and selected_level == stored_level and selected_module == stored_module:
            for student_info in stored_students.strip().split(','):
                if stored_students != 'students/notpaid' and stored_students != '':
                    student_name, payment_status = student_info.strip().split('/')
                    if payment_status == 'paid':
                        paid_students.append(student_name)
                    else:
                        notpaid_students.append(student_name)

    if len(notpaid_students) == 0 and len(paid_students) == 0:
        print('No students are enrolled in this class.')
    else:
        print(f'''Paid Students: {paid_students}
Not Paid Students: {notpaid_students}''')

def send_feedback(username): #current trainer as parameter so the func knows which trainer it is
    feedback = input('Enter message: ')

    with open('feedback.txt','a') as file:
        file.write(f'{username}:{feedback}\n')

def menu_lecturer(username):
        
    option = input('''
Operations:
Kindly choose one of the options below :-
1. Register student
2. Update student details
3. Enroll student to module
4. Unenroll students from their module.
5. Approval requests
6. Update profile
7. Logout
Select a number: ''')
    
    if option == '1':
        register_student()
        print('\nWhat else would you like to do today?')
        menu_lecturer(username)
    
    elif option == '2':
        update_student()
        print('\nWhat else would you like to do today?')
        menu_lecturer(username)

    elif option == '3':
        enroll_student()
        print('\nWhat else would you like to do today?')
        menu_lecturer(username)

    elif option == '4':
        unenroll_student()
        print('\nWhat else would you like to do today?')
        menu_lecturer(username)
    
    elif option == '5':
        approval(username)
        print('\nWhat else would you like to do today?')
        menu_lecturer(username)

    elif option == '6':
        update_profile(username)
        print('\nWhat else would you like to do today?')
        menu_lecturer(username)

    elif option == '7':
        logout()
    
    else:
        print('Please enter a valid number')
        menu_lecturer(username)

def register_student():
    student_name = input("Enter student's name: ")
    student_name = student_name.capitalize()
    student_username = input('Enter student\'s username: ')
    student_pw = input('Enter student password: ')
    
    with open('student_info.txt') as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_studentname, stored_tpnum, stored_email, stored_contact, stored_moe, stored_modulepair = line.strip().split(':') 
            if student_username == stored_username:
                print(f'\nError: Username "{student_username}" already exists. Please choose a different username.') #checks if username exists, if exists asks again.
                return register_student()
            
    
    with open('database.txt','a') as file: #adds username and password to database.txt for login
        file.write(f'student:{student_username}:{student_pw}\n') 
    
    tp_num = input('Enter student\'s TP number: ')
    email = input('Enter student\'s email: ')
    contact = input('Enter student\'s contact number: ')
    moe = input('Enter month of enrollment: ')

    
    with open('student_info.txt','a') as file:      #format of the txt file in which the data is going to be stored
        file.write(f'{student_username}:{student_name}:{tp_num}:{email}:{contact}:{moe}:modulepair\n')      #module pair consists of module and level
    
    with open('profile.txt','a') as file: #appends new trainer to profile.txt for update profile func
        file.write(f'{student_username}:{student_name}:status:course:year\n')
    
    print(f'Student {student_name} has been registered.')

def update_student():                   #change details of the student
    student_username = input('Enter student username: ')
    student_exist = False                                   #a flag  to see if the student exists in the records

    with open('student_info.txt','r') as file:              #reads every line to finds the fed student_username
        lines = file.readlines()
        for line in lines:
            stored_username, stored_studentname, stored_tpnum, stored_email, stored_contact, stored_moe, stored_modulepair = line.strip().split(':')
            if student_username == stored_username:
                student_exist = True
        
    while student_exist:        
        update_what = int(input('''
1. Name
2. TP Number
3. Email
4. Month of enrollment
5. Back to Menu
Enter a number: '''))
        
        if update_what == 1:
            with open('student_info.txt','r') as file:
                lines = file.readlines()
                updated_lines = []              #basically forms a temporary txt file as the lines are going to be fed in this
                name_updated = False
                for line in lines:
                    stored_username, stored_studentname, stored_tpnum, stored_email, stored_contact, stored_moe, stored_modulepair = line.strip().split(':')
                    if student_username == stored_username:
                        updated_name = input('Enter new name: ')
                        updated_line = f'{stored_username}:{updated_name}:{stored_tpnum}:{stored_email}:{stored_contact}:{stored_moe}:{stored_modulepair}\n'
                        updated_lines.append(updated_line)
                        print(f'Student name has been updated from {stored_studentname} to {updated_name}')
                    else:
                        updated_lines.append(line)          #if name does not match, it will append the original line which it was iterating to the above temp txt file

            print(f'''
Your current details are now the following
Name: {updated_name}
Student TP Number: {stored_tpnum}
Email: {stored_email}
Contact: {stored_contact}
Month of enrollment: {stored_moe}''')
                    
            with open('student_info.txt','w') as file:
                file.writelines(updated_lines)                  #writes the temp txt file back into the original file
            

        elif update_what == 2:
            with open('student_info.txt', 'r') as file:
                lines = file.readlines()
                updated_lines = []
                
                for line in lines:
                    stored_username, stored_studentname, stored_tpnum, stored_email, stored_contact, stored_moe, stored_modulepair = line.strip().split(':')
                    if student_username == stored_username:
                        updated_tpnum = input('Enter new student ID: ')
                        updated_line = f'{stored_username}:{stored_studentname}:{updated_tpnum}:{stored_email}:{stored_contact}:{stored_moe}:{stored_modulepair}\n'
                        updated_lines.append(updated_line)
                        print(f'Student {stored_studentname} TP Number has been updated to: {updated_tpnum}')
                        
                    else: 
                        updated_lines.append(line)

            print(f'''
Your current details are now the following
Name: {stored_studentname}
Student TP Number: {updated_tpnum}
Email: {stored_email}
Contact: {stored_contact}
Month of enrollment: {stored_moe}''')
                    
            with open('student_info.txt', 'w') as file:
                file.writelines(updated_lines)

        elif update_what == 3:
            with open('student_info.txt', 'r') as file:
                lines = file.readlines()
                updated_lines = []
                
                for line in lines:
                    stored_username, stored_studentname, stored_tpnum, stored_email, stored_contact, stored_moe, stored_modulepair = line.strip().split(':')
                    if student_username == stored_username:
                        updated_email = input('Enter new student email: ')
                        updated_line = f'{stored_username}:{stored_studentname}:{stored_tpnum}:{updated_email}:{stored_contact}:{stored_moe}:{stored_modulepair}\n'
                        updated_lines.append(updated_line)
                        print(f'Student {stored_studentname} Email has been updated from {stored_email} to {stored_email}')
                        
                    else: 
                        updated_lines.append(line)
 
            print(f'''
Your current details are now the following
Name: {stored_studentname}
Student TP Number: {stored_tpnum}
Email: {updated_email}
Contact: {stored_contact}
Month of enrollment: {stored_moe}''')
                    
            with open('student_info.txt', 'w') as file:
                file.writelines(updated_lines)
            
        elif update_what == 4:
            with open('student_info.txt', 'r') as file:
                lines = file.readlines()
                updated_lines = []
                
                for line in lines:
                    stored_username, stored_studentname, stored_tpnum, stored_email, stored_contact, stored_moe, stored_modulepair = line.strip().split(':')
                    if student_username == stored_username:
                        updated_moe = input('Enter new student month of enrollment: ')
                        updated_line = f'{stored_username}:{stored_studentname}:{stored_tpnum}:{stored_email}:{stored_contact}:{updated_moe}:{stored_modulepair}\n'
                        updated_lines.append(updated_line)
                        print(f'Student {stored_studentname} month of enrollment has been updated from {stored_moe} to {updated_moe}')
                        
                    else: 
                        updated_lines.append(line)
    
            print(f'''
Your current details are now the following
Name: {stored_studentname}
Student TP Number: {stored_tpnum}
Email: {stored_email}
Contact: {stored_contact}
Month of enrollment: {updated_moe}''')
                    
            with open('student_info.txt', 'w') as file:
                file.writelines(updated_lines)
                    
        elif update_what == 5:
            print('Exiting.')
            break
        
        else:
            print('Enter a valid number')
            
    
    else:
        print('Student username does not exist.')

def enroll_student():
    student_username = input('Enter student username: ')
    student_exist = False                                       #turns true if the student is found and then enables a particular set of instructions that will be performed after
    
    with open('student_info.txt','r') as file:                  #reads from student_info.txt to check if student exists.
        lines = file.readlines()
        for line in lines:
            stored_username, stored_studentname, stored_tpnum, stored_email, stored_contact, stored_moe, stored_modulepairs= line.strip().split(':')
            if student_username == stored_username:
                student_exist = True
    
    if student_exist:                                           #asks for module and level
        available_modules = ['Python','Java','SQL','C#','C++']
        available_module_levels = ['Beginner','Intermediate','Advance']
        module_name = input(f'Enter module name {available_modules}: ')
        
        module_level = input(f'Enter module level {available_module_levels} : ')
        module_level = module_level.capitalize()

        available_trainers = []                                 #initializing an empty list

        if module_name not in available_modules or module_level not in available_module_levels:     #basic english, works like an OR gate
            print('Enter valid module name or module level.') 
            return enroll_student()
            
        with open('class_info.txt','r') as file: #checks for available trainers that match the level and module inputs and appends them to the empty list
            lines = file.readlines()
            for line in lines:
                stored_trainer_username, stored_level, stored_module, stored_fee, stored_schedule, stored_students = line.strip().split(':')
                if module_level == stored_level and module_name == stored_module:
                    available_trainers.append(stored_trainer_username)

                    #choose trainer
                    chosen_trainer = input(f'''
Available Trainers for {stored_level} {stored_module}:{available_trainers}
Select a trainer: ''')

        student_enrolled = False

        if len(available_trainers) == 0:
            print('No trainers available for this module currently. Please contact an admin.')

        elif chosen_trainer in available_trainers:
            with open('class_info.txt','r') as file:                #checks if student is already enrolled in chosen course
                lines = file.readlines()
                for line in lines:
                    stored_trainer_username, stored_level, stored_module, stored_fee, stored_schedule, stored_students = line.strip().split(':')
                    existing_students = stored_students.strip().split(',')
                    if any(student.split('/')[0] == student_username for student in existing_students) and module_name == stored_module:
                            student_enrolled = True
                            break
            
            if not student_enrolled:
                with open('class_info.txt','w') as file:
                    for line in lines:
                        stored_trainer_username, stored_level, stored_module, stored_fee, stored_schedule, stored_students = line.strip().split(':')
                        if chosen_trainer == stored_trainer_username and module_level == stored_level and module_name == stored_module: 
                            stored_students = stored_students.replace('students/notpaid','') # removes default value 'students/notpaid' if it is present as strings are immutable
                            updated_students = f'{stored_students},{student_username}' if stored_students else student_username # Append the new student to the existing list of students
                            update_classinfo = f'{stored_trainer_username}:{stored_level}:{stored_module}:{stored_fee}:{stored_schedule}:{updated_students}/notpaid\n' 
                            file.write(update_classinfo)
                        else:
                            file.write(line)

                updated_modulepair = [] 

                with open('student_info.txt','r') as file:
                    lines = file.readlines()

                with open('student_info.txt','w') as file:
                    for line in lines:
                        stored_username, stored_studentname, stored_tpnum, stored_email, stored_contact, stored_moe, stored_modulepairs= line.strip().split(':')
                        updated_students = []
                        if student_username == stored_username:
                            existing_modulepair = stored_modulepairs.strip().split(';')
                            if 'modulepair' in existing_modulepair or '' in existing_modulepair: # removes default value 'modulepair' from student_info.txt when student is newly registered 
                                updated_modulepair = []
                            else:
                                updated_modulepair = existing_modulepair # if not default value use existing modules from stored_modulepairs

                            new_modulepair = f'{module_level},{module_name}' 
                            updated_modulepair.append(new_modulepair) # add new_modulepair to existing modulepairs 
                            updated_modulepair_str = ';'.join(updated_modulepair)
                            updated_student_info = f'{stored_username}:{stored_studentname}:{stored_tpnum}:{stored_email}:{stored_contact}:{stored_moe}:{updated_modulepair_str}\n'
                            file.write(updated_student_info)
                        else:
                            file.write(line)

                with open('module_status.txt','a') as file: 
                    file.write(f'{chosen_trainer}:{student_username}:{module_level}:{module_name}:notcompleted\n')
                
                print(f'Student {student_username} enrolled in {chosen_trainer} {module_level} {module_name} class.')
    
            else:
                print(f'Student {student_username} is already enrolled in this module')
            
    else:
        print(f'Student {student_username} does not exist.')         

def approval(username):
    student_modules = []

    option = input(f'''
1. View requests
2. Answer approval requests
3. Back to home menu
Enter a number: ''')
    
    if option == '1':
        with open('viewapprovalrequests.txt') as file:
            lines = file.readlines()
            for line in lines:
                stored_studentusername, stored_level, stored_module, approval_status = line.strip().split(':')
                student_modules.append((stored_studentusername, stored_level,stored_module,approval_status))
        
        for num, (stored_studentusername, level, module, status) in enumerate(student_modules,1):                   #iterates over student module retreiving index number and each student's request
            print(f'{num}| Username: {stored_studentusername} | Level: {level} | Module: {module} | Approval status: {status}')
        
        approval(username)

    elif option == '2':
        stud_id = input('Enter student username: ')
        student_exist = False

        with open('viewapprovalrequests.txt') as file:
            lines = file.readlines()
            for line in lines:
                stored_studentusername, stored_level, stored_module, approval_status = line.strip().split(':')
                if stud_id == stored_studentusername:
                    student_modules.append((stored_level,stored_module,approval_status))
                    student_exist = True

        if student_exist:       
            for num, (level, module, status) in enumerate(student_modules,1):
                print(f'{num}| Level: {level} | Module: {module} | Approval status: {status}')

            while True:
                try:
                    option = int(input("Enter the number of student request you want to approve: "))
                    if 1 <= option <= len(student_modules):
                        selected_level, selected_module, selected_status = student_modules[option -1]
                        break
                    else:
                        print('Enter a valid number.')
                except ValueError:
                    print('Enter a valid number')
            if selected_status == 'approved' or selected_status == 'rejected':
                student_pending = False
            else: 
                while True:
                    try:
                        option2 = int(input('''
Operations:
1. Approve
2. Reject
3. Exit
Select a number: '''))
                        if option2 == 1:
                            choice = '1'
                            break
                        elif option2 == 2:
                            choice = '2'
                            break
                        elif option2 == 3:
                            choice = '3'
                            break
                        else:
                            print('Enter a valid number.')
                    except ValueError:
                        print('Enter a valid number')
                
                if choice == '1':
                    with open('viewapprovalrequests.txt', 'w') as file:
                        for line in lines:
                            stored_studentusername, stored_level, stored_module, approval_status = line.strip().split(':')
                            if stud_id == stored_studentusername and selected_level == stored_level and selected_module == stored_module and approval_status == 'pending':            
                                respond = 'approved'
                                file.write(f'{stored_studentusername}:{stored_level}:{stored_module}:{respond}\n')
                                student_pending = True
                            else:
                                file.write(line)
                            
                elif choice == '2':
                    with open('viewapprovalrequests.txt', 'w') as file:
                        for line in lines:
                            stored_studentusername, stored_level, stored_module, approval_status = line.strip().split(':')
                            if stud_id == stored_studentusername and selected_level == stored_level and selected_module == stored_module and approval_status == 'pending':                        
                                respond = 'rejected'
                                file.write(f'{stored_studentusername}:{stored_level}:{stored_module}:{respond}\n')
                                student_pending = True
                            else:
                                file.write(line)

                elif choice == '3':
                    return(approval(username))

            if not student_pending:
                    print(f'Student request has already been {selected_status}.')
                
            else:
                print(f'Request of student {stud_id} for {selected_level} {selected_module} has been {respond}.')
        
        else:
            print('Student does not exist.')

    elif option == '3':
        menu_lecturer(username)

    else:
        print('Invalid value entered, enter digits assigned to menus.')

def unenroll_student(): 
    student_name = input('Enter student name: ')
    student_username = input('Enter student username: ')
    student_exist = False

    with open('student_info.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_studentname, stored_tpnum, stored_email, stored_contact, stored_moe, stored_modulepairs = line.strip().split(':')
            if student_username == stored_username and student_name == stored_studentname:
                student_exist = True
    
    available_modulepairs = set()
    module_status = False

    if student_exist:
        with open('module_status.txt','r') as file: 
            lines = file.readlines()
            for line in lines:
                stored_trainer, stored_username, stored_level, stored_module, stored_module_status = line.strip().split(':')
                if student_username == stored_username:
                    available_modulepairs.add((stored_level, stored_module, stored_module_status))

        for num, (level, module, status) in enumerate(available_modulepairs, 1):
            print(f'{num}| Module: {level},{module} | Status: {status}')

        while True:
            try:
                option = int(input("Enter the number of student's module you would like to delete: "))
                if 1 <= option <= len(available_modulepairs):
                    level, module, status = list(available_modulepairs)[option -1]
                    break
                else:
                    print('Enter a valid number.')
            except ValueError:
                print('Enter a valid number')

        if status == 'completed':
            module_status = True

        elif status == 'notcompleted':
            while True:
                choice = input(f'Student {student_name} has not completed this module. Do you still wish to remove them from {level},{module}? (Y/N): ')
                choice = choice.capitalize()
                if choice == 'Y':
                    module_status = True
                    break
                elif choice == 'N':
                    module_status = False
                    break
                else:
                    print('Please enter a valid choice.')
                                    
        if module_status:

            with open('module_status.txt','r') as file:
                lines = file.readlines()

            with open('module_status.txt','w') as file:
                for line in lines:
                    stored_trainer, stored_username, stored_level, stored_module, stored_module_status = line.strip().split(':')
                    if student_username == stored_username and level == stored_level and module == stored_module:
                        line.rstrip()
                    else:
                        file.write(line)

            with open('class_info.txt','r') as file:
                lines = file.readlines()
            
            with open('class_info.txt','w') as file:
                for line in lines:
                    stored_trainer_username, stored_level, stored_module, stored_fee, stored_schedule, stored_students = line.strip().split(':')
                    existing_students = stored_students.strip().split(',')

                    updated_students = []

                    for student_info in existing_students:
                        if student_info != '' and student_info != 'students/notpaid':
                            username, payment_status = student_info.strip().split('/')
                            if username == student_username and level == stored_level and module == stored_module:
                                   continue
                            else:
                                updated_students.append(student_info)
                    
                    updated_student_str = ','.join(updated_students)
                    updated_line = f'{stored_trainer_username}:{stored_level}:{stored_module}:{stored_fee}:{stored_schedule}:{updated_student_str}\n'

                    file.write(updated_line)

            with open('student_info.txt','r') as file:
                lines = file.readlines()

            with open('student_info.txt','w') as file:
                for line in lines:
                    stored_username, stored_studentname, stored_tpnum, stored_email, stored_contact, stored_moe, stored_modulepairs = line.strip().split(':')
                    existing_modulepairs = stored_modulepairs.strip().split(';')
        
                    updated_studentpair = []
                    if student_name == stored_studentname and student_username == stored_username:
                        for modulepairs in existing_modulepairs:
                            stored_level, stored_module = modulepairs.strip().split(',')
                            if level == stored_level and module == stored_module:
                                continue
                            else:
                                updated_studentpair.append(modulepairs)
                                
                        updated_modulepair_str = ';'.join(updated_studentpair)
                        updated_student_info  = f'{stored_username}:{stored_studentname}:{stored_tpnum}:{stored_email}:{stored_contact}:{stored_moe}:{updated_modulepair_str}\n'
                        file.write(updated_student_info)
                    else:
                        file.write(line)

            
            print(f'Student {student_name} has been removed from {level},{module} class.')

        else:
            print(f'No changes have been made to student {student_name}.')

    else:
        print('Student does not exist.')

def menu_student(username):
    option = input('''
Operations:
1. View schedule
2. View, delete or send request
3. View Invoice
4. Update profile
5. Logout
Select a number: ''')
    
    if option == '1':
        view_schedule(username)
        print('\nWhat else would you like to do today?')
        menu_student(username)

    elif option == '2':
        request(username)
        print('\nWhat else would you like to do today?')
        menu_student(username)

    elif option == '3':
        view_invoice(username)
        print('\nWhat else would you like to do today?')
        menu_student(username)
    
    elif option == '4':
        update_profile(username)
        print('\nWhat else would you like to do today?')
        menu_student(username)

    elif option == '5':
        logout()

    else:
        print('Please enter a valid option.')
        menu_student(username)

def request(username):
    option = input('''
Operations
1. View sent request
2. Send request
3. Delete pending request
Enter a number: ''')
    
    if option == '1':
        view_request(username)
        menu_student(username)

    elif option == '2':
        send_request(username)
        menu_student(username)
    
    elif option == '3':
        delete_request(username)
        menu_student(username)
    else:
        print('Enter a valid option.')
        return request(username)

def view_request(username):
    available_modules = []

    with open('viewapprovalrequests.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            student_username, stored_level, stored_module, approval_status = line.strip().split(':')
            if username == student_username:
                available_modules.append((stored_level,stored_module,approval_status))

    for num, (level, module, status) in enumerate(available_modules,1):
        print(f'{num}| Level: {level} | Module: {module} | Approval status: {status}')

def send_request(username):
    student_username = username
    available_modules = ['Python','Java','SQL','C#','C++']
    available_levels = ['Beginner','Intermediate','Advance']

    while True:
        new_module = input(f'Select a module {available_modules}: ')
        new_level = input(f'Select a level {available_levels}: ')
        if new_module in available_modules and new_level in available_levels:
            break
        else:
            print('Enter a valid module or level.')

    student_enrolled = False

    with open('student_info.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            stored_studentusername, stored_studentname, stored_tpnum, stored_email, stored_contact, stored_moe, stored_modulepairs = line.strip().split(':')
            existing_modulepairs = stored_modulepairs.strip().split(';')
            for modulepairs in existing_modulepairs:
                if modulepairs != '':
                    stored_level, stored_module = modulepairs.strip().split(',')
                    if username == stored_studentusername and new_level == stored_level and new_module == stored_module:
                        student_enrolled = True

    if student_enrolled:
        print('You are already enrolled in this module.')

    else:
        with open('viewapprovalrequests.txt','a') as file:
            file.write(f'{username}:{new_level}:{new_module}:pending\n')
            print(f'You have sent a request to enrolled in {new_level} {new_module}.')

def delete_request(username):
    available_modules = []

    with open('viewapprovalrequests.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            student_username, stored_level, stored_module, approval_status = line.strip().split(':')
            if username == student_username:
                available_modules.append((stored_level,stored_module,approval_status))
    for num, (level, module, status) in enumerate(available_modules,1):
        print(f'{num}| Level: {level} | Module: {module} | Approval status: {status}')

    while True:
        try:
            option = int(input('Enter number of request you wish to delete: '))
            if 1 <= option <= len(available_modules):
                selected_level, selected_module, selected_status = available_modules[option -1]
                break
            else:
                print('Enter a valid number.')
        except ValueError:
            print('Enter a valid number')

    request_deleted = False

    with open('viewapprovalrequests.txt','w') as file:
        for line in lines:
            student_username, stored_level, stored_module, approval_status = line.strip().split(':')
            if username == student_username and selected_level == stored_level and selected_module == stored_module and selected_status == 'pending':
                line.rstrip()
                request_deleted = True
            else:
                file.write(line)
    
    if request_deleted:
        print(f'Request to enroll in {selected_level} {selected_module} has been deleted.')
    else:
        print('Request could not be deleted as it has been approved or rejected.')

def view_schedule(username):
    with open('student_info.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_studentname, stored_tpnum, stored_email, stored_contact, stored_moe, stored_modulepairs = line.strip().split(':')
            if username == stored_username:
                student_username = stored_username
                if len(stored_modulepairs) == 0 or stored_modulepairs == 'modulepair':  # Check if stored_modulepairs is empty
                    print('You are not enrolled in any modules.')
                    return 
    
    available_modulepairs = []

    with open('class_info.txt','r') as file:
        lines = file.readlines()
    
        for line in lines:
            stored_trainer, stored_level, stored_module, stored_fee, stored_schedule, stored_students = line.strip().split(':')
            existing_students = stored_students.strip().split(',')
            if stored_students != '' and stored_students != 'students/notpaid':
                for students in existing_students:
                    username, payment_status = students.strip().split('/')
                    if student_username == username:
                        modulepair = (stored_level,stored_module) #adds tuple to modulepair list
                        available_modulepairs.append(modulepair)

    for num, modulepair in enumerate(available_modulepairs, 1):
        level, module = modulepair  # Unpack the tuple in list
        print(f'''{num}| Level: {level} | Module: {module}''')
    
    while True:
        try:
            option = int(input("Enter the number of module's schedule you would like to view: "))
            if 1 <= option <= len(available_modulepairs):
                selected_level, selected_module = list(available_modulepairs)[option -1]
                break
            else:
                print('Enter a valid number.')
        except ValueError:
            print('Enter a valid number')
    

    with open('class_info.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            stored_trainer, stored_level, stored_module, stored_fee, stored_schedule, stored_students = line.strip().split(':')
            if stored_level == selected_level and stored_module == selected_module:
                print(f'''
Module | Schedule
{selected_level},{selected_module} | {stored_schedule}''')

def view_invoice(username):  
    available_modulepairs = set()

    with open('class_info.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            stored_trainer, stored_level, stored_module, stored_fee, stored_schedule, stored_students = line.strip().split(':')
            existing_students = stored_students.strip().split(',')
            if stored_students != '' and stored_students != 'students/notpaid':
                for students in existing_students:
                    student_username, payment_status = students.strip().split('/')
                    if student_username == username:
                        modulepair = (stored_level,stored_module,stored_fee,payment_status) #adds tuple to modulepair list
                        available_modulepairs.add(modulepair)
    
    for num, (level, module, fee, payment_status) in enumerate(available_modulepairs, 1):  # Enumerate available module pairs
        print(f'{num}| Level: {level} | Module: {module} | Fee: {fee} | Payment Status: {payment_status}')
    
    choice = input('\nWould like you to make payment? (Y/N): ')
    choice = choice.capitalize()
    if choice == 'Y':

        while True: 
            try:
                option = int(input("\nEnter the number of the module you want to pay: "))
                if 1 <= option <= len(available_modulepairs):
                    selected_level, selected_module, selected_fee, selected_payment_status = list(available_modulepairs)[option - 1] #convert set to list for indexing. [option - 1] to adjust index as python start from 0
                    break  # Exit loop if option is valid
                else:
                    print('Enter a valid number')
            except ValueError:
                print('Enter a valid number.')
    
    
        if selected_payment_status == 'notpaid':
            updated_lines = [] 

            for line in lines:
                stored_trainer, stored_level, stored_module, stored_fee, stored_schedule, stored_students = line.strip().split(':')
                existing_students = stored_students.strip().split(',')
                updated_students_status = []

                if selected_level == stored_level and selected_module == stored_module == stored_fee == 'fee':
                    print('Trainer has not set a fee for this module.')
                    return

                else:
                    for student_info in existing_students:
                        if student_info != '':
                            student_username, payment_status = student_info.strip().split('/')
                            if selected_level == stored_level and selected_module == stored_module and student_username == username:
                                payment_status = 'paid'
                            updated_students_status.append(f'{student_username}/{payment_status}')

                    updated_students_status = ','.join(updated_students_status)
                    updated_line = f'{stored_trainer}:{stored_level}:{stored_module}:{stored_fee}:{stored_schedule}:{updated_students_status}\n'
                    updated_lines.append(updated_line)

            with open('class_info.txt', 'w') as file:
                for updated_line in updated_lines:
                    file.write(updated_line)
            
            print(f'You have made payment for {selected_level} {selected_module}.')
        
        else:
            print('You have already paid for this module.')
    
    elif choice == 'N':
        print('No payment made.')

    else:
        print('Enter a valid option.')
  
def update_profile(username):
    is_student = False

    with open('database.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            stored_user_type, stored_username, stored_password = line.strip().split(':')
            if stored_user_type == 'student' and username == stored_username:
                is_student = True

    while is_student == False:
        with open('profile.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                stored_username, stored_name, stored_jobtitle, stored_email, stored_contact = line.strip().split(':')
                if username == stored_username:
                    print(f'''
Profile
Name: {stored_name}
Title: {stored_jobtitle}
Email: {stored_email}
Contact: {stored_contact}''')
                    break
                    
        option = input('''
Operations
1. Name
2. Title
3. Email
4. Contact
5. Exit
Enter a number: ''')
          
        if option == '1':
            with open('profile.txt','w') as file:
                for line in lines:
                    stored_username, stored_name, stored_jobtitle, stored_email, stored_contact = line.strip().split(':')
                    if username == stored_username:
                        new_name = input('Enter name: ')
                        updated_profile = f'{stored_username}:{new_name}:{stored_jobtitle}:{stored_email}:{stored_contact}\n'
                        print(f"Name has been updated to '{new_name}'.")
                        file.write(updated_profile)
                        
                    else:
                        file.write(line)

        elif option == '2':
            with open('profile.txt','w') as file:
                for line in lines:
                    stored_username, stored_name, stored_jobtitle, stored_email, stored_contact = line.strip().split(':')
                    if username == stored_username:
                        new_jobtitle = input('Enter job title: ')
                        updated_profile = f'{stored_username}:{stored_name}:{new_jobtitle}:{stored_email}:{stored_contact}\n'
                        print(f"Job title has been updated to '{new_jobtitle}'.")
                        file.write(updated_profile)
                    
                    else:
                        file.write(line)

        elif option == '3':
            with open('profile.txt','w') as file:
                for line in lines:
                    stored_username, stored_name, stored_jobtitle, stored_email, stored_contact = line.strip().split(':')
                    if username == stored_username:
                        new_email = input('Enter email: ')
                        updated_profile = f'{stored_username}:{stored_name}:{stored_jobtitle}:{new_email}:{stored_contact}\n'
                        print(f"Email has been updated to '{new_email}'.")
                        file.write(updated_profile)
                        
                    else:
                        file.write(line)

        elif option == '4':
            with open('profile.txt','w') as file:
                for line in lines:
                    stored_username, stored_name, stored_jobtitle, stored_email, stored_contact = line.strip().split(':')
                    if username == stored_username:
                        new_contact = input('Enter phone number: ')
                        updated_profile = f'{stored_username}:{stored_name}:{stored_jobtitle}:{stored_email}:{new_contact}\n'
                        print(f"Contact has been updated to '{new_contact}'.")
                        file.write(updated_profile)
                        
                    else:
                        file.write(line)
        elif option == '5':
            print("Exiting profile update.")
            break

    while is_student == True:
        with open('student_info.txt','r') as file:
            lines2 = file.readlines()        
            for line in lines2:
                stored_username, stored_studentname, stored_tpnum, stored_email, stored_contact, stored_moe, stored_modulepair = line.strip().split(':')
                if username == stored_username:
                    print(f'''
Name: {stored_studentname}
TP Number: {stored_tpnum}
Email: {stored_email}
Contact: {stored_contact}
Month of enrollment: {stored_moe}''')
                    break
       
        with open('profile.txt','r') as file:
            lines1 = file.readlines()
            for line in lines1:
                stored_username, stored_name, stored_status, stored_course, stored_year = line.strip().split(':')
                if username == stored_username:
                    print(f'''Status: {stored_status}
Course: {stored_course}
Contact: {stored_year}''')
                    break
                    
        option = input('''
Operations
1. Status
2. Course
3. Intake
4. Contact
5. Exit
Enter a number: ''')
          
        if option == '1':
            with open('profile.txt','w') as file:
                for line in lines1:
                    stored_username, stored_name, stored_status, stored_course, stored_year = line.strip().split(':')
                    if username == stored_username:
                        new_status = input('Enter current status (available,away,do not disturb): ')
                        updated_profile = f'{stored_username}:{stored_name}:{new_status}:{stored_course}:{stored_year}\n'
                        print(f"Status has been updated to '{new_status}'.")
                        file.write(updated_profile)
                    
                    else:
                        file.write(line)

        elif option == '2':
            with open('profile.txt','w') as file:
                for line in lines1:
                    stored_username, stored_name, stored_status, stored_course, stored_year = line.strip().split(':')
                    if username == stored_username:
                        new_course = input('Enter enrolled course: ')
                        updated_profile = f'{stored_username}:{stored_name}:{stored_status}:{new_course}:{stored_year}\n'
                        print(f"Course has been updated to '{new_course}'.")
                        file.write(updated_profile)
                        
                    else:
                        file.write(line)

        elif option == '3':
            with open('profile.txt','w') as file:
                for line in lines1:
                    stored_username, stored_name, stored_status, stored_course, stored_year = line.strip().split(':')
                    if username == stored_username:
                        new_year = input('Enter Intake (Month,Year): ')
                        updated_profile = f'{stored_username}:{stored_name}:{stored_status}:{stored_course}:{new_year}\n'
                        print(f"Intake has been updated to '{new_year}'.")
                        file.write(updated_profile)
                        
                    else:
                        file.write(line)

        elif option == '4':
            with open('student_info.txt','w') as file:
                for line in lines2:
                    stored_username, stored_studentname, stored_tpnum, stored_email, stored_contact, stored_moe, stored_modulepair = line.strip().split(':')
                    if username == stored_username:
                        new_contact = input('Enter new contact information: ')
                        updated_profile = f'{stored_username}:{stored_studentname}:{stored_tpnum}:{stored_email}:{new_contact}:{stored_moe}:{stored_modulepair}\n'
                        print(f"Contact has been updated to '{new_contact}'.")
                        file.write(updated_profile)
                        
                    else:
                        file.write(line)
        elif option == '5':
            print("Exiting profile update.")
            break

        else:
            print('Enter a valid number.')

login()