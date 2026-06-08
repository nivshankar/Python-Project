def fact(n):
    """
    The function takes an integer as an input and uses Recursion
    function for factorial to return its value as an integer.

    fact(n)=n*(n-1)*(n-2)*......*3*2*1

    The function returns the factorial of the argument number. 
    """
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
    

def Max_2D(Matrix=[]):
    """
    This function takes argument as a list containing multiple list in it 
    also known as Matrix.

    It return maximum value of element present in the Matrix.

    It's return type is integer.
    """
    Max=Matrix[0][0]
    for row in Matrix:
        for ele in row:
            if ele>Max:
                Max=ele
    return Max

def Min_2D(Matrix=[]):
    """
    This function takes argument as a list containing multiple list in it 
    also known as Matrix.

    It return minimum value of elements present in the Matrix.

    It's return type is integer.
    """
    Min=Matrix[0][0]
    for row in Matrix:
        for ele in row:
            if ele<Min:
                Min=ele
    return Min

def Sum_2D(Matrix=[]):
    """
    This function takes argument as a list containing multiple list in it 
    also known as Matrix.

    It return sum of elements present in the Matrix.

    It's return type is integer.
    """
    Sum=0
    for row in Matrix:
        for ele in row:
            Sum+=ele
    return Sum

def Avg_2D(Matrix=[]):
    """
    This function takes argument as  list ,No of Rows and No of Columns
    containing multiple list in it also known as Matrix.

    It return Average of elements present in the Matrix.

    It's return type is float.
    """
    Sum=0
    NoOfElement=0
    for row in Matrix:
        for ele in row:
            Sum+=ele
            NoOfElement+=1
    avg =Sum/NoOfElement
    return avg

print("\n","Welcome to Data Analyzer and Transformer Program".center(90,"-"))

matrix=[]
input_array_1D=[]
sample_arr_1D=[]
Array_1d=[]
array_dimension=None
row=None
col=None

while True:
    print("\nSelect from the menu which operation you want to use:\n")
    print("1.Insert Data as an array")
    print("2.Display Data Summary")
    print("3.Calculate Factorial (Recursion)")
    print("4.Filter Data By Threshold")
    print("5.Sort Data")
    print("6.Exit Program")
    choice=int(input('\nEnter your choice: '))
    match choice:
        case 1:
            Array_1d.clear()
            matrix.clear()
            array_dimension=int(input("\nEnter the dimension of the array from 1 or 2: "))
            if array_dimension>2 or array_dimension<1:
                print("\nPlease enter dimension either 1 or 2")
                continue
            if array_dimension==1:
                array_choice=input("\nType 'Sample' to use sample array "
                "\nOr Type 'Input' to take input from user: ")
                if array_choice=='Sample':
                    sample_arr_1D=[10,3,7,32,21,76,80,110,6,-7]
                    Array_1d=sample_arr_1D.copy()
                    print(f"\nThe following is the sample array: {sample_arr_1D}")
                elif array_choice=='Input':
                    input_array_1D=[]
                    size=int(input("\nEnter array size: "))
                    print("\nEnter array elements:\n")
                    for i in range(size):
                        ele=int(input(f"a[{i}] : "))
                        input_array_1D.append(ele)
                    Array_1d=input_array_1D.copy()
                    print(f"\nThe following is the input array: {input_array_1D}")
                else:
                    print("\nType your choice as instructed.")
                    continue
            else:
                row=int(input("\nEnter row size of array: "))
                col=int(input("\nEnter column size of array: "))
                matrix=[]
                print("\nEnter arrat's elements: ")
                for r in range(row):
                    row_ele=[]
                    for c in range(col):
                        ele=int(input(f"a[{r}][{c}] : "))
                        row_ele.append(ele)
                    matrix.append(row_ele)
                print(f"\nThe following is the input Matrix: \n")
                for row in matrix:
                    for ele in row:
                        print(ele,end="  ")
                    print()
        case 2:
            if array_dimension==None:
                print("\nFirst insert an array.")
                continue 
            if array_dimension==1:
                print("\nData Summary:")
                print(f"Total elements: {len(Array_1d)}")
                print(f"Minimum value : {min(Array_1d)}")
                print(f"Maximum value : {max(Array_1d)}")
                print(f"Sum of all values : {sum(Array_1d[::])}")
                print("Average value: %.2f"%((sum(Array_1d[::]))/(len(Array_1d))))
            else:
                print("\nData Summary:")
                print(f"Total elements: {len(matrix)*len(matrix[0])}")
                print(f"Minimum value : {Min_2D(matrix)}")
                print(f"Maximum value : {Max_2D(matrix)}")
                print(f"Sum of all values : {Sum_2D(matrix)}")
                print("Average value: %.2f"%(Avg_2D(matrix)))
        case 3:
            n=int(input("\nEnter a number to calculate it's factorial: "))
            print(f"\nThe Factorial of {n} is {fact(n)}")
        case 4:
            if array_dimension==None:
                print("\nFirst insert an array.")
                continue 
            threshold=int(input("\nEnter a threshold value to filter out data above this value:"))
            filter=lambda x: x>=threshold
            filtered=[]
            if array_dimension == 1:

                for ele in Array_1d:
                    if filter(ele):
                        filtered.append(ele)

            else:

                for row in matrix:
                    for ele in row:
                        if filter(ele):
                            filtered.append(ele)

            print(f"\nElements greater than or equal to {threshold}:")
            print(filtered)
        case 5:
            if array_dimension==None:
                print("\nFirst insert an array.")
                continue
            print("\nHere are the sorting options available: ")
            print("1 for Ascending")
            print("2 for Descending") 
            sort_choose=int(input("Enter sorting choice: ")) 
            match sort_choose:
                case 1:
                    if array_dimension==1:
                        Array_1d.sort()
                        print(f"Sorted array in ascending: {Array_1d}")
                    else:
                        sorted_2d=sorted(matrix)
                        print(f"Sorted matrix using sorted method: {sorted_2d}")
                case 2:
                    if array_dimension==1:
                        Array_1d.sort(reverse=True)
                        print(f"Sorted array in ascending: {Array_1d}") 
                    else:
                        sorted_2d=sorted(matrix,reverse=True)
                        print(f"Sorted matrix using sorted method: {sorted_2d}")
                case _:
                    print("\nPlease enter valid sort option available")
        case 6:
            print("-"*90)
            print("\n\nThank you for using the Data Analyser and Transformer Program\n")
            break
