print("\n\tWelcome to the Pattern Genartor and Number Analyzer")
while True:
    print("\nSelect an option as a number: ")
    print("1.For Pattern Generation")
    print("2.For Number Analyzer")
    print("3.For exit")
    choice=int(input('\nEnter your choice : '))
    match choice:
        case 1:
            print("\nCurrently we have Right angled Triangle pattern available")
            row=int(input('Enter number of rows : '))
            if row>=2 and row<=15:
                for i in range(1,row+1):
                    for _ in range(row,i,-1):
                        print(" ",end=" ")
                    for _ in range(1,i+1):
                        print('*',end=" ")
                    print()
            else:
                print("\nEnter a row number greater or equal to 2 or less than equal to 15.")
        case 2:
            n1=int(input('Enter the starting number for range: '))
            n2=int(input('Enter the ending number for range: '))
            if n1>n2:
                print("\nStarting number should be less than the ending number.")
            else:
                Sum=0
                for i in range(n1,n2):
                    if i%2==0:
                        print(i," is even")
                    else:
                        print(i," is odd")
                    Sum=Sum+i
                print("Sum of numbers in range ",n1," , ",n2," is :",Sum)
        case 3:
            print("\n\tThank you for using the pattern generator and number analyzer , come back soon!")
            break
        case _:
            print("\nPlease enter a number from give choices.")
            continue
            break
