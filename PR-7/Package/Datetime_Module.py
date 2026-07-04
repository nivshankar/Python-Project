import datetime as dt
def Current_Datetime():
    print(f"\nCurrent Date and Time : {dt.datetime.now().strftime("\nDate : %d/%m/%Y\nTime : %H:%M:%S")}")

def Difference_Date():
    date1list=input('\nEnter the First Date (YYYY-MM-DD): ').strip().split("-")
    try:
        y1,m1,d1=map(int,date1list)
        date1=dt.date(y1,m1,d1)
    except ValueError as e:
        print(f"\nInvalid Date : {e}")
        return 
    date2list=input('Enter the Second Date (YYYY-MM-DD): ').strip().split("-")
    try:
        y2,m2,d2=map(int,date2list)
        date2=dt.date(y2,m2,d2)
    except ValueError as e:
        print(f"\nInvalid Date : {e}")
        return 
    difference=date1-date2
    if difference.days==0:
        print("\nBoth are same Dates.")
    else:
        print(f"\nThe difference between Date 1 and Date 2 is : {difference}")

def Custom_Formatdate():
    datelist=input('\nEnter the First Date (YYYY-MM-DD): ').strip().split("-")
    try:
        y,m,d=map(int,datelist)
        date=dt.date(y,m,d)
    except ValueError as e:
        print(f"\nInvalid Date : {e}")
        return 
    print("\nAvailable options for date format:")
    print("1. (DD/MM/YYYY)")
    print("2. (DD/MM/YY)")
    print("3. (MM-DD-YYYY)")
    print("4. (DD Month_Name YYYY)")
    print("5. (Day_Name , DD Month_Name YYYY)")
    print("6. (Day_Name , DD/MM/YY)")
    try:
        DFchoice=int(input("\nEnter your Choice: "))
    except ValueError:
        print("\nEnter valid Option from above as number only")
        return
    else:
        match DFchoice:
            case 1:
                print(f"{date.strftime("\n%d/%m/%Y")}")
            case 2:
                print(f"{date.strftime("\n%d/%m/%y")}")
            case 3:
                print(f"{date.strftime("\n%m/%d/%Y")}")
            case 4:
                print(f"{date.strftime("\n%d %B %Y")}")
            case 5:
                print(f"{date.strftime("\n%A , %d %B %Y")}")
            case 6:
                print(f"{date.strftime("\n%A , %d/%m/%y")}")
            case _:
                print("\nEnter valid option.")

def Stopwatch():
    import time as t 
    input("Press Enter to start the stopwatch...")
    start_time = t.time()
    print("Stopwatch started! Press Enter again to stop.")
    input()   
    end_time = t.time()

    stopwatch_display = end_time-start_time
    print(f"\nElapsed Time: {stopwatch_display:.2f} seconds")
    