import smtplib
import ssl


def send_email(daily_news):
    host = "smtp.gmail.com"
    port = 465

    username = "<Email-address>"
    password = "<APP-password>"

    receiver_email = "<Receiver-email-address>"

    context = ssl.create_default_context()

    # Send a mail to concern group or product owner.
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, daily_news)
