import yagmail
import time
from CONSTANTS import CONSTANTS

email, password = CONSTANTS.email.value, CONSTANTS.password.value
yag = yagmail.SMTP(email, password)


def sendMail(address, data):
    send = f"At time: {data[0]} \n the oven temperature is {data[1]}, We expect the meal to be {data[2]}"
    s = time.time()
    yag.send(to=address, subject='YOUR COOK TEMP!', contents=send)
    print(time.time() - s)
