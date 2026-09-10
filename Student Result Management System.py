'''
# 🐍 Student Result Management System

### Command-Line Based Python Project

*Aim:*
To develop a menu-driven *Student Result Management System* using Python that accepts student details and marks,
calculates total, percentage, grade, and pass/fail status using functions, and stores all student records in an *Excel file*.

'''
import pandas as pd
import os

StudentRecord = 'C:/Users/Vedant/OneDrive/Desktop/StudentRecord.xlsx'


def Menu():
    print('1. Add Name & Marks')
    print('2. Get Student Result')
    print('3. View All Results')
    print('4. Exit')

    ch=int(input('Enter Your Choice: '))

    if ch==1:
        get_Marks()
    elif ch==2:
        find()
    elif ch==3:
        St_Record()
    elif ch==4:
        print('Thank You')
    else:
        print('\n!!!Invalid Choice!!!\n')
        Menu()


def get_Marks():
    nm = input('Enter Student Name: ')
    cl = input('Enter Your Class as (F.Y/S.Y/T.Y/Branch): ')
    rl = int(input('Enter Your Roll No: '))
    mt = int(input('Enter Your Marks of Maths: '))
    sci = int(input('Enter Your Marks of Science: '))
    mrthi = int(input('Enter Your Marks of Marathi: '))
    eng = int(input('Enter Your Marks of English: '))
    comp = int(input('Enter Your Marks of Computer: '))
    tmarks=mt+sci+mrthi+eng+comp
    per = (tmarks/500)*100
    per1 = f"{per:.2f}%"
    #for grade
    if per>=90.00:
        grd='A'
    elif per>=75.00:
        grd='B'
    elif per>=60.00:
        grd='C'
    elif per>=50.00:
        grd='D'
    elif per>=40:
        grd='E'
    else:
        grd='F'

    #for Status
    if grd=='F':
        sts='Fail'
    else:
        sts='Pass'
        

    #create Dictionary
    data ={
        'Roll no':[rl],
        'Name':[nm],
        'Class': [cl],
        'Total': [tmarks],
        'Percentage':[per1],
        'Grade': [grd],
        'Status':[sts]
        }
    df = pd.DataFrame(data)

    #Append data if file exists
    if os.path.exists(StudentRecord):
        old_df = pd.read_excel(StudentRecord)
        df=pd.concat([old_df,df],ignore_index=True)

    df.to_excel(StudentRecord, index=False)

    

    print('\nStudent Result is Stored!!!\n')
    
    Menu()
    
def St_Record():
    if os.path.exists(StudentRecord):
        df=pd.read_excel(StudentRecord)
        print('\n======All Records=======\n')
        print(df)
        print('\n')
    else:
        print('\n    Student Record is Empty\n')
    Menu()

def find():
    if os.path.exists(StudentRecord):
        df=pd.read_excel(StudentRecord)
        

        Roll_No=int(input('Enter Your Roll No: '))
        Student=df[df['Roll no']==Roll_No]
    
        print('\n======Student Result=======\n')
        print(Student)
        print('\n')
    else:
        print('\n     Student Result not Exists\n')
    Menu()
Menu()    
