import pandas as pd
import getData as gd
import createMail as cm
import time
gd.saveData()

df = pd.read_csv('./1.csv')
temperature, time = gd.splitData(df)
address = "saharsh.shukla2018@vitstudent.ac.in"
data = [time, temperature]
cm.sendMail(address, data)
a = time.time
print("Mail sent at time: ", a)



