import smtplib

my_email = "yamunapatoju7@gmail.com"
password = "gqsz hain omuh cepk"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user= my_email , password= password)
connection.sendmail(to_addrs= "youyamuna.122@gmail.com" , from_addr= my_email , msg= "Subject :hello \n\n hiu its my bornday")
connection.close()