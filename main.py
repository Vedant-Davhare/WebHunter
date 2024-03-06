import tkinter.messagebox
from tkinter import *
from PIL import Image, ImageTk
from ph_no import PhoneNumber
from emailAddress import Email
from ip import Ip
from help import Help
from about import About


class webhunter:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x800+0+0")
        self.root.title("Web Hunter")

        # bg image
        img3 = Image.open(r"college_images\mainBG.jpg")
        img3 = img3.resize((1600, 800), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1600, height=800)
        tkinter.messagebox.showinfo("Alert", "Respect Other Privacy")

        # mobile number
        img4 = Image.open(r"college_images\phone.jpg")
        img4 = img4.resize((150, 100), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.ph_no)
        b1.place(x=160, y=340, width=150, height=100)

        # b1 = Button(bg_img, text="Phone Number", cursor="hand2", font=("times new roman", 10, "bold"), bg="darkblue",
        #             fg="white", command=self.ph_no)
        # b1.place(x=100, y=240, width=150, height=30)
        #
        # email button
        img5 = Image.open(r"college_images\email.jpg")
        img5 = img5.resize((150, 100), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.emailAdd)
        b1.place(x=650, y=340, width=150, height=100)
        #
        # b1 = Button(bg_img, text="Email", cursor="hand2", font=("times new roman", 10, "bold"), bg="darkblue",
        #             fg="white", command=self.emailAdd)
        # b1.place(x=400, y=240, width=150, height=30)
        #
        # ip button
        img6 = Image.open(r"college_images\ipadd.jpg")
        img6 = img6.resize((150, 100), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.ip)
        b1.place(x=1090, y=340, width=150, height=100)

        # b1 = Button(bg_img, text="Ip Address", cursor="hand2", font=("times new roman", 10, "bold"), bg="darkblue",
        #             fg="white", command=self.ip)
        # b1.place(x=700, y=240, width=150, height=30)
        #

        # About
        img8 = Image.open(r"college_images\about (2).jpg")
        img8 = img8.resize((150, 100), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.about)
        b1.place(x=400, y=600, width=150, height=100)

        # b1 = Button(bg_img, text="About", cursor="hand2", font=("times new roman", 10, "bold"), bg="darkblue",
        #             fg="white", command=self.about)
        # b1.place(x=1000, y=240, width=150, height=30)


        # Help button
        img7 = Image.open(r"college_images\help (2).jpg")
        img7 = img7.resize((150, 100), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.help)
        b1.place(x=900, y=600, width=150, height=100)

        # b1 = Button(bg_img, text="Help", cursor="hand2", font=("times new roman", 10, "bold"), bg="darkblue",
        #             fg="white", command=self.help)
        # b1.place(x=1000, y=240, width=150, height=30)


        # Exit Button
        img11 = Image.open(r"college_images\exit.jpg")
        img11 = img11.resize((80, 60), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b1.place(x=1400, y=30, width=80, height=60)

        # b1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 10, "bold"), bg="darkblue",
        #             fg="white", command=self.iExit)
        # b1.place(x=1000, y=440, width=150, height=30)

    # =====================================Functions buttos====================+

    def ph_no(self):
        self.new_window = Toplevel(self.root)
        self.app = PhoneNumber(self.new_window)

    #
    def emailAdd(self):
        self.new_window = Toplevel(self.root)
        self.app = Email(self.new_window)

    #
    def ip(self):
        self.new_window = Toplevel(self.root)
        self.app = Ip(self.new_window)

    #
    def help(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    #
    def about(self):
        self.new_window = Toplevel(self.root)
        self.app = About(self.new_window)

    def iExit(self):
        self.exit = tkinter.messagebox.askyesno("Web Hunter", "Are you sure! you want to exit", parent=self.root)
        if self.exit == True:
            self.root.destroy()
        else:
            return False


if __name__ == "__main__":
    root = Tk()
    obj = webhunter(root)
    root.mainloop()
