import datetime
import os

def drawmenu():

    def choose_menu(n = str()):
        if n == '1':
            os.system('cls')
            Option_1()
        if n == '2':
            os.system('cls')
            Option_2()
        if n == '3':
            os.system('cls')
            Option_3()
        if n == '4':
            os.system('cls')
            Option_4()
        if n == '5':
            os.system('cls')
            Option_5()
        if n == '6':
            os.system('cls')
            Option_6()
        if n == '7':
            Quit()

    os.system('cls')
    s = '''
        ----------------------------------------------
    *********************Smart School**********************
        ----------------------------------------------

        Welcome to this application! <Made by Ky :)>
        Let's start!


    =========================MENU==========================
                                                          
        1. Calendar
        2. Calculating the salary
        3. Sorting the list of salaries (Ascending)
        4. Employee information
        5. Calculating average mark of student
        6. Searching student's information
        7. Exit program

    =======================================================
    '''
    print(s)
    n = input('Enter the number corresponding to the function: ')
    while True:
        if n in ['1', '2', '3', '4', '5', '6', '7']:
            break
        print('Error!')
    choose_menu(n)
    
# 1. Calendar
def Option_1():

    def day_of_month(yyyy = int(),mm = int()):
        def leap_year(yyyy = int()):
            if (yyyy % 400 == 0) or (yyyy % 4 ==0 and yyyy % 100 != 0):
                return True
            else:
                return False
        if mm == 2 :
            if leap_year(yyyy):
                return 29
            else :
                return 28
        elif mm in [1,3,5,7,8,10,12]:
            return 31
        return 30

    def date_now():
        t = datetime.datetime.now()
        print('Time  ' + t.strftime('%I : %M %p'))
        print('Date  ' + t.strftime('%A, %B %d %G'))

    def choose_op1(n = str()):
        if n == '1':
            yyyy = int(input('Enter the year: '))
            while True:
                mm = int(input('Enter the month: '))
                if mm <0 or mm >12 :
                    print('Error!')
                else :
                    break
            t = datetime.date(yyyy,mm,1)
            print(t.strftime('%B has'),day_of_month(yyyy,mm),'days')
        else:
            date_now()

    def display1():
        s='''
        =======================================================

        1. Seeing day of month
        2. Seeing datetime now

        =======================================================
        '''
        print(s)
       
        n =input('What do you want to see? (1 or 2) : ')
        while True: 
            if n == '1' or n == '2':
                break
            print('Error!')
        choose_op1(n)
    while True:
        display1()
        n = input('Do you want to continue? (Press "e" to back the Home Page or any key to continue this function): ')
        if n == 'e':
            drawmenu()
            break
        os.system('cls')

# 2. Calculate the salary 
def Option_2():
    def cal_salary(s = float(), h = float()): #s is salary/hour and h is hours
        if h <= 40:
            return s*h
        else :
            return s*40 + 1.5*s*(h-40)
    def choose_2(n = str()):
        global f
        if n == '1':
            while True: 
                n = standard_name(input("Employee's name: "))
                if not is_not_words(n):
                    break
                print('Error!')
            f.write('Name: %s\n' %n)
            while True:
                s = input('Enter the salary per hour ($): ')
                if is_float(s):
                    s = float(s)
                    break
                print('Error!')
            f.write('    Salary/hour : %6.2f ($)\n' %s)
            while True:
                h = input('Enter the hours per month (h): ')
                if is_float(h):
                    h = float(h)
                    break
                print('Error!')
            f.write('    Hour/month  : %6.2f (h)\n' %h)
            print('The salary per month is %.2f' %cal_salary(s, h),'($)\n')
            f.write('    Salary/month: %6.2f ($)\n' %(cal_salary(s, h)))
            n = input("Do you want to calculate another's salary? "+'(Press "e" to exit calculating or any key else to continue): ')
            os.system('cls')
            if n != 'e':
                #os.system('cls')
                choose_2('1')
            #else:
                #os.system('cls')
        else:
            f = open(txt,'r')
            print(f.read())
            f.close()
            n = input('Press any key to exit! ')

    def display2(): 
        s = '''
        =======================================================
        
        
        1. Calculating the salary
        2. Seeing salary of each employees


        
        =======================================================
        '''
        print(s)    
        n = input('Your choice is ? (1 or 2): ')
        while True:
            if n == '1' or n == '2':
                os.system('cls')
                choose_2(n)
                break
            print('Error!')
        
        
    txt = 'data/salary.txt'
    reload(txt)
    while True:
        display2()
        n = input('Do you want to continue the function 2? (Press "e" to back the Home Page or any key else to continue): ')
        if n == 'e':
            f.close()
            break
        os.system('cls')
    drawmenu()
    
# 3. Sort list (Quicksort)
def Option_3():
    
    def enterlist():
        while True:
            n = input('Enter number of employees: ')
            if n.isdigit():
                n = int(n)
                break
            print('Error!')
        for i in range(n):
            while True:
                n = standard_name(input("Employee's name %d : " %(i+1)))
                if not(is_not_words(n)):
                    names.append(n)
                    break
                print('Error!')
            while True:
                n = input("The %s's salary ($): " %names[i])
                if is_float(n):
                    salary.append(float(n))
                    break
                print('Error!')
    def qsort(left = int(), right = int()):
        i = left
        j = right
        k = salary[(right +left-1)//2]
        while True:
            while salary[i] < k :
                i += 1
            while salary[j] > k :
                    j -= 1
            if i <= j :
                salary[i], salary[j] = salary[j], salary[i]
                names[i], names[j] = names[j], names[i]
                i +=1
                j -=1
            if i > j :
                    break
        if j > left :
            qsort(left,j)
        if i < right:
            qsort(i, right)
    s = '''                EMPLOYEE'S SALARIES                   \n\n|  STT  |           Name            |       Salary      |\n|       |                           |                   |'''
    while True:        
        names = list()
        salary = list()
        enterlist()
        qsort(0,len(salary)-1)
        os.system('cls')
        print(s)
        for i in range(len(salary)):
            print('| {:_^5} | {:_<25} | {:_>13} ($) |'.format(i+1, names[i], group_digits(str(salary[i]))))
        print()
        n = input('Do you want to continue? (Press "e" to back the Home Page or any key else to continue this function): ')
        if n == 'e':
            break
        os.system('cls')
    drawmenu()
    
# 4. Employee information 
def Option_4():

    def handle_name(st = str()):
        n=''
        names = standard_name(st).split()
        print('Name: ',names[-1])
        for i in names[:-1]:
            n += i + ' '
        print('Surname: ', n)
        print('Full name: ',standard_name(st))
    
    def choose_4(n = int()):
        global f
        if n == 1:
            txt = 'data/employees.txt'
            reload(txt)
            while True:
                name = standard_name(input("Enter employee's name: "))
                if not is_not_words(name):
                    break
                print('Error!')
            while True:
                department = input("Enter %s's department: " %name)
                if not is_not_words(department):
                    break
                print('Error!')
            while True:
                position = input("Enter %s's position: " %name)
                if not is_not_words(position):
                    break
                print('Error!')
            
            f.write('%s __Position: %s __Department: %s \n' %(standard_name(name),department,position))
            handle_name(name)
        else:
            f = open('data/employees.txt','r')
            print(f.read())
            f.close()
            input('Press any key to exit! ')
            os.system('cls')
            drawmenu()

    def display4():
        s = '''
        =======================================================


        1. Standardize the name
        2. See the list of employee


        =======================================================
        '''
        print(s)
        while True:
            n = input('Your choice is ? (1 or 2): ')
            if n == '1' or n == '2':
                n = int(n)
                os.system('cls')
                choose_4(n)
                break
            print('Error!')

    while True:
        display4()
        n = input('Press "e" to back the Home Page or any key else to continue with another: ')
        if n == 'e':
            f.close()
            break
    drawmenu()

# 5. Calculate average mark of student
def Option_5():

    def sumlist(list):
        s = 0
        for i in list:
            s += i
        return s

    def average_mark(mark = list(),weight = list()):
        sum_mark = 0
        for i in range(len(mark)): #len(mark) == len(weight)
            sum_mark += mark[i] * weight[i]
        return sum_mark/sumlist(weight)

    def enterdata():
        subjects = list()
        mark = list()
        weight = list()
       
        while True:
            st_name = standard_name(input('Student name: '))
            if not is_not_words(st_name) :
                f.write('Name: %s\n' %st_name)
                break
            print('Error!')
             
        i = 0
        while True:
            while True:
                n = input('Enter subject %d: ' %(i+1)).title()
                if not is_not_words(n):
                    subjects.append(n)
                    break
                print('Error!')
                    
            while True:
                n = input('Enter mark of the subject %d: ' %(i+1))
                if is_float(n) and (0 <= float(n) <= 10):
                    mark.append(float(n))
                    break
                print('Error!')
            while True:
                n = input("Enter the mark's weight above: ")
                if is_float(n) and( float(n) in [1,1.5,2,2.5,3]):
                    weight.append(float(n))
                    break
                print('Error!')
            f.write('   %s : %.1f (weight: %.1f)\n' %(subjects[i], mark[i], weight[i]))
            i += 1
            n = input("Press 'e' to exit entering subject information or any key else to continue entering data: ")
            if n == 'e':
                break
        f.write('   Overall mark: %.1f' %average_mark(mark, weight))
        f.write('\n')
            
    txt = 'data/average_mark.txt'
    reload(txt)
    while True:
        enterdata()
        e = input("Enter another student's data? (Press 'e' to back the Home Page or any key else to continue): ")
        if e == 'e':
            os.system('cls')
            f.close()
            f2 = open(txt,'r')
            print(f2.read())
            input('Enter any key to continue! ')
            f2.close()
            break
    drawmenu()

# 6. Searching student's 
def Option_6():
    txt = 'data/student.txt'
    def enterdata():
        global f
        while True:
            while True:
                name = standard_name(input("Student's name: "))
                if not is_not_words(name):
                    break
                print('Error!')
            class_st = input("%s's class: " %name).upper()
            while True:
                mark = input("%s's overall mark: " %name)
                if is_float(mark):
                    mark = float(mark)
                    break
                print('Error!')
            f.write('%s %s %.1f\n' %(name, class_st, mark))
            n = input("Do you want to enter another student's data? "+'(Press "e" to exit entering or any key else to continue): ')
            if n == 'e':
                os.system('cls')
                f.close()
                f = open(txt,'r')
                print(f.read())
                input('Completed Update!\nPress any key to continue! ')
                os.system('cls')
                break
        display6()

    def inputdata(txt = str()):
        f = open(txt,'r')
        student = list(f)
        for i in range(len(student)):
            info = student[i].split()
            name = ' '.join(info[:len(info)-2]).title()
            student[i] = (name,info[-2],float(info[-1]))
        f.close()
        return student

    def findname(name = str(),student = list()):
        results = list()
        j = 1
        for i in range(len(student)):
            if name in student[i][0]:
                results.append(student[i])
                print('%d. %s __ Class: %5s __ Overall mark: %.1f' %((j),student[i][0],student[i][-2],student[i][-1]))
                j += 1
        input('Press any key to continue!')
        os.system('cls')
        drawmenu()
    
    def choose_6(n = str()):
        if n == '1':
            reload(txt)
            enterdata()
        else:
            name = standard_name(input("Enter student's name: "))
            findname(name, inputdata(txt))


    def display6():
        s = '''
        =======================================================


        1. Entering students data
        2. Searching student's information


        =======================================================
        '''
        print(s)
        while True:
            n = input('Your choice is ? (1 or 2): ')
            if n in ['1', '2']:
                os.system('cls')
                break
            print('Error!')
        choose_6(n)

    display6()

# 7. Exit application
def Quit():
    print('Quit application!')
    exit()

# Other functions
def is_float(a = str()):
    try :
        float(a)
        return True
    except ValueError:
        return False

def is_not_words(s = str()):
    if s == '' or s.isspace():
        return True
    for i in s.split():
        if not i.isalnum():
            return True
    if any(i.isdigit() for i in s) :
        return True
    return False

def standard_name(st = str()):
    st = st.strip().title()
    while st.find('  ') != -1:
        st = st.replace('  ',' ')
    return st

def group_digits(s = str()):
    st = [s[s.find('.'):]]
    i = -(len(s)-s.find('.')+1)
    while i > -len(s):
        st.append(s[i-3 : i])
        i -= 3
    st.reverse()
    return ','.join(st[:-1])+st[-1]

def reload(txt = str()): # Reload data from .txt file
    global f
    n = input('Do you want to reload data? (Press "y" to reload data or any key else to continue with old data ):  ')
    if n == 'y':
        f = open(txt,'w')
    else:
        f = open(txt,'a')

#begin

drawmenu()
    
    
    


