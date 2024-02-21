import smtplib, ssl


def sendmail(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    username = "saivenkatesh619@gmail.com"
    password = "lfzwbmpcwxtasafu"

    sendto = "hemalathaande12@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, sendto, message)
