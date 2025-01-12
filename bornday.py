from datetime import datetime
import pandas as pd
import smtplib
import random

MY_EMAIL = "yamunapatoju7@gmail.com"  # Your email
MY_PASSWORD = "gqsz hain omuh cepk"  # Your password

today = datetime.now()
today_tuple = (today.month, today.day)

# Load birthdays from CSV
data = pd.read_csv("birthdays.csv")
print("Birthdays loaded successfully.")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for index, data_row in data.iterrows()}
print(birthdays_dict)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # Randomly select a letter template number
    file_number = random.randint(1, 3)  # Generates a random integer between 1 and 3
    print(f"Selected letter template number: {file_number}")

    # Construct the file path
    file_path = f"C:\\Users\\DELL\\Desktop\\automated wishes\\letter_templates\\letter_{file_number}.txt"

    # Open and read the letter template
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])  # Ensure this key matches your CSV

    # Send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],  # Use the email from the CSV
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
    print("Email sent successfully!")
else:
    print("No birthdays today.")
