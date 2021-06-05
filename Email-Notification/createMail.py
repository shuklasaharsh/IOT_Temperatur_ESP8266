import yagmail
import time
from CONSTANTS import CONSTANTS

email, password = CONSTANTS.email.value, CONSTANTS.password.value
yag = yagmail.SMTP(email, password)


def sendMail(address, data):
    send = f"Your cook time is: {data[0]} \n and the temperature is {data[1]}"
    s = time.time()
    yag.send(to=address, subject='YOUR COOK TEMP!', contents=send)
    print(time.time() - s)
