def Create_File(filename):
    try:
        with open(filename,'x') as f:
            pass 
        print("\nFile created successfuly")
    except FileExistsError:
        print("\nFile Already Exist.")

def Write_File(filename):
    try:
        f=open(filename,'r')
    except FileNotFoundError:
        print(f"\nError : File {filename} doesn't exist in the present directory.")
    else:
        f.close()
        writedata=input('Enter the data to overwrite to file:\n')
        with open(filename,'w') as f:
            f.write(f'{writedata}\n')
        print("\nData entry overwriting successful.")

def Read_File(filename):
    try:
        with open(filename,'r') as f:
            content=f.read()
        print("File Content: ")
        print(content)
    except FileNotFoundError as e:
        print(f"\nError : {filename} does not exist.")

def Append_File(filename):
    try:
        f=open(filename,'r')
    except FileNotFoundError:
        print(f"\nError : File {filename} doesn't exist in the present directory.")
    else:
        f.close()
        appenddata=input('Enter the data to append to file:\n')
        with open(filename,'a') as f:
            f.write(f'{appenddata}\n')
        print("\nData entry successful.")