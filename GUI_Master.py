

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import CNNModelp 
import sqlite3
import threading 
#import tfModel_test as tf_test
global fn
fn=""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Pest Identification System")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('2.jpg')
image2 =image2.resize((w,h), Image.LANCZOS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
#
lbl = tk.Label(root, text="AgriGuard: Automated Pest Classification", font=('times', 35,' bold '), height=1, width=32,bg="#7a3b2e",fg="white")
lbl.place(x=300, y=20)


frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=220, height=350, bd=5, font=('times', 14, ' bold '),bg="#82b74b")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=10, y=90)

    
    
###########################################################################
def train_model():
 
    update_label("Model Training Start...............")
    
    start = time.time()

    X= CNNModelp.main()
    
    end = time.time()
        
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
    msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

    print(msg)

import functools
import operator


def convert_str_to_tuple(tup):
    s = functools.reduce(operator.add, (tup))
    return s

def test_model_proc(fn):
    from keras.models import load_model
    from keras.optimizers import Adam

#    global fn
    
    IMAGE_SIZE = 64
    LEARN_RATE = 1.0e-4
    CH=3
    print(fn)
    if fn!="":
        # Model Architecture and Compilation
       
        model = load_model('pest_model1.h5')
            
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        
        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
        img = img.astype('float32')
        img = img / 255.0
        print('img shape:',img)
        prediction = model.predict(img)
        print(np.argmax(prediction))
        plant=np.argmax(prediction)
        print(plant)
        
        
        
        if plant == 0:
            Cd="Pesticide = Acephate, Malathion \n Adristyrannus"
        elif plant == 1:
            Cd="Pesticide = Dinotefuran,Acetamiprid \n Aleurocanthus spiniferus"
        elif plant == 2:
            Cd="Pesticide = Malathion,Chlorpyrifos  \n Alfalfa plant bug"
        elif plant == 3:
            Cd="Pesticide = pymetrozine,Azadirachtin \n  Alfalfa seed chalcid"
        elif plant == 4:
            Cd="Pesticide = Carbosulfan,\n  Alfalfa weevil"
        elif plant == 5:
            Cd="Pesticide = Indoxacarb,\n  Ampelophaga"
        elif plant == 6:
            Cd="Pesticide = Syngenta ampilgo, \n Aphids"
        elif plant == 7:
            Cd="Pesticide = Imidacloprid, \n  Aphis citricola Vander Goot"
        elif plant == 8:
            Cd="Pesticide =Acela , \n Apolygus lucorum"
        elif plant == 9:
            Cd="Pesticide = Bacillus thuringiensis, \n  Army worm"
        elif plant == 10:
            Cd="Pesticide = Chlorantraniliprole, \n  Asiatic rice borer"
        elif plant == 11:
            Cd="Pesticide = Dichlororvos , \n Bactrocera tsuneonis"
        elif plant == 12:
            Cd="Pesticide = Bifenthrin, \n Beet army worm"
        elif plant == 13:
            Cd="Pesticide =Pyrethrin , \n Beet fly"
        elif plant == 14:
            Cd="Pesticide =Nuvan ,\n  Beet spot flies"
        elif plant == 15:
            Cd="Pesticide =Novacide ,\n  Beet weevil"
        elif plant == 16:
            Cd="Pesticide =Malathion , \n Beetle"
        elif plant == 17:
            Cd="Pesticide =Acephate , \n  Bird cherry-oataphid"
        elif plant == 18:
            Cd="Pesticide =Deltamethrin ,\n  Black cutworm"
        elif plant == 19:
            Cd="Pesticide =Phendal ,  \n  Black hairy"
        elif plant == 20:
            Cd="Pesticide =Carbaryl , \n  Blister beetle"
        elif plant == 21:
            Cd="Pesticide =Acephate , \n  Bollworm"
        elif plant == 22:
            Cd="Pesticide=Fenpyroximate, Spiromesifen,\n Brevipoalpus lewisi McGregor"
        elif plant == 23:
            Cd="Pesticide =Systemic ,\n Brown plant hopper"
        elif plant == 24:
            Cd="Pesticide =Bacillus thuriniensis , \n Cabbage army worm"
        elif plant == 25:
            Cd="Pesticide= Imidacloprid, Thiacloprid, \n Cerodonta denticornis"
        elif plant == 26:
            Cd="Pesticide =Imidacloprid ,\n Ceroplastes rubens"
        elif plant == 27:
            Cd="Pesticide =Phoskill ,\n Chlumetia transversa"
        elif plant == 28:
            Cd="Pesticide= Acetamiprid, Buprofezin,\n Chrysomphalus aonidum"
        elif plant == 29:
            Cd="Pesticide=Thiacloprid, Dinotefuran, \n Cicadella viridis"
        
            
        A=Cd
        return A

############################################################
def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=60, font=("bold", 20), bg='bisque2', fg='black')
    result_label.place(x=250, y=400)

###############################################################################


def test_model():
    global fn
    if fn!="":
        update_label("Model Testing Start...............")
        
        start = time.time()
    
        X=test_model_proc(fn)
        
        X1="Selected Image is {0}".format(X)
        x2=format(X)+" Diesease is detected"
        
        end = time.time()
            
        ET="Execution Time: {0:.4} seconds \n".format(end-start)
        
        msg="Image Testing Completed.."+'\n'+ x2 + '\n'+ ET
        fn=""
    else:
        msg="Please Select Image For Prediction...."
        
    update_label(msg)
    
#############################################################################
    
def openimage():
   
    global fn
    fileName = askopenfilename(initialdir='D:/Kirti Project/23ci1610/23ci1610/code/100% pest identification/dataset/test_set', title='Select image for Aanalysis ',
                               filetypes=[("all files", "*.*")])
    IMAGE_SIZE=200
    imgpath = fileName
    fn = fileName


#        img = Image.open(imgpath).convert("L")
    img = Image.open(imgpath)
    
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
#        img = img / 255.0
#        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)


    x1 = int(img.shape[0])
    y1 = int(img.shape[1])



    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(im)
    img = tk.Label(root, image=imgtk, height=250, width=250)
    img.image = imgtk
    img.place(x=300, y=100)
  
#############################################################################    

def convert_grey():
    global fn    
    IMAGE_SIZE=200
    
    img = Image.open(fn)
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
    
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])

    gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)

    gs = cv2.resize(gs, (x1, y1))

    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print(threshold)

    im = Image.fromarray(gs)
    imgtk = ImageTk.PhotoImage(image=im)
    
    #result_label1 = tk.Label(root, image=imgtk, width=250, font=("bold", 25), bg='bisque2', fg='black',height=250)
    #result_label1.place(x=300, y=400)
    img2 = tk.Label(root, image=imgtk, height=250, width=250,bg='white')
    img2.image = imgtk
    img2.place(x=580, y=100)

    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)

    img3 = tk.Label(root, image=imgtk, height=250, width=250)
    img3.image = imgtk
    img3.place(x=880, y=100)
    #result_label1 = tk.Label(root, image=imgtk, width=250,height=250, font=("bold", 25), bg='bisque2', fg='black')
    #result_label1.place(x=300, y=400)


#################################################################################################################
def window():
    root.destroy()




button1 = tk.Button(frame_alpr, text=" Select_Image ", command=openimage,width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button1.place(x=10, y=40)

button2 = tk.Button(frame_alpr, text="Image_preprocess", command=convert_grey, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button2.place(x=10, y=100)

button3 = tk.Button(frame_alpr, text="Train Model", command=train_model, width=12, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button3.place(x=10, y=130)
#
button4 = tk.Button(frame_alpr, text="CNN_Prediction", command=test_model, width=15, height=1, bg="white", fg="black", font=('times', 15, 'bold'))
button4.place(x=10, y=160)
#
#
button5 = tk.Button(frame_alpr, text="button5", command=window,width=8, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
button5.place(x=450, y=20)


exit = tk.Button(frame_alpr, text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="#7a3b2e",fg="white")
exit.place(x=10, y=220)



root.mainloop()