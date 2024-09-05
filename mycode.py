from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile
root = Tk()
root.title("Image Processing app")
root.geometry('800x400')
def open_file():
    file = askopenfile(mode ='r', filetypes
    =[('Image Files', '*.jpg')])
    print(file)
    if file is not None:
        content = file.name
        print(content)
        file = open('geek.txt', 'w')
        file.write(content)
        file.close()

def openProgram():
    import cv2
    # importing haar file through cascade classifier
    face_cascade = cv2.CascadeClassifier("haarf1.xml")
    face_cascade1 = cv2.CascadeClassifier("haare2.xml")

    #file database of the current file in read mode
    file = open("geek.txt", "r")
    content = file.read()
    img1 = cv2.imread(content)
    file.close()

    # conversion into grayscale image
    fimg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    # using cascade classifier block of ML for face haar file with scale factor of 15 % decrement
    facess = fac e_cascade.detectMultiScale(fimg, scaleFactor=1.15, minNeighbors=5)

    # using cascade classifier block of ML for eye haar file with scale factor of 10 % decrement
    fac = face_cascade1.detectMultiScale(fimg, scaleFactor=1.13, minNeighbors=20)

    # importing open cv for code vision
    print("face matrix ", facess)

    # importing open cv for code vision
    print("eye matrix ", fac)

    # searching for corners of the face through data
    for x, y, w, h in facess: img1 = cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # searching for corners of the eyes through data
    for x, y, w, h in fac: img1 = cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # resizing the image to fit in the running window
    resizedface = cv2.resize(img1, (int(img1.shape[1] / 2), int(img1.shape[0] / 2)))

    # displaying the image with face and eyes block
    cv2.imshow('Gray', resizedface)

    # after key is pressed the image will exit
    cv2.waitKey(0)

    # cleaning all windos after button is pressed
    cv2.destroyWindow("Gray")

    #labelling gui contnets that will be shown
    w = Label(root, text=' ', font=("Helvetica", 33))
    w.pack()

    w = Label(root, text='Firstly Press to Select Image', font=("Helvetica", 13))
    w.pack()

    #labelling gui buttons that will be shown
    btn = Button(root, text ='Open', command = lambda:open_file())
    btn.pack(side = TOP, pady = 10)

    w = Label(root, text='Secondaly Press to Detect', font=("Helvetica", 13))
    w.pack()

    mbutton = Button(text = "Go", command = openProgram).pack()
    btn.pack(side=TOP, pady=10)

    w = Label(root, text=' ', font=("Helvetica", 73))
    w.pack()

    w = Label(root, text='Image Detection App',
    font=("Helvetica", 56))
    w.pack()

    # images in the gui
    load = Image.open("v9.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.place(x=0, y=0)
    #closing and finishing the gui layout
    mainloop()