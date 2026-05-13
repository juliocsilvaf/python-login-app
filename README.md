# 🔐 Python Login Application

Academic project developed as part of the **Certificate IV in Information Technology** at **TAFE NSW** (Sydney, Australia).

A console-based login application built in Python that handles user registration, authentication and account display — storing credentials in a text file.

---

## 📋 Project Overview

**Unit assessed:** ICTPRG302 – Apply Introductory Programming Techniques

The application simulates a simple login system with three components as per the client requirements from Gelos Enterprises:

- **Component 1** – New user registration
- **Component 2** – User login and authentication
- **Component 3** – Display existing user accounts

---

## 💡 Features

- Register a new user with username and password
- Password validation — minimum length of 10 characters
- Login authentication by comparing input against stored credentials
- Display all registered usernames (without passwords)
- Persistent data storage using a text file (`accounts.txt`)
- Recursive input handling for invalid entries

---

## 📁 Files

| File | Description |
|------|-------------|
| `login_app.py` | Main Python application — all three components |
| `accounts.txt` | Text file storing registered usernames and passwords |

---

## ⚙️ How It Works

```
--Main Menu--

Type 1 for New Registration
Type 2 for Login
Type 3 for Exit
```

**Registration:** User enters a username and password (min. 10 characters) → saved to `accounts.txt` as `username,password`

**Login:** User enters credentials → compared line by line with `accounts.txt` → displays all usernames if successful

**Display Users:** Lists all registered usernames and total count

---

## 🔍 Key Concepts

```python
# File write — append new user
myfile = open("accounts.txt", "a")
myfile.write(f"{username},{password}\n")

# File read — authenticate user
lines = myfile.read().splitlines()
for line in lines:
    words = line.split(",")
    if words[0] == username and password == words[1]:
        print("Correctly Username and Password!!")
```

**Concepts applied:**
- Functions (`def`)
- File I/O (`open`, `read`, `write`, `splitlines`, `split`)
- Input validation (`len`)
- Loops (`for`)
- Conditionals (`if/elif/else`)
- Recursion for invalid input handling
- String formatting (f-strings)
- `sys.exit()` for clean program termination

---

## 🛠️ Technologies

- **Python 3**
- File I/O (text file as data store)
- Console-based UI

---

## ▶️ How to Run

```bash
python login_app.py
```

Make sure `accounts.txt` exists in the same directory before running.

---

## 🎓 Context

Completed as Assessment Event 2 of 3 for the unit ICTPRG302 — **Certificate III in Information Technology** at **TAFE NSW**, Sydney, Australia (2024).

---

*Julio Cesar da Silva Filho | [LinkedIn](https://www.linkedin.com/in/julio-cesar-filho-84241842/)*
