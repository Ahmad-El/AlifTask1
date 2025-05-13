import smtplib


def send_email(to_email, subject, message):
    sender_email = "your_email@gmail.com"
    password = "your_password"

    msg = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, to_email, msg)
    server.quit()
