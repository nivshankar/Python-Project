import numpy as np
import random as r
class DataAnalytics:
    def __init__(self):
        self.array=np.array([])
    def CreateOneDArray(self):
        try:
            self.size=int(input("\nEnter size of 1D array: "))
        except ValueError:
            print("\nEnter a valid number as input.")
        else:
            if self.size<3:
                print("\nPlease enter size greater than 3 so as to analyse the array.")
            elif self.size>30:
                print("\nPlease enter size less than equal to 30.")
            else:
                self.__arrstr=input(f"\nEnter {self.size} elements separated with space : ")
                self.__arrlist=self.__arrstr.strip().split(" ")
                if len(self.__arrlist)<self.size or len(self.__arrlist)>self.size:
                    print(f"\n{self.size} elements are required as per the size of array.")
                else:
                    try:
                        self.array=[]
                        self.array=np.array(list(map(int,self.__arrlist)))
                    except Exception :
                        print("\nInput only numerical values.")
                    else:
                        print("\n1D Array created successfuly: ")
                        print(self.array)
                        self.arr1d=True
                        self.arr2d=False
                        self.arr3d=False

    def CreateTwoDArray(self):
        try:
            self.row=int(input("\nEnter number of row in 2D array: "))
            self.col=int(input("\nEnter number of column in 2D array: "))
        except ValueError:
            print("\nEnter a valid number as input.")
        else:
            if self.row<2 or self.col<2:
                print("\nRow and column should be atleast greater or equal to 2.")
            elif self.row*self.col>30 :
                print("\nSuch a big array size , enter smaller array.")
            else:
                self.__arrstr=input(f"\nEnter {self.row*self.col} elements with space : ")
                self.__arrlist=self.__arrstr.strip().split(" ")
                if len(self.__arrlist)<self.row*self.col or len(self.__arrlist)>self.row*self.col:
                    print(f"\n{self.row*self.col} elements are required as per the size of array.")
                else:
                    try:
                        self.array=[]
                        self.array=np.array(list(map(int,self.__arrlist)))
                    except Exception :
                        print("\nInput only numerical values.")
                    else:
                        print("\n2D Array created successfuly: ")
                        self.array=self.array.reshape(self.row,self.col)
                        print(self.array)
                        self.arr1d=False
                        self.arr2d=True
                        self.arr3d=False

    def CreateThreeDArray(self):
        try:
            self.row=int(input("\nEnter number of row in 3D array: "))
            self.col=int(input("\nEnter number of column in 3D array: "))
            self.depth=int(input("\nEnter depth of 3D array: "))
        except ValueError:
            print("\nEnter a valid number as input.")
        else:
            self.size=self.row*self.col*self.depth
            if self.row<2 or self.col<2 or self.depth<2:
                print("\nRow , column and depth should be atleast greater or equal to 2.")
            elif self.size>30 :
                print("\nSuch a big array size , enter smaller array.")
            else:
                self.__arrstr=input(f"\nEnter {self.size} elements with space : ")
                self.__arrlist=self.__arrstr.strip().split(" ")
                if len(self.__arrlist)<self.size or len(self.__arrlist)>self.size:
                    print(f"\n{self.size} elements are required as per the size of array.")
                else:
                    try:
                        self.array=[]
                        self.array=np.array(list(map(int,self.__arrlist)))
                    except Exception :
                        print("\nInput only numerical values.")
                    else:
                        print("\n3D Array created successfuly: ")
                        self.array=self.array.reshape(self.depth,self.row,self.col)
                        print(self.array)
                        self.arr1d=False
                        self.arr2d=False
                        self.arr3d=True

    def Indexing_Slicing(self):
     if  self.array.size==0:
        print("\nFirst create an array then go for indexing or slicing.")
     else:
        while True:
            print("-"*85)
            print("\nSelect an operation: ")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back to Main Menu")
            try:
                ch=int(input("\nEnter your choice: "))
            except ValueError:
                print("\nEnter a valid number as input.")
            else:
                match ch:
                    case 1:
                        if self.arr1d:
                            self.indexno=int(input("\nEnter index number of element : "))
                            try:
                                print(f"\nThe element at {self.indexno} number is : {self.array[self.indexno]}")
                            except Exception as e:
                                print(f"\nError : {e}")
                        elif self.arr2d:
                            self.indexlist=input("\nEnter row and column number of element comma separated: ").strip().split(",")
                            if len(self.indexlist)!=2:
                                print("\nEnter two inputs as number.")
                            else:
                                try:
                                    a,b=list(map(int,self.indexlist))
                                except Exception as e:
                                    print(f"\n{e}") 
                                else:
                                    if (self.row >=0 and self.col>=0) and (self.row>a and self.col>b):
                                        print(f"\nThe element at index [{a}][{b}] is : {self.array[a,b]}")
                                    else:
                                        print("\nThe index numbers are not valid.")
                        elif self.arr3d:
                            self.indexlist=input("\nEnter layer/depth , row and column numbers of element comma separated: ").strip().split(",")
                            if len(self.indexlist)!=3:
                                print("\nEnter three inputs as number.")
                            else:
                                try:
                                    a,b,c=list(map(int,self.indexlist))
                                except Exception as e:
                                    print(f"\n{e}") 
                                else:
                                    if (self.row >=0 and self.col>=0 and self.depth>=0) and (self.row>b and self.col>c and self.depth>a):
                                        print(f"\nThe element at index [{a}][{b}][{c}] is : {self.array[a,b,c]}")  
                                    else:
                                        print("\nThe index numbers are not valid.") 

                    case 2:
                        if self.arr1d:
                            self.sliceinput=input("\nEnter the your start and end of slicing separated with colon(:) : ").strip().split(":")
                            if len(self.sliceinput)!=2:
                                print("\nEnter both start and end points of slicing as number.")
                            else:
                                try:
                                    start,end=list(map(int,self.sliceinput))
                                except Exception:
                                    print("\nEnter only numbers as range of slicing")
                                else:
                                    print(f"\nOutput of slicing : {self.array[start:end]}")
                        elif self.arr2d or self.arr3d:
                            self.rowslice=input("\nEnter row silicing separated with colon(:) : ").strip().split(":")
                            if len(self.rowslice)!=2:
                                print("\nEnter both start and end points of row slicing as number.")
                                continue
                            else:
                                try:
                                    strow,enrow=list(map(int,self.rowslice))
                                except Exception:
                                    print("\nEnter only numbers as range of slicing")
                                    continue
                                else:
                                    if strow>self.row-1 or enrow>self.row-1 or strow<0 or enrow<0:
                                            print("\nInvalid slicing range.")
                                            continue

                            self.colslice=input("\nEnter column silicing separated with colon(:) : ").strip().split(":")
                            if len(self.colslice)!=2:
                                print("\nEnter both start and end points of column slicing as number.")
                                continue
                            else:
                                try:
                                    stcol,encol=list(map(int,self.colslice))
                                except Exception:
                                    print("\nEnter only numbers as range of slicing")
                                    continue
                                else:
                                    if stcol>self.col-1 or encol>self.col-1 or stcol<0 or encol<0:
                                            print("\nInvalid slicing range.")
                                            continue
                            if self.arr2d:
                                print(f"\nOutput of slicing:\n{self.array[strow:enrow,stcol:encol]}")
                            else :
                                self.depthslice=input("\nEnter layer silicing separated with colon(:) : ").strip().split(":")
                                if len(self.depthslice)!=2:
                                    print("\nEnter both start and end points of layer slicing as number.")
                                    continue
                                else:
                                    try:
                                        stdepth,endepth=list(map(int,self.depthslice))
                                    except Exception:
                                        print("\nEnter only numbers as range of slicing")
                                        continue
                                    else: 
                                        if stdepth>self.depth-1 or endepth>self.depth-1 or stdepth<0 or endepth <0:
                                            print("\nInvalid slicing range.")
                                            continue
                                        print(f"\nOutput of slicing:\n{self.array[stdepth:endepth,strow:enrow,stcol:encol]}")
                    
                    case 3:
                        print()
                        print('Back to main  Menu'.center(65))
                        print("-"*85)
                        break

                    case _:
                        print("\nEnter valid choice")

    def MathematicalOperation(self):
        if  self.array.size==0:
            print("\nFirst create an array then go for Mathematical operations.")
        else:
            self.array2=[]
            while True:
                print("-"*85)
                print("Choose a Mathematical Operation: ")
                print("1. Adding")
                print("2. Subtracting")
                print("3. Multiplication")
                print("4. Division")
                print("5. Back to Main Menu")
                try:
                    mchoice=int(input("Enter your choice: "))
                except ValueError:
                    print("\nEnter choice as an option number.")
                    continue
                if mchoice==5:
                    print()
                    print('Back to main  Menu'.center(65))
                    print("-"*85)
                    break
                if self.arr1d:
                    self.__arrstr=input(f"\nEnter same size array ,{self.size} elements separated with space : ")
                    self.__arrlist=self.__arrstr.strip().split(" ")
                    if len(self.__arrlist)<self.size or len(self.__arrlist)>self.size:
                        print(f"\n{self.size} elements are required as per the size of array.")
                        continue
                    else:
                        try:
                            self.array2=np.array(list(map(int,self.__arrlist)))
                        except Exception :
                            print("\nInput only numerical values.")
                            continue
                elif self.arr2d:
                    self.__arrstr=input(f"\nEnter same sized 2D array, {self.row*self.col} elements separated with space : ")
                    self.__arrlist=self.__arrstr.strip().split(" ")
                    if len(self.__arrlist)<self.row*self.col or len(self.__arrlist)>self.row*self.col:
                        print(f"\n{self.row*self.col} elements are required as per the size of array.")
                        continue
                    else:
                        try:
                            self.array2=np.array(list(map(int,self.__arrlist)))
                            self.array2=self.array2.reshape(self.row,self.col)
                        except Exception :
                            print("\nInput only numerical values.")
                            continue
                elif self.arr3d:
                    self.__arrstr=input(f"\nEnter same sized 3D array,{self.size} elements with space : ")
                    self.__arrlist=self.__arrstr.strip().split(" ")
                    if len(self.__arrlist)<self.size or len(self.__arrlist)>self.size:
                        print(f"\n{self.size} elements are required as per the size of array.")
                        continue
                    else:
                        try:
                            self.array2=np.array(list(map(int,self.__arrlist)))
                            self.array2=self.array2.reshape(self.depth,self.row,self.col)
                        except Exception :
                            print("\nInput only numerical values.")
                            continue
                print(f"\nOriginal Array:\n{self.array}")
                print(f"\nSecond Array:\n{self.array2}")
                match mchoice:
                    case 1:
                        print(f"\nResult array:\n{self.array+self.array2}")
                    case 2:
                        print(f"\nResult array:\n{self.array-self.array2}")
                    case 3:
                        print(f"\nResult array:\n{self.array*self.array2}") 
                    case 4:
                        print(f"\nResult array:\n{self.array/self.array2}")
                    case _:
                        print("\nChoose vaild option from given operation.")

    def Combining_Spliting(self):
        if  self.array.size==0:
            print("\nFirst create an array then go for comibining and splitting.")
        else:
           while True:
                print("-"*85)
                print("Choose an Operation: ")
                print("1. Combining Arrays")
                print("2. Spliting Arrays")
                print("3. Back to Main Menu")
                try:
                    cschoice=int(input("\nEnter your choice: "))
                except ValueError:
                    print("\nEnter choice as an option number.")
                    continue
                match cschoice:
                    case 1:
                        if self.arr1d:
                            self.__arrstr=input(f"\nEnter same size array ,{self.size} elements separated with space : ")
                            self.__arrlist=self.__arrstr.strip().split(" ")
                            if len(self.__arrlist)<self.size or len(self.__arrlist)>self.size:
                                print(f"\n{self.size} elements are required as per the size of array.")
                                continue
                            else:
                                try:
                                    self.array2=np.array(list(map(int,self.__arrlist)))
                                except Exception :
                                    print("\nInput only numerical values.")
                                    continue
                                print(f"\nOriginal Array:\n{self.array}")
                                print(f"\nSecond Array:\n{self.array2}")
                                self.array=np.concatenate((self.array,self.array2))
                                print(f"\nCombined Array:\n{self.array}")
                        elif self.arr2d:
                            self.__arrstr=input(f"\nEnter same sized 2D array, {self.row*self.col} elements separated with space : ")
                            self.__arrlist=self.__arrstr.strip().split(" ")
                            if len(self.__arrlist)<self.row*self.col or len(self.__arrlist)>self.row*self.col:
                                print(f"\n{self.row*self.col} elements are required as per the size of array.")
                                continue
                            else:
                                try:
                                    self.array2=np.array(list(map(int,self.__arrlist)))
                                    self.array2=self.array2.reshape(self.row,self.col)
                                except Exception :
                                    print("\nInput only numerical values.")
                                    continue
                                print(f"\nOriginal Array:\n{self.array}")
                                print(f"\nSecond Array:\n{self.array2}")
                                rchoice=[1,2]
                                if (r.choice(rchoice))==1:
                                    self.array=np.hstack((self.array,self.array2))
                                    print(f"\nCombined Array (hstack):\n{self.array}")
                                else:
                                    self.array=np.vstack((self.array,self.array2))
                                    print(f"\nCombined Array:\n{self.array}")
                        elif self.arr3d:
                            self.__arrstr=input(f"\nEnter same sized 3D array,{self.size} elements with space : ")
                            self.__arrlist=self.__arrstr.strip().split(" ")
                            if len(self.__arrlist)<self.size or len(self.__arrlist)>self.size:
                                print(f"\n{self.size} elements are required as per the size of array.")
                                continue
                            else:
                                try:
                                    self.array2=np.array(list(map(int,self.__arrlist)))
                                    self.array2=self.array2.reshape((self.depth,self.row,self.col))
                                except Exception :
                                    print("\nInput only numerical values.")
                                    continue
                                print(f"\nOriginal Array:\n{self.array}")
                                print(f"\nSecond Array:\n{self.array2}")
                                rchoice=[1,2,3]
                                if (r.choice(rchoice))==1:
                                    self.array=np.concatenate((self.array, self.array2), axis=0)
                                    print(f"\nCombined Array (combined on axis 0):\n{self.array}")
                                elif (r.choice(rchoice))==2:
                                    self.array=np.concatenate((self.array, self.array2), axis=1)
                                    print(f"\nCombined Array (combined on axis 1):\n{self.array}")
                                else:
                                    self.array=np.concatenate((self.array, self.array2), axis=2)
                                    print(f"\nCombined Array (combined on axis 2):\n{self.array}")
                    case 2:
                        if self.arr1d:
                            try:
                                parts=int(input("\nInto how many parts you want to divide array : "))
                            except ValueError:
                                print("\nEnter Valid integer number into how many parts array will divide.")
                                continue
                            try:
                                print(f"\nOriginal Array:\n{self.array}")
                                print(f"\nArray splitted into {parts} parts : \n{np.split(self.array,parts)}")
                            except Exception as e:
                                print(f"Error : {e}")
                        elif self.arr2d:
                            try:
                                parts=int(input("\nInto how many parts you want to divide array : "))
                            except ValueError:
                                print("\nEnter Valid integer number into how many parts array will divide.")
                                continue
                            try:
                                ch=[1,2]
                                if (r.choice(ch)==1):
                                    print(f"Array splitted (hsplit): \n{np.hsplit(self.array,parts)}")
                                else: 
                                    print(f"Array splitted (vsplit): \n{np.vsplit(self.array,parts)}")
                            except Exception as e:
                                print(f"Error : {e}")
                        elif self.arr3d:
                            try:
                                parts=int(input("\nInto how many parts you want to divide array : "))
                            except ValueError:
                                print("\nEnter Valid integer number into how many parts array will divide.")
                                continue
                            try:
                                ch=[1,2,3]
                                if (r.choice(ch)==1):
                                    print(f"Array splitted (about axis 0): \n{np.split(self.array,parts,axis=0)}")
                                elif (r.choice(ch)==2): 
                                    print(f"Array splitted (about axis 1): \n{np.split(self.array,parts,axis=1)}")
                                else:
                                    print(f"Array splitted (about axis 2): \n{np.split(self.array,parts,axis=2)}")
                            except Exception as e:
                                print(f"Error : {e}")
                    case 3:
                        print()
                        print('Back to main  Menu'.center(65))
                        print("-"*85)
                        break
                    case _:
                        print("\nChoose vaild option from given operation.")

    def SearchSortFilter(self):
        if  self.array.size==0:
            print("\nFirst create an array then go for search , sort or filter.")
        else:
            while True:
                print("-"*85)
                print("Choose an Operation: ")
                print("1. Search an element")
                print("2. Sort Array")
                print("3. Filter Array")
                print("4. Back to Main Menu")
                try:
                    sschoice=int(input("\nEnter your choice: "))
                except ValueError:
                    print("\nEnter choice as an option number.")
                    continue
                match sschoice:
                    case 1:
                        try:
                            self.searchval=int(input("\nEnter the element you want to search : "))
                        except ValueError:
                            print("\nEnter a valid numerical value to search.")
                            continue
                        self.result=np.where(self.array==self.searchval)
                        if self.arr1d:
                            if len(self.result[0])==0:
                                print(f"\n{self.searchval} not found in the array.")
                            else:
                                print(f"\n{self.searchval} found at index position(s) : {self.result[0].tolist()}")
                        elif self.arr2d:
                            if len(self.result[0])==0:
                                print(f"\n{self.searchval} not found in the array.")
                            else:
                                positions=list(zip(self.result[0].tolist(),self.result[1].tolist()))
                                print(f"\n{self.searchval} found at [row,column] position(s) : {positions}")
                        elif self.arr3d:
                            if len(self.result[0])==0:
                                print(f"\n{self.searchval} not found in the array.")
                            else:
                                positions=list(zip(self.result[0].tolist(),self.result[1].tolist(),self.result[2].tolist()))
                                print(f"\n{self.searchval} found at [depth,row,column] position(s) : {positions}")
 
                    case 2:
                        print(f"\nOriginal Array:\n{self.array}")
                        if self.arr1d:
                            print(f"\nSorted Array:\n{np.sort(self.array)}")
                        elif self.arr2d:
                            print("\nSort along which axis ?")
                            print("1. Row wise (axis=1)")
                            print("2. Column wise (axis=0)")
                            try:
                                axischoice=int(input("\nEnter your choice: "))
                            except ValueError:
                                print("\nEnter choice as an option number.")
                                continue
                            if axischoice==1:
                                print(f"\nSorted Array (row wise):\n{np.sort(self.array,axis=1)}")
                            elif axischoice==2:
                                print(f"\nSorted Array (column wise):\n{np.sort(self.array,axis=0)}")
                            else:
                                print("\nChoose valid option from given choices.")
                        elif self.arr3d:
                            print("\nSort along which axis ?")
                            print("1. Depth (axis=0)")
                            print("2. Row (axis=1)")
                            print("3. Column (axis=2)")
                            try:
                                axischoice=int(input("\nEnter your choice: "))
                            except ValueError:
                                print("\nEnter choice as an option number.")
                                continue
                            if axischoice==1:
                                print(f"\nSorted Array (axis=0):\n{np.sort(self.array,axis=0)}")
                            elif axischoice==2:
                                print(f"\nSorted Array (axis=1):\n{np.sort(self.array,axis=1)}")
                            elif axischoice==3:
                                print(f"\nSorted Array (axis=2):\n{np.sort(self.array,axis=2)}")
                            else:
                                print("\nChoose valid option from given choices.")
 
                    case 3:
                        print("\nChoose a filter condition: ")
                        print("1. Greater than")
                        print("2. Less than")
                        print("3. Equal to")
                        try:
                            fchoice=int(input("\nEnter your choice: "))
                        except ValueError:
                            print("\nEnter choice as an option number.")
                            continue
                        try:
                            fval=int(input("\nEnter the value to filter with : "))
                        except ValueError:
                            print("\nEnter a valid numerical value.")
                            continue
                        print(f"\nOriginal Array:\n{self.array}")
                        match fchoice:
                            case 1:
                                print(f"\nFiltered Array (elements greater than {fval}):\n{self.array[self.array>fval]}")
                            case 2:
                                print(f"\nFiltered Array (elements less than {fval}):\n{self.array[self.array<fval]}")
                            case 3:
                                print(f"\nFiltered Array (elements equal to {fval}):\n{self.array[self.array==fval]}")
                            case _:
                                print("\nChoose valid option from given choices.")
 
                    case 4:
                        print()
                        print('Back to main  Menu'.center(65))
                        print("-"*85)
                        break
                    case _:
                        print("\nChoose vaild option from given operation.")
 
    def AggregationStatistics(self):
        if  self.array.size==0:
            print("\nFirst create an array then go for aggregations or statistics.")
        else:
            while True:
                print("-"*85)
                print("Choose an Operation: ")
                print("1. Sum")
                print("2. Mean")
                print("3. Maximum")
                print("4. Minimum")
                print("5. Standard Deviation")
                print("6. Variance")
                print("7. Back to Main Menu")
                try:
                    achoice=int(input("\nEnter your choice: "))
                except ValueError:
                    print("\nEnter choice as an option number.")
                    continue
                if achoice==7:
                    print()
                    print('Back to main  Menu'.center(65))
                    print("-"*85)
                    break
                if achoice not in (1,2,3,4,5,6):
                    print("\nChoose vaild option from given operation.")
                    continue
                axischoice=None
                if self.arr2d or self.arr3d:
                    print("\nChoose how you want to compute: ")
                    print("1. Entire Array")
                    if self.arr2d:
                        print("2. Row wise (axis=1)")
                        print("3. Column wise (axis=0)")
                    else:
                        print("2. Depth wise (axis=0)")
                        print("3. Row wise (axis=1)")
                        print("4. Column wise (axis=2)")
                    try:
                        axischoice=int(input("\nEnter your choice: "))
                    except ValueError:
                        print("\nEnter choice as an option number.")
                        continue
                print(f"\nOriginal Array:\n{self.array}")
                if axischoice is None or axischoice==1:
                    axis=None
                elif self.arr2d:
                    if axischoice==2:
                        axis=1
                    elif axischoice==3:
                        axis=0
                    else:
                        print("\nChoose valid option from given choices.")
                        continue
                elif self.arr3d:
                    if axischoice==2:
                        axis=0
                    elif axischoice==3:
                        axis=1
                    elif axischoice==4:
                        axis=2
                    else:
                        print("\nChoose valid option from given choices.")
                        continue
                match achoice:
                    case 1:
                        print(f"\nSum:\n{np.sum(self.array,axis=axis)}")
                    case 2:
                        print(f"\nMean:\n{np.mean(self.array,axis=axis)}")
                    case 3:
                        print(f"\nMaximum:\n{np.max(self.array,axis=axis)}")
                    case 4:
                        print(f"\nMinimum:\n{np.min(self.array,axis=axis)}")
                    case 5:
                        print(f"\nStandard Deviation:\n{np.std(self.array,axis=axis)}")
                    case 6:
                        print(f"\nVariance:\n{np.var(self.array,axis=axis)}")
 
def main():
    print("\nWelcome to the Numpy Analyzer")
    obj=DataAnalytics()
    while True:
        print("="*85)
        print("Choose an Operation: ")
        print("1. Create a Numpy Array")
        print("2. Indexing or Slicing")
        print("3. Perform Mathematical Operations")
        print("4. Combine or split Arrays")
        print("5. Search , sort or filter Arrays")
        print("6. Compute Aggregations and statistics")
        print("7. Exit")
        try:
            choice=int(input("\nEnter your choice: "))
        except ValueError:
            print("\nEnter choice as an option number.")
        else:
            match choice:
                case 1:
                    try:
                        dimension=int(input("\nEnter dimension of array 1 ,2 or 3 : "))
                    except ValueError:
                        print("\nEnter dimension as number.")
                    else:
                        if dimension==1 or dimension==2 or dimension==3:
                            if dimension==1:
                                obj.CreateOneDArray()
                            elif dimension==2:
                                obj.CreateTwoDArray()
                            else:
                                obj.CreateThreeDArray()
                        else:
                           print("\nEnter valid dimension of array.")
                case 2:
                    obj.Indexing_Slicing()
                case 3:
                    obj.MathematicalOperation() 
                case 4:
                    obj.Combining_Spliting() 
                case 5:
                    obj.SearchSortFilter() 
                case 6:
                    obj.AggregationStatistics() 
                case 7:
                    print()
                    print("Thank you for using Numpy Analyzer....".center(68))
                    print("="*85)
                    break
                case _:
                    print("\nEnter valid option number")

if __name__=="__main__":
    main()
