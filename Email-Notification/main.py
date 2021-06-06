import pandas as pd
from datetime import datetime as dt
import createMail as cm
import getData as gd
import turicreate as tc
import cleanData as cd
import modelApplication

gd.saveData()

df = pd.read_csv('./1.csv')
sf = tc.SFrame('./1.csv')
df, sf = cd.getCleanData(sf)
temperature, time = gd.splitData(df)
time = dt.now()
current_time = time.strftime("%H:%M:%S")
model = modelApplication.loadModel()
prediction = modelApplication.getPrediction(sf.tail(1), model)
prediction = modelApplication.textPrediction(prediction)
address = "saharsh.shukla2018@vitstudent.ac.in"
data = [current_time, temperature, prediction]
print(data)
cm.sendMail(address, data)
print("Mail sent at time: ", time)
