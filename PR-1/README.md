# Interactive Personal Data Collector 🧾🐍

A beginner-friendly Python project that collects personal information from the user and displays:

- Name
- Age
- Height
- Favourite Number
- Data Types of Inputs
- Memory Addresses using `id()`
- Approximate Birth Year

---

## 📌 Features

- Interactive input collection
- Demonstrates Python data types
- Shows memory addresses of variables
- Calculates approximate birth year
- Clean terminal-based output

---

## 💻 Python Code

```python
print("\n\tWelcome the Interactive Personal Data Collector !!")
name = input("\n\tEnter Your name : ")
age =int (input("\tEnter your age : "))
height =float (input("\tEnter your height in meters : "))
fav=int (input("\tEnter your favourite number : "))

print("\n\tThank you! Here is the information we collected:\n")

print("\tName: ",name," (Type : ",type(name)," , Memory address: ",id(name))
print("\tAge: ",age," (Type : ",type(age)," , Memory address: ",id(age))
print("\tHeight: ",height," m  (Type : ",type(height)," , Memory address: ",id(height))
print("\tFavourit number: ",fav," (Type : ",type(fav)," , Memory address: ",id(fav))

Byear=2026-age

print("\n\tYour Birth year is approximately: ",Byear,"(Based on your age of ",age,")")
```

---

## ▶️ Sample Output

```text
Welcome the Interactive Personal Data Collector !!

Enter Your name : Neev
Enter your age : 19
Enter your height in meters : 1.6
Enter your favourite number : 77

Thank you! Here is the information we collected:

Name:  Neev  (Type :  <class 'str'> , Memory address: 2608350112064)
Age:  19  (Type :  <class 'int'> , Memory address: 140717495698920)
Height:  1.6 m  (Type :  <class 'float'> , Memory address: 2608310949104)
Favourite number:  77  (Type :  <class 'int'> , Memory address: 140717495700776)

Your Birth year is approximately: 2007 (Based on your age of 19)
```


## 📚 Concepts Used

- `input()`
- Type Casting (`int`, `float`)
- `print()`
- `type()`
- `id()`
- Variables and Arithmetic Operations

---
