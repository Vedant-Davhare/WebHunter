from tkinter import *
from PIL import Image, ImageTk
class About:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x800+0+0")
        self.root.title("Web Hunter")

        # bg image
        img3 = Image.open(r"college_images\about.jpg")
        img3 = img3.resize((1520, 800), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1520, height=800)


if __name__ == "__main__":
    root = Tk()
    obj = About(root)
    root.mainloop()
