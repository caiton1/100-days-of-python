import smtplib

user_name = "waynekerr0987@gmail.com"
password = "yxtzfmhpbpfzpklm"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=user_name, password=password)
    connection.sendmail(
        from_addr=user_name,
        to_addrs="connor.nicolai.aiton@gmail.com",
        msg="Subject:Hello\n\n poop"
    )

