class Employee:
    __employee_id=None
    _name=None
    _age=None
    __salary=None
    def setter(self,id,name,age,salary):
        self.__employee_id=id
        self._name=name
        self._age=age
        self.__salary=salary
    def getter(self):
        return {'Employee Id':self.__employee_id,'Name':self._name,'Age':self._age,'Salary':self.__salary}
    def __del__(self):
        pass

class Manager(Employee):
    def __init__(self,id,name,age,salary,dept):
        self.setter(id,name,age,salary)
        self._department=dept
    def Manager_Info(self):
        info=self.getter()
        info['Department']=self._department
        return info
    def __del__(self):
        pass

class Developer(Employee):
    def __init__(self,id,name,age,salary,lang):
        self.setter(id,name,age,salary)
        self._programming_language=lang
    def Developer_Info(self):
        info=self.getter()
        info['Programming Language']=self._programming_language
        return info
    def __del__(self):
        pass

Developer_List={}
Employee_Ids=[]
Manager_List={}
print("\n","Python OOP Project : Employee Management System ".center(75,"-"))
while True:
    print()
    print("-"*80)
    print("Choose option to manage Employee:")
    print("1 for adding Developer")
    print("2 for adding Manager")
    print("3 for Show Details")
    print("4 for Updating Details of Employee")
    print("5 for Removing an Employee")
    print("6 to Exit the program")
    print("-"*80)
    choice=int(input('Enter your Choice: '))
    match choice:
        case 1:
            id=int(input('\nEnter Employee Id of Developer: '))
            if id in Employee_Ids:
                print("\nThe Employee Id already exists, give different id.")
            else:
                Developer_obj=Developer(
                    id
                    ,input('\nEnter Name of Developer: ')
                    ,int(input('\nEnter Age of Developer: '))
                    ,int(input('\nEnter Salary of Developer: '))
                    ,input('\nEnter Programming Language of Developer: ')
                )
                Employee_Ids.append(id)
                Developer_List[id]=Developer_obj.Developer_Info()
                print("\nDeveloper Data added Successfuly.")
        case 2:
            id=int(input('\nEnter Employee Id of Manager: '))
            if id in Employee_Ids:
                print("\nThe Employee Id already exists, give different id.") 
            else:
                Dept=input('\nEnter Department of Manager: ')
                if Dept in Manager_List.keys():
                    print("\nA Manager already exist in that Department, enter different department.")
                else:
                    Manager_obj=Manager(
                        id
                        ,input('\nEnter Name of Manager: ')
                        ,int(input('\nEnter Age of Manager: '))
                        ,int(input('\nEnter Salary of Manager: '))
                        ,Dept
                    )
                    Employee_Ids.append(id)
                    Manager_List[Dept]=Manager_obj.Manager_Info()
                    print("\nManager Data added Successfuly.") 
        case 3:
           while True:
            print("\nChoose which data to show")
            print("1 for Developer")
            print('2 for Manager ')
            display_choice=int(input("\nYour Choice: "))
            match display_choice:
                case 1:
                    if not Developer_List:
                        print("\nFirst Enter atleast 1 Developer to display the data")
                        break
                    else:
                        i=1
                        for k,v in Developer_List.items():
                            print("-"*85)
                            print(f"Developer {i}".center(80))
                            for key,value in v.items():
                                print(key,": ",value)
                            i+=1
                        break
                case 2:
                    if not Manager_List:
                        print("\nFirst Enter atleast 1 Manager to display the data")
                        break
                    else:
                        i=1
                        for k,v in Manager_List.items():
                            print("-"*85)
                            print(f"Manager {i}".center(80))
                            for key,value in v.items():
                                print(key,": ",value)
                            i+=1 
                        break
                case _:
                    print("\nEnter valid display option")
        case 4:
            while True:
                print("\nChoose which employee to update")
                print("1 for Developer")
                print('2 for Manager ')
                update_choice=int(input("\nYour Choice: "))
                match update_choice:
                 case 1:
                    if not Developer_List:
                        print("\nFirst Enter atleast 1 Developer to display the data")
                        break
                    else:
                        check_id=int(input('\nEnter Employee Id of Developer: '))
                        if check_id in Developer_List.keys():
                            print("\nEnter choice that needs to be updated")
                            print("1 for Name")
                            print("2 for Age")
                            print("3 for Salary")
                            your_choice=int(input('\nYour choice: '))
                            match your_choice:
                                 case 1:
                                      update_Name=input('\nEnter updated name: ')
                                      Developer_List[check_id]['Name']=update_Name
                                      print("\nName updation ==> Successful")
                                      break
                                 case 2:
                                      update_Age=input('\nEnter updated age: ')
                                      Developer_List[check_id]['Age']=update_Age
                                      print("\nAge updation ==> Successful")
                                      break
                                 case 3:
                                      update_Salary=input('\nEnter updated salary: ')
                                      Developer_List[check_id]['Salary']=update_Salary
                                      print("\nSalary updation ==> Successful")
                                      break 
                                 case _:
                                      print("\nEnter valid Choice.")
                                      break
                        else:
                             print("\nThe Employee ID you entered is not present in current Developers IDs.")
                             break

                 case 2:
                    if not Manager_List:
                            print("\nFirst Enter atleast 1 Manager to display the data")
                            break
                    else:
                        check_dept=input('\nEnter Department of Manager: ')
                        if check_dept in Manager_List.keys():
                            print("\nEnter choice that needs to be updated")
                            print("1 for Name")
                            print("2 for Age")
                            print("3 for Salary")
                            your_choice=int(input('\nYour choice: '))
                            match your_choice:
                                 case 1:
                                      update_Name=input('\nEnter updated name: ')
                                      Manager_List[check_dept]['Name']=update_Name
                                      print("\nName updation ==> Successful")
                                      break
                                 case 2:
                                      update_Age=input('\nEnter updated age: ')
                                      Manager_List[check_dept]['Age']=update_Age
                                      print("\nAge updation ==> Successful")
                                      break
                                 case 3:
                                      update_Salary=input('\nEnter updated salary: ')
                                      Manager_List[check_dept]['Salary']=update_Salary
                                      print("\nSalary updation ==> Successful")
                                      break 
                                 case _:
                                      print("\nEnter valid Choice.")
                                      break
                        else:
                             print("\nThere is no Manager in the department you entered.")
                             break
                 case _:
                    print("\nEnter valid update option")
        case 5:
            print("\nChoose Employee to Remove")
            print("1 for Developer")
            print('2 for Manager ')
            remove_choice=int(input("\nYour Choice: "))
            match remove_choice:
                case 1:
                    if not Developer_List:
                        print("There is no Developer Data added , so add first.") 
                    else:
                        remove_id=int(input("\nEnter Employee ID to remove the Developer: "))
                        if remove_id  in Developer_List.keys():
                            print("\nPlease Verify if the person to remove is as below")
                            for k,v in Developer_List[remove_id].items():
                                print(k,': ',v)
                            if input('\nEnter Y To Verify And N to cancel: ')=='Y':
                                Employee_Ids.remove(remove_id)
                                del Developer_List[remove_id]
                                print("\nEmployee Removal ==> Successful")
                            else:
                                    print("\nEmployee Removal ==> Canceled")
                        else:
                                print("\nNo Developer present for the given ID , so Employee Don't Exist.")
                case 2:
                    if not Manager_List:
                            print("There is no Manager Data added , so add first.")
                    else:
                        remove_dept=input("\nTo Remove Manager ,enter Manager Department : ")
                        if remove_dept  in Manager_List.keys():
                            print("\nPlease Verify if the person to remove is as below")
                            for k,v in Manager_List[remove_dept].items():
                                print(k,': ',v)
                            if input('\nEnter Y To Verify And N to cancel: ')=='Y':
                                Employee_Ids.remove(Manager_List[remove_dept]['Employee Id'])
                                del Manager_List[remove_dept]
                                print("\nEmployee Removal ==> Successful")
                            else:
                                    print("\nEmployee Removal ==> Canceled")
                        else:
                                print("\nNo Manager present for the given Department , so Employee Don't Exist.")
                case _:
                    print("\nEnter valid option to remove.")
        case 6:
            print("\nExiting the system. All resources has been cleared")
            Developer_List.clear()
            Manager_List.clear()
            print("\nGoodbye ,See you later.")
            break
        case _:
            print("\nEnter valid option from given List")
