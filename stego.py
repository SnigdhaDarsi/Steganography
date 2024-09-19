from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import cv2
import numpy as np

root = Tk()
root.title("Steganography - Hide a Message in an Image")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#fefae0")

def showimage():
    global img
    global img_pil
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetype=(("PNG file","*.png"),("JPG file","*.jpg"),("ALL files","*.")))
    img_pil = Image.open(filename)
    img = ImageTk.PhotoImage(img_pil)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

def hide_message_in_plane(plane, message):
    # Flatten the 2D plane into a 1D array
    flat_plane = plane.flatten()
    #to know how long the message is for decoding, the first byte of the plane will be the message length
    flat_plane[0] = len(message)
    #convert message to binary
    message = ''.join([format(ord(char), '08b') for char in message])
    
    # Replace the LSB of each pixel with a bit from the message
    for i in range(len(message)):
        flat_plane[i+1] = (flat_plane[i+1] & ~1) | int(message[i]) # Set LSB to message[i]
    
    # Reshape back to original dimensions
    return flat_plane.reshape(plane.shape)
def get_message_in_plane(plane):
    # Flatten the 2D plane into a 1D array
    flat_plane = plane.flatten()

    
    # Initialize an empty list to store the binary bits of the message
    binary_message = []

    message_len = flat_plane[0] *8
    # Extract LSBs from the flattened plane to form the binary message
    for i in range(1, message_len+1):  # As message length is stored in the first pixel, we use this to determine how many pixels to read
        # Extract LSB using bitwise AND operation
        binary_message.append(str(flat_plane[i] & 1))  # Extract the LSB and convert to string
    
    # Convert the binary message to a string (byte by byte)
    message = ''.join(binary_message)

    # Convert binary message to ASCII text
    decoded_message = ''.join([chr(int(message[i:i+8], 2)) for i in range(0, len(message), 8)])

    return decoded_message
def Hide():
    message = text1.get(1.0,END)
    

   
    # Convert PIL image to a NumPy array (in RGB format)
    img_np = np.array(img_pil)

    # Convert the RGB image to BGR format (because OpenCV uses BGR by default)
    img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    # splits the image into its individual colour channels where b,g and r are 2d arrays
    b,g,r = cv2.split(img_cv)
     # Replace the LSBs in the blue channel with the binary message
    new_b = hide_message_in_plane(b, message)
    
    # Reconstruct the image with the modified blue channel
    img_with_message = cv2.merge([new_b, g, r])
    cv2.imwrite(filename[:len(filename)-3]+ "hidden.png", img_with_message)
def Show():
    # Convert PIL image to a NumPy array (in RGB format)
    img_np = np.array(img_pil)
    
    # Convert the RGB image to BGR format (because OpenCV uses BGR by default)
    img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    # splits the imag into its individual colour channels where b,g and r are 2d arrays
    b,g,r = cv2.split(img_cv)

    decoded_message = get_message_in_plane(b)
    text1.insert(END,decoded_message)
def save():
    print("")
#logo
logo = PhotoImage(file="logo.png")
Label(root,image=logo,bg="#fefae0").place(x=10,y=0)

Label(root,text="Steganography tool",bg = "#fefae0",fg="black",font="Arial 25 bold").place(x=100,y=20)
#first frame
f = Frame(root,bd=3,bg="#a3b18a",width=340,height=280,relief = GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg="#a3b18a")
lbl.place(x=40,y=10)

#second frame
frame2=Frame(root,bd=3,width=340,height=280,bg="#588157",relief =GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Robote 20",bg="#588157",fg="black",relief = GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#third frame
frame3 = Frame(root,bd=3,bg="#3a5a40",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="Open Image",width=10,height=2,font="Arial 14 bold",command=showimage).place(x=20,y=20)
Button(frame3,text="Save Image",width=10,height=2,font="Arial 14 bold",command=save).place(x=180,y=20)

#fourth frame
frame4 = Frame(root,bd=3,bg="#3a5a40",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="Hide Data",width=10,height=2,font="Arial 14 bold",command=Hide).place(x=20,y=20)
Button(frame4,text="Show Data",width=10,height=2,font="Arial 14 bold",command=Show).place(x=180,y=20)
root.mainloop()

