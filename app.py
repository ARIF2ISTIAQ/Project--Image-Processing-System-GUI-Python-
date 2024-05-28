# from cProfile import label
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import os
import mean_median_gaussian
from matplotlib.pyplot import text
import guassian
from tkinter import Label
import mean2d
from matplotlib import image
import oneD

gui_root=Tk()
gui_root.title('App for image processing ')
#with and height
gui_root.geometry("400x200")

#maximum and minimum
gui_root.minsize(920,700)
gui_root.maxsize(1000,800)


label=Label(text="MAIN SYSTEM")
label.pack(pady=40)
label1=Label()
label1.pack()
label2=Label()
label2.pack()
globalimage='';


def open_file():
       fln = filedialog.askopenfilename(initialdir=os.getcwd(),title = "Select Image",
        filetypes= (("JPG file","*.jpg"),('PNG file','*.png'),('All File','*.*')))
       ext=fln.split('.')
       global globalimage
       globalimage = fln;
    #    print(ext[1])
       img = Image.open(fln)
       saveimage='before.'+ext[1]
       img.save(saveimage)
       img.thumbnail((400,400))
       img = ImageTk.PhotoImage(img)
       label.configure(image=img)
       label.image = img
def processing():
    country= c.get()
    if country =='Mean 2D':
        mean2d.func(globalimage)
        img = Image.open('output.jpg')
        img = img.resize((250,150))
        img.thumbnail((400,400))
        img = ImageTk.PhotoImage(img)
        label1.configure(image=img)
        label1.image = img
    elif country == 'Mean 1D':
        oneD.test()
    elif country == "Gaussian 2D":
        guassian(globalimage)
        img = Image.open('output.jpg')
        img = img.resize((250,150))
        img.thumbnail((400,400))
        img = ImageTk.PhotoImage(img)
        label1.configure(image=img)
        label1.image = img
    elif country == 'Median 2D':
        mean_median_gaussian.func2(globalimage)
    
    print(country)
    

# Dropdown menu options
options = [
    "Mean 1D",
    "Median 1D",
    "Mean 2D",
    "Median 2D",
    "Gaussian 2D"
]

clicked = StringVar()
clicked.set( "Mean 1D" )

select_file = Label(gui_root, 
                  text = "").place(x = 80,y = 140)

image=ttk.Button(gui_root, text="Browse", command=open_file).pack(pady=30)
    

# label_4 = Label(gui_root, text="SELECT FILTER")
# label_4.place(x=60,y=80)


c=StringVar()
droplist=OptionMenu(gui_root,c, *options)
droplist.config(width=15)
label_4 = Label(gui_root, text="SELECT FILTER")
label_4.place(x=40,y=70)
label_4.pack()
c.set('Select Image' ) 
droplist.pack()

button = ttk.Button(gui_root, text="Process Image", command=processing)
button.place(x=60,y=80)
button.pack(pady=20)
label9=Label(gui_root,text="without")


gui_root.mainloop()