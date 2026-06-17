import datetime
class EmptyJournalError(Exception):
    pass
class JournalManager:
    def __init__(self):
        self.filename='Journal.txt'
    def new_entry(self):
        self.entry=input(f'\nEnter your journal entry: \n')
        self.timestamp=datetime.datetime.now().strftime("Date: %d-%m-%Y  Time: %H:%M:%S")
        try:
            with open(self.filename,'a') as file:
                file.write(f'{self.timestamp}\n{self.entry}\n\n')
                print("\nEntry added successfuly.")
        except PermissionError:
            print("Error: Permission denied. Cannot write to the journal file.")
    def display_entry(self):
        try:
            f=open(self.filename,'r')
            content=f.read()
        except FileNotFoundError:
            print("\nNo Journal entries found .Start by adding a new entry.")
        except PermissionError:
            print("Error: Permission denied. Cannot write to the journal file.")
        else:
            if content=="":
                raise EmptyJournalError("Journal is empty so can't display entry")
            else:
                print("\nYour Journal Entries")
                print("-"*85)
                print(content)
                print("-"*85)
    def search_entry(self):
        try:
            f=open(self.filename,'r')
            content=f.read()
        except FileNotFoundError:
            print("\nNo Journal entries found. Start by adding a new entry.")
        except PermissionError:
            print("Error: Permission denied. Cannot write to the journal file.") 
        else:
            if content=="":
                raise EmptyJournalError("Journal is empty so can't find any entry")
            else:
                self.search_word=input("\nEnter a keyword or date to search a entry: ")
                self.match_content=[]
                with open(self.filename,'r') as file:
                    self.content = list(file.read().split("\n\n"))
                for entry in self.content:
                    if self.search_word.lower() in entry.lower():
                        self.match_content.append(entry)
                if not self.match_content:
                    print("\nNo entry found for the specified keyword or date.")
                else:
                    print("Match keyword entry found:")
                    print("-"*85)
                    for entry in self.match_content:
                        print(entry)
                    print("-"*85)
    def delete_element(self):
        try:
            f=open(self.filename,'r')
            content=f.read()
            if content=="":
                raise EmptyJournalError("Journal is empty so can't delete entry")
            else:
                final_choice=input('\nEnter yes to confirm Delete and No to cancel: ')
                if final_choice.lower()=='yes':
                    with open(self.filename,'w') as file:
                        pass
                    print("\nAll data is cleared from Journal File.")
                elif final_choice.lower()=='no':
                    print("\nDeleting all entries from Journal successful")
                else:
                    print("\nEnter valid choice to delete entries of journal or not.")
        except FileNotFoundError:
            print("\nNo Journal entries found. Start by adding a new entry.")
        except PermissionError:
            print("Error: Permission denied. Cannot write to the journal file.")

journal = JournalManager()
 
print("Welcome to Personal Journal Manager!")
 
while True:
    print("\nPlease select an option:\n")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")
    try:
        choice = int(input("\nUser Input:\n"))
    except ValueError:
        print("\nEnter proper value")
    except TypeError:
        print("\nEnter integer as choice only")
    except Exception as e:
        print(f"Error occurred : {e}")
    else:
        match choice:
            case 1:
                journal.new_entry()
            case 2:
                journal.display_entry()
            case 3:
                journal.search_entry()
            case 4:
                journal.delete_element()
            case 5:
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break
            case _ :
                print("Invalid option. Please select a valid option from the menu.")

'''

'''