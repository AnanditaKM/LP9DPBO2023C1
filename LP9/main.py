from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from vila import Vila
from tkinter import *
from PIL import ImageTk, Image

hunians = []
hunians.append(Apartemen("Anandita", "apart1.jpg", "Jl. in aja dulu", "21x100 Meter", 2,2,"Televisi, Kulkas, Air Hangat"))
hunians.append(Vila("Kusumah", "vila1.jpg", "Jl. vila", "200x200 m", "Vilaaa", 12, 20))
hunians.append(Rumah("mulyadi","rumah.jpg","jl.melati","200x20",2,2,"mobil 2"))
hunians.append(Indekos("Anan", "dita", "kos.jpg", "Jl. gerlong", "100x100 meter", "Rp1000000"))

root = Tk()
root.title("Latihan DPBO Python")

list_gambar = []

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    img = Image.open("gambar/" + hunians[index].get_gambar())
    img = img.resize((200, 200))
    photo_img = ImageTk.PhotoImage(img)
    list_gambar.append(photo_img)
    img_label = Label(d_frame, image=photo_img)
    img_label.grid(row=0, column=0)

    d_summary = Label(d_frame, text="Summary\n" + str(hunians[index].get_detail()) + str(hunians[index].get_summary()) + "\n" + str(hunians[index].get_dokumen()), anchor="w", justify=LEFT).grid(row=1, column=0, sticky="w")

def main_page():
    label.destroy()
    frameland.destroy()
    img_label.destroy()
    button.destroy()

    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, height=4, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, height=4, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        image = Image.open("gambar/" + h.get_gambar())
        image = image.resize((62, 62))

        photo = ImageTk.PhotoImage(image)
        list_gambar.append(photo)

        image_label = Label(frame, image=photo, borderwidth=1, relief="solid")
        image_label.grid(row=index, column=2)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, height=4, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=3)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, height=4, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=3)

        b_detail = Button(frame, text="Details ", height=3, width=9, command=lambda index=index: details(index))
        b_detail.grid(row=index, column=4)

label = Label(root, text="Pengguna dan Huniannya ", font=('Arial', 16))
label.pack()

img = Image.open("gambar/hunian.jpg")
img = img.resize((200, 200))
photo_img = ImageTk.PhotoImage(img)
list_gambar.append(photo_img)
frameland = Frame(root, padx=10, pady=10)
frameland.pack(padx=10, pady=10)
img_label = Label(frameland, image=photo_img)
img_label.pack()

button = Button(root, text='Main Page', font=('Arial', 8), command=main_page)
button.pack(side=BOTTOM)

root.mainloop()
