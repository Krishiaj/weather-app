#imported tkinter
from tkinter import *
#imported ttk from tkinter
from tkinter import ttk


#Adding API for data:

import requests

def data_get():


#API key: a944b2ba1e6316ebb298abefed17833c
      city =city_name.get()
      data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a944b2ba1e6316ebb298abefed17833c").json()
      w_label1.config(text= data["weather"][0]["main"])
      wb_label1.config(text=data["weather"][0]["description"])
      temp_label1.config(text =str(int(data["main"]["temp"]-273.15)))
      per_label1.config(text=data["main"]["pressure"])


#Created win variable and initialized it with Tk() class to 
# create a window
win = Tk()

#Set the title of the window  by calling win variable which has already stored  tkinker 
win.title("SkyScope")


#Set the background color of the window by calling win variable which has already stored tkinker
win.config(bg = "blue")


#Set the size of the window by calling win variable which has already stored tkinker
win.geometry("500x570")


#Adding title within the window by calling win variable which has already stored tkinker and within the variable 
# which would be name_lable will have label function in that new variable text would be given which would store the string

name_label = Label(win,text = "SkyScope",font =("Arial", 30, "bold"))

name_label.place(x = 25,y= 50,height=50,width=450)


#Created combobox by adding ttk library and calling the ttk library with combobox function then whole command has been stored in the variable com. 
# We have also included all the parameters in it which is there in the name_label variable.
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, text = "SkyScope", values=list_name, font = ("Arial", 30, "bold"),textvariable=city_name )
#set the default value of the combobox to first item of the list
com.place(x =25, y=120, height=50, width=450)

#Creating a column: 
w_label = Label(win,text = "Weather Climate",font =("Arial", 20))

w_label.place(x = 25,y=260,height=50,width=210)

#Creating Column
w_label1 = Label(win,text = "",font =("Arial", 20))

w_label1.place(x = 250,y=260,height=50,width=210)

#Creating a column:
wb_label = Label(win,text = "Weather Discription",font =("Arial", 17))

wb_label.place(x = 25,y=330,height=50,width=210)

#Creating column:
wb_label1 = Label(win,text = "",font =("Arial", 17))

wb_label1.place(x = 250,y=330,height=50,width=210)

#Creating a column:
temp_label = Label(win,text = "Temperature",font =("Arial", 20))

temp_label.place(x = 25,y=400,height=50,width=210)

#Creating column:
temp_label1 = Label(win,text = "",font =("Arial", 20))

temp_label1.place(x = 250,y=400,height=50,width=210)


#Creating a column:
per_label = Label(win,text = "Pressure",font =("Arial", 20))

per_label.place(x = 25,y=470,height=50,width=210)


#Creating column:
per_label1 = Label(win,text = "",font =("Arial", 20))

per_label1.place(x = 250,y=470,height=50,width=210)



#Creating a button 
done_button = Button(win, text = "Done",font = ("Arial", 30, "bold"), command= data_get)
#placed the button in the window
done_button.place(x =200,y=190, height=50, width=100)














#runned the mainloop function by calling win variable
# to keep the window open
win.mainloop()

