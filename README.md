# Password Strength Checker 🔐✨

A simple yet powerful Python project developed during my *Cyber Security & Ethical Hacking Internship*.  
This tool checks whether a user-entered password is *Strong, **Weak, or **Banned*, using two reference lists:
- weak_passwords.txt
- banned_passwords.txt

---

## Features ⚙️

- 📏 Checks password length and complexity
- 🧾 Compares input with known weak and banned password lists
- 💬 Provides clear feedback and suggestions
- 🧠 Smart evaluation logic using regex
- 🔐 Encourages better password hygiene

---

## How It Works ⚡

1. 🧑‍💻 *User enters a password*
2. The script checks:
   - 🔴 If it's in banned_passwords.txt → *Banned Password*
   - 🟡 If it's in weak_passwords.txt → *Weak Password*
   - ✅ Else, it checks rules:
     - ✅ At least 8 characters
     - ✅ Includes *lowercase*
     - ✅ Includes *uppercase*
     - ✅ Includes *digit*
     - ✅ Includes *special character*  
     → then it's a *Strong Password*

---

## Password Rules 📜

To be considered strong, your password must:
- 📏 Be at least 8 characters
- 🔠 Include uppercase letters
- 🔡 Include lowercase letters
- 🔢 Include digits
- 🔣 Include special characters (!@#$%^&*, etc.)

---

## Files 📂

- password_checker.py – Main Python script
- weak_passwords.txt – Common weak passwords
- banned_passwords.txt – Restricted passwords
- README.md – This documentation file

---

## Requirements 🧰

- Python 3.x

---

## How to Run ▶️

```bash
python password_checker.py

---

Sample Passwords 🧪

| Type   | Example                    |
|--------|----------------------------|
| Weak   | 123456, qwerty             |
| Banned | admin123, hackme           |
| Strong | P@ssw0rd123!, MyS3cur3#Key |

---

Author 🙋‍♀️

Pranjali Prashant Jagtap
Intern at Cyber Security & Ethical Hacking Program
Passionate about making the web more secure!
