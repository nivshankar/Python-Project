print('Welcome to Student Data Organiser')
Students_Data={}
Subject_Unique={}
while True:
    print('\nSelect the option as per list number: ')
    print('1)Add Student: New Student Record')
    print('2)Display All Students: Displays all student record')
    print('3)Update Student Info. : One at a time')
    print('4)Delete Student')
    print('5)Display Subjects Offered')
    print('0) Exit the Student Data Organiser')
    choice=int(input('\nEnter Your choice: '))
    match choice:
        case 1:
            print('\nEnter Student Details :')
            Student_Id=int(input('Student Id: ')) 
            if Student_Id in Students_Data:
                print("\nStudent Id already exist")
            else:
                Name=input('Name: ')
                DOB=input("Date of Birth (DD-MM-YYYY): ")
                age=int(input("Age: "))
                Subject_String=input('Subjects separated by commas: ')
                Subjects=set(Subject_String.split(","))
                Unique_Information=(Student_Id,Name,DOB,age)
                Students_Data[Student_Id]={'Info':Unique_Information,'Subjects':Subjects}
                print('New Student Data Addition --> Successful')
        case 2:
            if not Students_Data:
                print("\nNo Student Data Found")
            else:
                print("\n","Displaying  all Students".center(70,"-"))
                for Sdata in Students_Data.values():
                    print(f"\nStudent Id -> {Sdata['Info'][0]}"
                          ,f"\nName -> {Sdata['Info'][1]}"
                          ,f"\nDate Of Birth -> {Sdata['Info'][2]}"
                          ,f"\nAge -> {Sdata['Info'][3]}\nSubjects: "
                          )
                    for sub in Sdata['Subjects']:
                        print(sub,end=",")
                    print()
        case 3:
            if not Students_Data:
                print('\nThere is no Student Data available. Firstly add a stuent data')
                continue
            Id=int(input("\nEnter Student Id to update student Details: "))
            found=False
            for StudId,info in Students_Data.items():
              if Id==StudId:
                  Id,current_name,DOB,current_age=info['Info']
                  current_subjects=info['Subjects']
                  found=True
                  print("Select from following to Update")
                  print("1)Name")
                  print("2)Subject")
                  print("3)Age")
                  update_choice=int(input('\nChoose what you want to update: '))
                  match update_choice:
                        case 1:
                            update_name=input("Enter name you want to update: ")
                            info['Info']=(Id,update_name,DOB,current_age)
                            print("\nName Update --> Successful")
                        case 2:
                           update_subject=input("Enter the updated subjects separated with commas: ")
                           info['Subjects'].update(set(update_subject.split(",")))
                           print("\nSubjects Update --> Successful")
                        case 3:
                            update_age=int(input("Enter your current age: "))
                            info['Info']=(Id,current_name,DOB,update_age)
                            print("\nAge Update --> Successful")
                        
                        case _:
                            print("\nEnter valid option to update.")
                  
            if found == False:
                    print("\nThe Id you entered is not in Student data list.")
                        
                        
        case 4:
            if not Students_Data:
                print('\nThere is no Student Data available. Firstly add a stuent data')
                continue
            Id=int(input('\nEnter Student Id to delete: '))
            if Id in Students_Data:
                Students_Data.pop(Id)
                print("\nStudent Data Deletion --> Successful")
            else:
                print("\nThe Id you entered is not in Student data list.")
        case 5:
            if not Students_Data:
                print("\nThere in no subject data avilable right now,firstly add some data.")
                continue
            Unique_Subjects=set()
            for Id,details in Students_Data.items():
                Unique_Subjects.update(details['Subjects'])
            print("\n","Current Available Subjects are".center(60,"-"),"\n")
            for sub in Unique_Subjects:
                print(sub,end=" | ")
            print()
        case 0:
            print('\nThanks for using the student Data Organiser')
            break
        case _:
            print("\nEnter valid Choice.")
    
            
