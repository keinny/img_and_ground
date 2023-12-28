#Kenneth Nondo
#made for medici Data review process of translation
#version 2
# imports not important all are in the package

import pandas as pd
import os
from tkinter import *
from tkinter import filedialog
from datetime import datetime


path = os.getcwd()

file = pd.read_excel( filedialog.askopenfilename(initialdir =  "/",title = "open excel",filetype = (("spreadsheet","*.xlsx"),("all files","*.*"))))

image_coords_df = file.iloc[28:, :3]
ground_coords_df = file.iloc[28:,5:8]
get_name = str(file.iloc[5,1])


timestamp = datetime.now().strftime("_%Y-%m-%d_%H-%M-%S")
folder_name = get_name + f'{timestamp}'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)


image_coords_df.to_csv(os.path.join(folder_name,get_name +'_image_coords.csv'), index=False, header=False)
ground_coords_df.to_csv(os.path.join(folder_name,get_name +'_ground_coords.csv'), index=False, header=False)



window = Tk()
