from tkinter import *
print('''
-------------------------------------------------------------------------------------------------------------------
1R.jpg - это промежуточный файл, если вы изменили фото, а при его обновлении ничего не поменялось,
то в списке выберите 1R.jpg
Два поля ввода под update image это размер изображения в пикселях в порядке - ширина, высота
Если при попытке разместить изображение появляется ошибка, проверьте, заданы ли параметры контраста, резкости,
яркости, высота, ширина, поворот!
Если у вас слабый компьютер, то многие действия, по типу to grey, будут длиться довольно долго,
в консоли выводится прогресс выполнения, в конце окно уведомит вас о завершении действия
После сохранения файла с изменёнными контрастом, резкостью, яркостью, поворотом
рекомендуется сбросить все эти настройки до стандартных значений
Стандартные значения:
rotate - 0
Contrast - 1
Brightness - 1
Sharpness - 1
При "Save as" писать расширение не надо, расширения предопределено - .jpg
Если ваш сохранённый файл не показывается,
то обновите список доступных файлов "Update dir of files"
Это самый первый релиз программы, далее она будет обновляться
Мой discord для связи - sania212
-------------------------------------------------------------------------------------------------------------------
''')
import os
import numpy as np
from tkinter import Menu, messagebox
from tkinter.ttk import Combobox
from PIL import Image,ImageTk,ImageEnhance,ImageFilter
import os
from tqdm import tqdm
import githubdl
#Updater V3, credit to: (discord) sania212"
print("Updater V3, credit to: (discord) sania212")
window = Tk()
window["bg"] = "black"
window.title("PythonShop")
window.geometry('1000x700')
try:
    githubdl.dl_file("https://github.com/HOMENYK/Redactor-python-", "Main.exe", "Main_temp.exe", github_token="...")
except:
    print("Bad internet connection")
print("Checking for updates, please wait...")
Mfile = open("Main.exe", "rb")
Current_code = Mfile.read()
Mfile.close()
Mfile2 = open("Main_temp.exe", "rb")
Git_code = Mfile2.read()
Mfile2.close()
if(Git_code == Current_code):
    print("Your version already up to date")
else:
    if(str(input("Update found, are you want to install update? (T or F): ")) == "T"):
        os.system("AutoUpdate.exe")
        window.destroy
    else:
        pass
def Saved():
    lbl2=Label(window, text='Saved!', font=('Arial Bold', 8, ), bg='grey',fg='white')
    lbl2.place(x=70,y=25)
    lbl2.after(1000, lambda: DeleteText(lbl2))
def quad_as_rect(quad):
    if quad[0] != quad[2]: return False
    if quad[1] != quad[7]: return False
    if quad[4] != quad[6]: return False
    if quad[3] != quad[5]: return False
    return True
def quad_to_rect(quad):
    assert(len(quad) == 8)
    assert(quad_as_rect(quad))
    return (quad[0], quad[1], quad[4], quad[3])
def rect_to_quad(rect):
    assert(len(rect) == 4)
    return (rect[0], rect[1], rect[0], rect[3], rect[2], rect[3], rect[2], rect[1])
def shape_to_rect(shape):
    assert(len(shape) == 2)
    return (0, 0, shape[0], shape[1])
def griddify(rect, w_div, h_div):
    w = rect[2] - rect[0]
    h = rect[3] - rect[1]
    x_step = w / float(w_div)
    y_step = h / float(h_div)
    y = rect[1]
    grid_vertex_matrix = []
    for _ in range(h_div + 1):
        grid_vertex_matrix.append([])
        x = rect[0]
        for _ in range(w_div + 1):
            grid_vertex_matrix[-1].append([int(x), int(y)])
            x += x_step
        y += y_step
    grid = np.array(grid_vertex_matrix)
    return grid
def distort_grid(org_grid, max_shift):
    new_grid = np.copy(org_grid)
    x_min = np.min(new_grid[:, :, 0])
    y_min = np.min(new_grid[:, :, 1])
    x_max = np.max(new_grid[:, :, 0])
    y_max = np.max(new_grid[:, :, 1])
    new_grid += np.random.randint(- max_shift, max_shift + 1, new_grid.shape)
    new_grid[:, :, 0] = np.maximum(x_min, new_grid[:, :, 0])
    new_grid[:, :, 1] = np.maximum(y_min, new_grid[:, :, 1])
    new_grid[:, :, 0] = np.minimum(x_max, new_grid[:, :, 0])
    new_grid[:, :, 1] = np.minimum(y_max, new_grid[:, :, 1])
    return new_grid
def grid_to_mesh(src_grid, dst_grid):
    assert(src_grid.shape == dst_grid.shape)
    mesh = []
    for i in range(src_grid.shape[0] - 1):
        for j in range(src_grid.shape[1] - 1):
            src_quad = [src_grid[i    , j    , 0], src_grid[i    , j    , 1],
                        src_grid[i + 1, j    , 0], src_grid[i + 1, j    , 1],
                        src_grid[i + 1, j + 1, 0], src_grid[i + 1, j + 1, 1],
                        src_grid[i    , j + 1, 0], src_grid[i    , j + 1, 1]]
            dst_quad = [dst_grid[i    , j    , 0], dst_grid[i    , j    , 1],
                        dst_grid[i + 1, j    , 0], dst_grid[i + 1, j    , 1],
                        dst_grid[i + 1, j + 1, 0], dst_grid[i + 1, j + 1, 1],
                        dst_grid[i    , j + 1, 0], dst_grid[i    , j + 1, 1]]
            dst_rect = quad_to_rect(dst_quad)
            mesh.append([dst_rect, src_quad])
    return mesh
def FT(image4):
    flipped_image=image.transpose(Image.FLIP_TOP_BOTTOM)
    flipped_image.save(os.getcwd()+"\\Photo\\1R.jpg")
    Saved()
def FLR(image4):
    flipped_image=image.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_image.save(os.getcwd()+"\\Photo\\1R.jpg")
    Saved()
def Height_r():
    try:
        Height_T = height.get()
        return Height_T
    except:
        Error()
def Weight_r():
    try:
        Wight_T = wight.get()
        return Wight_T
    except:
        Error()
def Factor():
    try:
        Factor_R = float(factor.get())
        return Factor_R
    except:
        Error()
def Sharpness_F():
    try:
        Factor_S = float(factor_s.get())
        return Factor_S
    except:
        Error()
def factor_B():
    try:
        Factor_B = float(factor_b.get())
        return Factor_B
    except:
        Error()
def factor_S1():
    try:
        Factor_S2 = float(factor_s2.get())
        return Factor_S2
    except:
        Error()
def Complete():
    lbl2=Label(window, text='Complete!', font=('Arial Bold', 8, ), bg='grey',fg='white')
    lbl2.place(x=70,y=25)
    lbl2.after(1000, lambda: DeleteText(lbl2))
def Error():
    lbl2=Label(window, text='Error!', font=('Arial Bold', 8, ), bg='grey',fg='white')
    lbl2.place(x=70,y=25)
    lbl2.after(1000, lambda: DeleteText(lbl2))
def EnterRG():
    rg=rotate.get()
    if rg == '' or int(rg)>360:
        Error()
    else:
        return rg
def DeleteText(lbl2):
    lbl2.destroy()
def placePhoto(photo_n):
    try:
        Factor_R = Factor()
        Factor_S = Sharpness_F()
        Factor_B = factor_B()
        Factor_S2 = factor_S1()
        height = Height_r()
        wight = Weight_r()
        global image
        global image2
        global image3
        global image4
        global image5
        destroyPhoto()
        nrg = EnterRG()
        Path=photo_n.get()
        image = Image.open("Photo\\" + Path)
        image = image.rotate(int(nrg), expand=True)
        image = image.resize((int(height), int(wight)))
        enc = Constrast(image)
        image2 = enc.enhance(Factor_R)
        enc2 = Sharpness(image2)
        image3 = enc2.enhance(Factor_S2)
        enc3 = Brightness(image3)
        image4 = enc3.enhance(Factor_B)
        enc4 = Colour_B(image4)
        image5 = enc4.enhance(Factor_S)
        photo = ImageTk.PhotoImage(image5)
        Img.configure(image=photo)
        Img.image=photo
        return image, image2, image3, image4, image5
    except:
        Error()
def rgd_to_grey(image4):
    try:
        ht = Height_r()
        w = Weight_r()
        h = int(ht) - 1
        img = image4
        img = img.convert("RGB")
        xs = 0
        ys = 0
        r = int(h)*int(w)
        for i in tqdm(range(r)):
            pixelRGB = img.getpixel((xs,ys))
            R,G,B = pixelRGB
            brightness = int(sum([R,G,B])/3)
            img.putpixel((xs,ys), (brightness, brightness, brightness))
            xs=xs+1
            if xs == h:
                xs=0
                ys=ys+1
        img.save(os.getcwd()+"\\Photo\\1R.jpg")
        Complete()
    except:
        Error()
def destroyPhoto():
    try:
        Img.configure(image=None)
        Img.image = None
    except:
        Error()
def Save():
    try:
        image.save(os.getcwd()+"\\Photo\\Save.jpg")
        Saved()
    except:
        Error()
def Save_as(image):
    try:
        window2 = Tk()
        window2.title("Диалоговое окно")
        window2.geometry('100x70')
        labl = Label(window2, text="Имя файла:", font=('Arial Bold', 10))
        labl.place(x=20,y=5)
        Name = Entry(window2, width=10)
        Name.place(x=25,y=25)
        btn5 = Button(window2, text="Принять", command=lambda:destroyWin(window2,Name,image))
        btn5.place(x=27,y=45)
    except:
        Error()
def Take_Name(Name,image):
    Name_F=Name.get()
    image.save(os.getcwd()+"\\Photo\\"+Name_F+".jpg")
def destroyWin(window2,Name,image):
    Take_Name(Name,image)
    window2.destroy()
    Saved()
def Edit():
    messagebox.showinfo('info', 'В разработке')
def Delete():
    destroyPhoto()
def UdpateDir(photo_n):
    photos=os.listdir(os.getcwd()+"\\Photo")
    photo_n.configure(values=photos)
    return photos
def updateImage(photo_n):
    destroyPhoto()
    placePhoto(photo_n)
def Constrast(image):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer
def Sharpness(image2):
    enhancer2 = ImageEnhance.Sharpness(image2)
    return enhancer2
def Brightness(image3):
    enhancer3 = ImageEnhance.Brightness(image3)
    return enhancer3
def Colour_B(image4):
    enhancer4 = ImageEnhance.Color(image4)
    return enhancer4
def Shmix(im):
    dst_grid = griddify(shape_to_rect(im.size), 4, 4)
    src_grid = distort_grid(dst_grid, 50)
    mesh = grid_to_mesh(src_grid, dst_grid)
    im = im.transform(im.size, Image.MESH, mesh)
    Saved()
    im.save("Photo//1R.jpg")
def Iversion(image4):
    try:
        ht = Height_r()
        w = Weight_r()
        h = int(ht) - 1
        img = image4
        img = img.convert("RGB")
        xs = 0
        ys = 0
        r = int(h)*int(w)
        for i in tqdm(range(r)):
            pixelRGB = img.getpixel((xs,ys))
            R,G,B = pixelRGB
            New_R = 255-R
            New_G = 255-G
            New_B = 255-B
            img.putpixel((xs,ys), (New_R, New_G, New_B))
            xs=xs+1
            if xs == h:
                xs=0
                ys=ys+1
        img.save(os.getcwd()+"\\Photo\\1R.jpg")
        Complete()
    except:
        Error()
def OAR(img):
    W = Weight_r()
    H = Height_r()
    size = (int(W),int(H))
    try:
        width, height = img.size
        if width > height:
            ratio = width / size[0]
            new_height = int(height/ratio)
            new_size = (size[0], new_height)
        else:
            ratio = height / size[1]
            new_width = int(width/ratio)
            new_size = (new_width, size[1])
        img.thumbnail(new_size, Image.ANTIALIAS)
        img.save(os.getcwd()+"\\Photo\\1R.jpg")
        Saved()
    except:
        Error()
def FS(photo_n):
    Path=photo_n.get()
    IMG = Image.open("Photo//"+Path)
    size = IMG.size
    wight.delete(0,END)
    height.delete(0,END)
    wight.insert(0, str(size[1]))
    height.insert(0, str(size[0]))
    return size
    Complete()
def destroyWin2(window3,DOUBLE,photo_n,image4):
    Krat = float(DOUBLE.get())
    img = image4
    W1=Weight_r()
    H1=Height_r()
    size = (int(W1),int(H1))
    w = int(size[0]/Krat)
    h = int(size[1]/Krat)
    wight.delete(0,END)
    height.delete(0,END)
    wight.insert(0, str(w))
    height.insert(0, str(h))
    img.resize((w,h))
    img.save(os.getcwd()+"\\Photo\\1R.jpg")
    window3.destroy()
def destroyWin3(window3,DOUBLE,photo_n,image4):
    Krat = float(DOUBLE.get())
    img = image4
    W1=Weight_r()
    H1=Height_r()
    size = (int(W1),int(H1))
    w = int(size[0]*Krat)
    h = int(size[1]*Krat)
    wight.delete(0,END)
    height.delete(0,END)
    wight.insert(0, str(w))
    height.insert(0, str(h))
    img.resize((w,h))
    img.save(os.getcwd()+"\\Photo\\1R.jpg")
    window3.destroy()
def FS_S(photo_n, image4):
    try:
        window9 = Tk()
        window9.title("Диалоговое окно")
        window9.geometry('100x70')
        labl = Label(window9, text="Во сколько раз:", font=('Arial Bold', 10))
        labl.place(x=15,y=5)
        DOUBLE = Entry(window9, width=10)
        DOUBLE.place(x=25,y=25)
        btn5 = Button(window9, text="Принять", command=lambda:destroyWin2(window9,DOUBLE,photo_n,image4))
        btn5.place(x=27,y=45)
    except:
        Error()
def FS_B(photo_n, image4):
    try:
        window8 = Tk()
        window8.title("Диалоговое окно")
        window8.geometry('100x70')
        labl = Label(window8, text="Во сколько раз:", font=('Arial Bold', 10))
        labl.place(x=15,y=5)
        DOUBLE_B = Entry(window8, width=10)
        DOUBLE_B.place(x=25,y=25)
        btn5 = Button(window8, text="Принять", command=lambda:destroyWin3(window8,DOUBLE_B,photo_n,image4))
        btn5.place(x=27,y=45)
    except:
        Error()
def Change_BG(cl):
    if cl=="red": window["bg"] = "red"
    elif cl=="blue": window["bg"] = "blue"
    elif cl=="green": window["bg"] = "green"
    elif cl=="yellow": window["bg"] = "yellow"
    elif cl=="white": window["bg"] = "white"
    elif cl=="black": window["bg"] = "black"
    else:
        Error()
def Background():
    cl_r="red"
    cl_b1="blue"
    cl_g="green"
    cl_y="yellow"
    cl_w="white"
    cl_b2="black"
    window3 = Tk()
    window3.title("Цвет")
    window3.geometry('10x150')
    btn15 = Button(window3, text="red", command=lambda:Change_BG(cl_r))
    btn15.place(x=0,y=0)
    btn16 = Button(window3, text="blue", command=lambda:Change_BG(cl_b1))
    btn16.place(x=0,y=25)
    btn17 = Button(window3, text="green", command=lambda:Change_BG(cl_g))
    btn17.place(x=0,y=50)
    btn19 = Button(window3, text="yellow", command=lambda:Change_BG(cl_y))
    btn19.place(x=0,y=75)
    btn20 = Button(window3, text="white", command=lambda:Change_BG(cl_w))
    btn20.place(x=0,y=100)
    btn21 = Button(window3, text="black", command=lambda:Change_BG(cl_b2))
    btn21.place(x=0,y=125)
def your_Image():
    try:
        window4 = Tk()
        window4.title("Диалоговое окно")
        window4.geometry('100x70')
        labl = Label(window4, text="Имя:", font=('Arial Bold', 10))
        labl.place(x=15,y=5)
        BackName = Entry(window4, width=10)
        BackName.place(x=25,y=25)
        btn5 = Button(window4, text="Принять", command=lambda:delWin(window4, BackName))
        btn5.place(x=27,y=45)
    except:
        Error()
def delWin(win, BackName):
    b_img = Image.open("Background images//"+str(BackName.get())+".jpg")
    print((window.winfo_width(), window.winfo_height()))
    b_img = b_img.resize((window.winfo_width(), window.winfo_height()))
    b_image = ImageTk.PhotoImage(b_img)
    pannel.configure(image=b_image)
    pannel.image = b_image
    win.destroy()
    Complete()
def Colour_of_image(mode,img):
    try:
        if mode == "R":
            ht = Height_r()
            w = Weight_r()
            h = int(ht) - 1
            img = image4
            img = img.convert("RGB")
            xs = 0
            ys = 0
            r = int(h)*int(w)
            for i in tqdm(range(r)):
                pixelRGB = img.getpixel((xs,ys))
                R,G,B = pixelRGB
                G = 0
                B = 0
                img.putpixel((xs,ys),(R,G,B))
                xs+=1
                if xs == h:
                    xs=0
                    ys+=1
        if mode == "G":
            ht = Height_r()
            w = Weight_r()
            h = int(ht) - 1
            img = image4
            img = img.convert("RGB")
            xs = 0
            ys = 0
            r = int(h)*int(w)
            for i in tqdm(range(r)):
                pixelRGB = img.getpixel((xs,ys))
                R,G,B = pixelRGB
                R = 0
                B = 0
                img.putpixel((xs,ys),(R,G,B))
                xs+=1
                if xs == h:
                    xs=0
                    ys+=1
        if mode == "B":
            ht = Height_r()
            w = Weight_r()
            h = int(ht) - 1
            img = image4
            img = img.convert("RGB")
            xs = 0
            ys = 0
            r = int(h)*int(w)
            for i in tqdm(range(r)):
                pixelRGB = img.getpixel((xs,ys))
                R,G,B = pixelRGB
                G = 0
                R = 0
                img.putpixel((xs,ys),(R,G,B))
                xs+=1
                if xs == h:
                    xs=0
                    ys+=1
        Saved()
        img.save(os.getcwd()+"\\Photo\\1R.jpg")
    except:
        Error()
def Thresholding(img):
    try:    
        ht = Height_r()
        w = Weight_r()
        h = int(ht) - 1
        img = image4
        img = img.convert("RGB")
        xs = 0
        ys = 0
        r = int(h)*int(w)
        for i in tqdm(range(r)):
            pixelRGB = img.getpixel((xs,ys))
            R,G,B = pixelRGB
            brightness = int(sum([R,G,B])/3)
            if brightness >=100:
                img.putpixel((xs,ys),(255,255,255))
            elif brightness <100:
                img.putpixel((xs,ys),(0,0,0))
            xs+=1
            if xs == h:
                xs=0
                ys+=1
        Saved()
        img.save(os.getcwd()+"\\Photo\\1R.jpg")
    except:
        Error()
def Edges(img):
    try:
        img_gray = img.convert("L")
        img_edges_pre = img_gray.filter(ImageFilter.SMOOTH)
        img_edges = img_edges_pre.filter(ImageFilter.FIND_EDGES)
        Saved()
        img_edges.save(os.getcwd()+"\\Photo\\1R.jpg")
    except:
        Error()
def Emboss(img):
    try:
        img_gray = img.convert("L")
        img_emboss_pre = img_gray.filter(ImageFilter.SMOOTH)
        img_emboss = img_emboss_pre.filter(ImageFilter.EMBOSS)
        Saved()
        img_emboss.save(os.getcwd()+"\\Photo\\1R.jpg")
    except:
        Error()
def Contour(img):
    try:
        img_gray = img.convert("L")
        threshold = 50
        img_gray = img_gray.point(lambda x: 255 if x > threshold else 0)
        img_contour = img_gray.filter(ImageFilter.CONTOUR)
        Saved()
        img_contour.save(os.getcwd()+"\\Photo\\1R.jpg")
    except:
        Error()
photos = ("Обновите доступные фото")
prev_x=0
prev_y=0
pannel = Label(window)
pannel.place(x=0,y=0)
lbl=Label(window, text='version 0.0.3', font=('Arial Bold', 8, ), bg='grey',fg='white')
lbl.place(x=0,y=0)
btn1=Button(window, text='Exit', font=('Arial Bold', 7), command=window.destroy, bg='grey',fg='white')
btn1.place(x=70,y=0)
photo_n = Combobox(window, values=photos)
photo_n.place(x=0,y=50)
btn2=Button(window, text='Rotate', font=('Arial Bold', 10), command=lambda:EnterRG())
btn2.place(x=0,y=20)
rotate = Entry(window, width=4)
rotate.insert(0, "0")
rotate.place(x=50,y=25)
height = Entry(window, width=3)
height.place(x=0,y=175)
lbl10 = Label(window, text=' <- contrast', font=('Arial Bold', 8, ), bg='grey',fg='white')
lbl10.place(x=30,y=225)
factor = Entry(window, width=3)
factor.insert(0, "1")
factor.place(x=0,y=225)
Img = Label(window)
Img.place(x=170,y=20)
lbl10 = Label(window, text=' <- sharpness', font=('Arial Bold', 8, ), bg='grey',fg='white')
lbl10.place(x=30,y=250)
factor_s2 = Entry(window, width=3)
factor_s2.insert(0, "1")
factor_s2.place(x=0,y=250)
lbl10 = Label(window, text=' <- brightness', font=('Arial Bold', 8, ), bg='grey',fg='white')
lbl10.place(x=30,y=275)
factor_b = Entry(window, width=3)
factor_b.insert(0, "1")
factor_b.place(x=0,y=275)
wight = Entry(window, width=3)
wight.place(x=30,y=175)
btn3 = Button(window, text="place photo", command=lambda:placePhoto(photo_n))
btn3.place(x=0,y=75)
btn4 = Button(window, text="Delete photo", command=destroyPhoto)
btn4.place(x=0,y=100)
btn6 = Button(window, text="Update dir of files", command=lambda:UdpateDir(photo_n))
btn6.place(x=0,y=125)
btn7 = Button(window, text="update image", command=lambda:updateImage(photo_n))
btn7.place(x=0,y=150)
btn8 = Button(window, text="To grey", command=lambda:rgd_to_grey(image5))
btn8.place(x=0,y=200)
btn9 = Button(window, text="Cursed image",command=lambda:Shmix(image5))
btn9.place(x=0,y=300)
btn10 = Button(window, text="Inversion", command=lambda:Iversion(image5))
btn10.place(x=0,y=325)
btn11 = Button(window, text="Flip top",command=lambda:FT(image4))
btn11.place(x=0,y=350)
btn12 = Button(window, text="Flip left to right", command=lambda:FLR(image5))
btn12.place(x=0,y=375)
btn14 = Button(window, text="Full Size", command=lambda:FS(photo_n))
btn14.place(x=0,y=425)
btn13 = Button(window, text="On aspect ratio", state=["disabled"], command=lambda:OAR(image5))
btn13.place(x=0,y=400)
btn16 = Button(window, text="All Red", command=lambda:Colour_of_image("R", image5))
btn16.place(x=0,y=450)
btn17 = Button(window, text="All Green", command=lambda:Colour_of_image("G", image5))
btn17.place(x=0,y=475)
btn18 = Button(window, text="All Blue", command=lambda:Colour_of_image("B", image5))
btn18.place(x=0,y=500)
btn18 = Button(window, text="Thresholding", command=lambda:Thresholding(image5))
btn18.place(x=0,y=550)
btn18 = Button(window, text="Edges", command=lambda:Edges(image5))
btn18.place(x=0,y=575)
btn18 = Button(window, text="Emboss", command=lambda:Emboss(image5))
btn18.place(x=0,y=600)
btn18 = Button(window, text="Contour", command=lambda:Contour(image5))
btn18.place(x=0,y=625)
factor_s = Entry(window, width=3)
factor_s.insert(0, "1")
factor_s.place(x=0,y=525)
lbl20 = Label(window, text=' <- colour ballance', font=('Arial Bold', 8, ), bg='grey',fg='white')
lbl20.place(x=30,y=525)
menu=Menu(window)
new_item = Menu(menu,tearoff=0)
new_item.add_command(label="Save", command=Save)
new_item.add_command(label="Save as", command=lambda:Save_as(image5))
new_item.add_separator()
new_item.add_command(label="Edit (уменьшить)", command=lambda:FS_S(photo_n, image5))
new_item.add_command(label="Edit (увеличить)", command=lambda:FS_B(photo_n, image5))
new_item.add_separator()
new_item.add_command(label="Delete", command=Delete)
menu.add_cascade(label="файл", menu=new_item)
new_item2 = Menu(menu,tearoff=0)
new_item2.add_command(label="Background Colour", command=Background)
new_item2.add_command(label="Background Image", command=your_Image)
new_item2.add_separator()
menu.add_cascade(label="программа", menu=new_item2)
window.config(menu=menu)
UdpateDir(photo_n)
window.mainloop()