import tkinter
from tkinter import *
from selenium import webdriver
import requests

root= Tk()
root.title("Weather Update")
root.geometry('500x40')

def rain():    
    state=city.get()
    driver = webdriver.Chrome('C:\\Users\\gaura\\Documents\\Downloads\\Chrome\\chromedriver.exe')
    driver.get("https://www.google.com/search?q=rain+in+"+state+"&oq=rain+in+"+state+"&aqs=chrome..69i57j69i60.2518j0j7&sourceid=chrome&ie=UTF-8")
    ratings = driver.find_element_by_class_name('wob_t').text
    status = driver.find_element_by_id('wob_dcp').text
    L12=Label(root,text="Weather")
    L12.grid(row=2,column=1,)
    L12=Label(root,text=status)
    L12.grid(row=2,column=2,columnspan=2)
    L13=Label(root,text="Current Temperature")
    L13.grid(row=3,column=1,columnspan=2)
    L13=Label(root,text=ratings)
    L13.grid(row=3,column=3,columnspan=2)


l1= Label(root,text='City')
l1.grid(row=1,column=1)

city=StringVar()
e1 = Entry(root,textvariable=city)
e1.grid(row=1,column=2)

b1 = Button(root, text='Button', command=rain)
b1.grid(row=1,column=3)

mainloop()