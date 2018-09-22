#pip install pytube
from pytube import YouTube
import pandas as pd
import os
df = pd.read_csv('youtube_list.csv', delimiter=',', header=None)
df.columns.tolist()
#set working directory to save files into
os.getcwd()
os.chdir("C:\\2018_working\\BrisbaneAI\\CS231Lectures")
os.getcwd()

for index, row in df.iterrows():
   print (row[0])
   #YouTube(row[0]).streams.first().download()
   print(YouTube(row[0]).title)
