def main():
    print("="*85)
    print("Welcome to Multi-Utility toolkit")
    while True:
        print("="*85)
        print("Choose An Option number".center(50))
        print("\n1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. generate Unique Identifiers (UUID)")
        print("5. File Operations")
        print("6. Explore Module Attributes (Directory)")
        print("7. Exit")
        print("="*85)
        try:
            choice=int(input("Enter your Choice: "))
            print("="*85)
        except ValueError:
            print("Enter valid Option from above as number only")
            continue
        else:
            match choice:
                case 1:
                    while True:
                        print("-"*85)
                        print("Date and Time Operations")
                        print("\n1. Display Current Date and time")
                        print("2. Difference Between Two Dates")
                        print("3. Format Date into custom format")
                        print("4. Stopwatch")
                        print("5. Back to Main Menu")
                        print("-"*85)
                        try:
                            Dchoice=int(input("Enter your Choice: "))
                        except ValueError:
                            print("Enter valid Option from above as number only")
                            continue
                        else:
                            from Package import Datetime_Module as DTM
                            match Dchoice:
                                case 1:
                                    DTM.Current_Datetime()
                                case 2:
                                    DTM.Difference_Date()
                                case 3:
                                    DTM.Custom_Formatdate()
                                case 4:
                                    DTM.Stopwatch()
                                case 5:
                                    print()
                                    print("Back to Main Menu".center(70))
                                    print("-"*85)
                                    break
                                case _:
                                    print("\nEnter valid choice.") 
                case 2:
                    while True:
                        print("-"*85)
                        print("\nMathematical Operations ")
                        print("1. Calculate Factorial")
                        print("2. Area of Circle ")
                        print("3. Trigonometric Calculations")
                        print("4. Back to Main Menu")
                        print("-"*85)
                        try:
                            mchoice = int(input("Enter Choice : "))
                        except ValueError:
                            print("\nEnter valid Option from above as number only")
                            continue
                        else:
                            from Package import Math_Module as MM
                            match mchoice:
                                case 1:
                                    MM.factorial_num()
                                case 2:
                                    MM.circle_area()
                                case 3:
                                    MM.trigono()
                                case 4:
                                    print()
                                    print("Back to Main Menu".center(70))
                                    print("-"*85)
                                    break
                                case _:
                                    print("\nEnter valid choice.") 
                case 3:
                  import random as r
                  while True:
                    print("-"*85)
                    print("Radom Data Generation")
                    print("\n1. Generate Random Number")
                    print("2. Generate Random List")
                    print("3. Create Random Pasword")
                    print("4. Generate Random OTP")
                    print("5. Back To main Menu")
                    print("-"*85)
                    try:
                        Rchoice=int(input("Enter your Choice: "))
                    except ValueError:
                        print("Enter valid Option from above as number only")
                        continue
                    else:
                        match Rchoice:
                            case 1:
                                num=r.randint(0,1000)
                                print(f"\nGenerated number is : {num}")
                            case 2:
                                rlist=[]
                                lsize=r.randint(3,10)
                                for _ in range(lsize):
                                    ele=r.randint(0,100)
                                    rlist.append(ele)
                                print(f"\nGenerated List is: {rlist}")
                            case 3:
                                upchar="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                lowchar="abcdefghijklmnopqrstuvwxyz"
                                num="0123456789"
                                spchar="`~!@#$%^&*()_+-=[]{}|;:',.<>/?"
                                totchar=upchar+lowchar+num+spchar
                                password=""
                                try:
                                    passlen=int(input("\nEnter password length: "))
                                except ValueError:
                                        print("Enter valid password length")
                                        continue
                                else:
                                    if passlen<4:
                                        print("\nPassword length less than 4 is not safe.")
                                    elif passlen>16:
                                        print("\nPassword length greater than 16 is way more lengthy password")
                                    else:
                                        ranchoice=[1,2,3,4]
                                        r.shuffle(ranchoice)
                                        for i in ranchoice:
                                            if i==1:
                                                password+=r.choice(upchar)
                                            elif i==2:
                                                password+=r.choice(lowchar)
                                            elif i==3:
                                                password+=r.choice(num)
                                            elif i==4:
                                                password+=r.choice(spchar)
                                        if passlen>4:
                                            for _ in range(passlen-4):
                                                password+=r.choice(totchar)

                                        print(f"\nPassword generated : {password}")
                            case 4:
                                otplen=r.randint(4,7)
                                if otplen==4:
                                    otp=r.randint(1000,9999)
                                elif otplen==5:
                                    otp=r.randint(10000,99999)
                                elif otplen==6:
                                    otp=r.randint(100000,999999)
                                elif otplen==7:
                                    otp=r.randint(1000000,9999999)
                                print(f"\nOTP Generated : {otp}")
                            case 5:
                                print()
                                print("Back to Main Menu".center(70))
                                print("-"*85)
                                break
                            case _:
                                print("\nEnter valid choice.") 
                case 4:
                    from uuid import uuid4 as u4
                    print("\n","Welcome to Random Id Generator Program".center(70,"-"))
                    Id=u4()
                    print(f"\nGenerated ID is : {Id}\n")
                case 5:
                  from Package import File_Module as FM
                  while True:
                    print("-"*85)
                    print("\nChoose An File Operation number")
                    print("\n1. Create a new File")
                    print("2. Write to a file")
                    print("3. Read From a file")
                    print("4. Append to a File")
                    print("5. Back To main Menu")
                    try:
                        print("-"*85)
                        filechoice=int(input("Enter your Choice: "))
                    except ValueError:
                        print("\nEnter valid Option from above as number only")
                        continue
                    else:
                        match filechoice:
                            case 1:
                                file=input("\nEnter file name: ").strip()
                                FM.Create_File(file)
                            case 2:
                                file=input("\nEnter file name: ").strip()
                                FM.Write_File(file)
                            case 3:
                                file=input("\nEnter file name: ").strip()
                                FM.Read_File(file)
                            case 4:
                                file=input("\nEnter file name: ").strip()
                                FM.Append_File(file)
                            case 5:
                                print()
                                print("Back to Main Menu".center(70))
                                print("-"*85)
                                break  
                            case _ :
                                print("\nEnter valid choice.")  
                case 6:
                    from importlib import import_module as impmod
                    module_name=input("Enter module name to explore: ").strip()
                    try:
                        module=impmod(module_name)
                        print("\nAvailable attributes are :")
                        print("-"*85)
                        for i in dir(module):
                            print(i)
                        print()
                    except ModuleNotFoundError:
                        print(f"\nError : No module named {module_name} exist")
                case 7:
                    print("="*85)
                    print("Thank You for using the  Multi-Utility toolkit")
                    print("="*85)
                    break
                case _ :
                    print("\nEnter valid option.\n")
if __name__=='__main__':
    main()