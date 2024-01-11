# Python-PasswordManager


 ### [Password Manager Medium](https://medium.com/@michaellopezcs17/creating-a-password-manager-in-python-d3e95b58b933)
 
Introduction: 

In this password manager, we have created a simple command-line tool to help users manage their passwords securely. The password manager offers features such as creating an account, adding passwords for different websites or applications, retrieving passwords, generating strong passwords, checking password strength, checking password policy compliance, changing passwords, and saving the password data to a file.
![image](https://github.com/Merlowpe1504/Python-PasswordManager/assets/154375598/cdd2782f-5414-438f-8b6f-9fd3fe27967f)


Password Generation:

The tool can generate strong passwords using a combination of uppercase and lowercase letters, digits, and special characters. It ensures that the generated passwords meet the recommended length and complexity criteria.

Password Strength Validator:

The password strength check function evaluates the entered password against OWASP guidelines. It provides feedback on whether the password is weak or strong based on factors like length, the presence of digits, letters, uppercase letters, and special characters.

Password Policies:

The password policy check function enforces a 90-day password policy. It verifies whether a password meets the specified criteria and hasn't been used recently. Additionally, it includes a minimum password age requirement of 3 days.
![image](https://github.com/Merlowpe1504/Python-PasswordManager/assets/154375598/2003f414-7417-4c80-a5d2-86383733249b)

Account Creation:

Users can create an account by providing a username and a desired password. The password is securely hashed using SHA-256 before storage. The tool also keeps track of previous passwords to prevent reuse.

Password Management:

Users can add passwords for different websites or applications, retrieve passwords when needed, and change passwords with a new and secure one. The tool ensures that changed passwords adhere to the password policy.
![image](https://github.com/Merlowpe1504/Python-PasswordManager/assets/154375598/588fb1b5-62b3-456a-9532-50ea63a197fc)
![image](https://github.com/Merlowpe1504/Python-PasswordManager/assets/154375598/79a837a1-4a93-4212-a18e-c111ac3f38ee)

Data Storage:

The password data is stored in a JSON file named 'passwords.json.' This allows users to save their password information persistently and retrieve it when needed.

Usage:

The password manager operates through a user-friendly menu where users can select various options to manage their passwords. The tool runs in a loop until the user chooses to exit, saving the password data to the file upon exit.

This password manager provides a convenient and secure way for users to handle their passwords, promoting good security practices and compliance with recommended password policies.
