import tkinter as tk
from tkinter import filedialog
import ntpath
import re
import pandas as pd

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
head, tail = ntpath.split(file_path)

tail_length = len(tail)
file_month = year = tail[0:tail_length - 8]
file_year = tail[tail_length - 8:tail_length - 4]

my_file = open(file_path, "r").read().split("=")
list_size = len(my_file)

temp = []
for t in my_file:
    temp.append(t.split())
    
for x in range(1, list_size - 1):
    del temp[x][0]
    
type = []
station = []
day = []
month = []
year = []
hour = []
correction = []
body = []

for i in range(0,list_size - 1):
    type.append(temp[i][0])
    station.append(temp[i][1])
    str = temp[i][2]
    day.append(str[0:2])
    month.append(file_month)
    year.append(file_year)
    hour.append(str[2:len(str)])
    body_str = ""
    if re.search(r'^\s*([A-Z]\s*){3}$', temp[i][3]):  
        correction.append(temp[i][3])
        for j in range(4,len(temp[i]) - 1):
            body_str = body_str + temp[i][j] + " "
    else:
        correction.append("-")
        for j in range(3,len(temp[i]) - 1):
            body_str = body_str + temp[i][j] + " "
    body.append(body_str)
    
    
dict = {'type': type, 'station': station, 'day': day, 'month': month, 'year': year, 'hour': hour, 'correction': correction, 'body':body}
df = pd.DataFrame(dict) 
df_reset=df.set_index('type')
output_file = file_month + file_year + ".csv"
df_reset.to_csv(output_file) 
