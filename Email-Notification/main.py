import pandas as pd
import getData as gd
import createMail as cm

gd.saveData()

df = pd.read_csv('./1.csv')
temperature, time = gd.splitData(df)
address = input("Enter Email: ")
data = [time, temperature]
cm.sendMail(address, data)




