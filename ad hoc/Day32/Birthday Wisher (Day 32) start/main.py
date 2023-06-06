import smtplib
import datetime as dt
import random

# get current time
now = dt.datetime.now()
weekday = now.weekday()
user_name = "waynekerr0987@gmail.com"
password = "yxtzfmhpbpfzpklm"


# if its a monday

if weekday == 0:
    with open("quotes.txt", "r") as quotefile:
        all_quotes = quotefile.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=user_name, password=password)
        connection.sendmail(
            from_addr=user_name,
            to_addrs="connor.nicolai.aiton@gmail.com",
            msg=f"Subject:Monaday motivation\n\n {quote}"
        )







