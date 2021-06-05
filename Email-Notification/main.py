import pandas as pd
from datetime import datetime as dt
import createMail as cm
import getData as gd

gd.saveData()

df = pd.read_csv('./1.csv')
temperature, time = gd.splitData(df)
time = dt.now()
current_time = time.strftime("%H:%M:%S")
address = "saharsh.shukla2018@vitstudent.ac.in"
data = [current_time, temperature]
cm.sendMail(address, data)
print("Mail sent at time: ", time)
