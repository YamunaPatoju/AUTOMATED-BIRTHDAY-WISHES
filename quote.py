import smtplib
import datetime as dt
import random

#date module

now = dt.datetime.now()
week_day = now.weekday()
if week_day == 0:
    with open("C:\\Users\\DELL\\Desktop\\automated wishes\\quotefile.txt" , encoding= "utf-8") as thought_file:
        all_quotes = thought_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    my_email = "yamunapatoju7@gmail.com"
    password = "sdhy ayxl avhr kjbb"

    connection = smtplib.SMTP("smtp.gmail.com" , 587)
    connection.starttls()
    connection.login(user = my_email , password = password )
    subject = "Subject: MONDAY MOTIVATION\n"
    message = f"{subject}\n{quote}".encode('utf-8')
    connection.sendmail(to_addrs= "youyamuna.122@gmail.com" , from_addr= my_email , msg= message)
    connection.close()

