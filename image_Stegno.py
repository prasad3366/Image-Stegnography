from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import  os

class IMG_Stegno:
    output_image_size = 0

    def main(self, root):
        root.title('Image Steganography Project')
        root.geometry('600x600')
        root.resizable(width =False, height=False)
        frame = Frame(root)
        frame.grid()
        frame.place(relx=.5, rely=.5, anchor="center")
        title = Label(frame,text='Image Steganography')
        title.config(font=('Times new roman',18, 'bold'))
        title.grid(pady=10)
        title.grid(row=1)

        encode = Button(frame,text="Encode",command= lambda :self.encode_frame1(frame), padx=14,bg = '#e3f4f1' )
        encode.config(font=('Arial Black',14,'bold'), bg='#586EE8',fg='#FFFFFF')
        encode.grid(row=2)
        decode = Button(frame, text="Decode",command=lambda :self.decode_frame1(frame), padx=14,bg = '#e3f4f1')
        decode.config(font=('Arial Black',14,'bold'), bg='#586EE8',fg='#FFFFFF')
        decode.grid(pady = 12)
        decode.grid(row=3)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

    def back(self,frame):
        frame.destroy()
        self.main(root)

    def encode_frame1(self,F):
        F.destroy()
        F2 = Frame(root)
        F2.grid()
        F2.place(relx=.5, rely=.5, anchor="center")
        label1= Label(F2,text='Select The Image In Which You Want To Hide Text :')
        label1.config(font=('Times new roman',18, 'bold'))
        label1.grid()
        button_bws = Button(F2,text='Select',command=lambda : self.encode_frame2(F2))
        button_bws.config(font=('Arial Black',14,'bold'), bg='#586EE8',fg='#FFFFFF')
        button_bws.grid()
        button_back = Button(F2, text='Cancel', command=lambda : IMG_Stegno.back(self,F2))
        button_back.config(font=('Arial Black',14,'bold'),bg='#586EE8',fg='#FFFFFF')
        button_back.grid(pady=15)
        button_back.grid()

    def decode_frame1(self,F):
        F.destroy()
        d_f2 = Frame(root)
        d_f2.grid()
        d_f2.place(relx=.5, rely=.5, anchor="center")
        label1 = Label(d_f2, text='Select Image with Hidden text:')
        label1.config(font=('Times new roman',18,'bold'))
        label1.grid()
        button_bws = Button(d_f2, text='Select', command=lambda :self.decode_frame2(d_f2))
        button_bws.config(font=('Arial Black',14,'bold'), bg='#586EE8',fg='#FFFFFF')
        button_bws.grid()
        button_back = Button(d_f2, text='Cancel', command=lambda : IMG_Stegno.back(self,d_f2))
        button_back.config(font=('Arial Black',14,'bold'), bg='#586EE8',fg='#FFFFFF')
        button_back.grid(pady=15)
        button_back.grid()

    def encode_frame2(self,e_F2):
        e_pg= Frame(root)
        e_pg.grid()
        e_pg.place(relx=.5, rely=.5, anchor="center")
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            my_img = Image.open(myfile)
            new_image = my_img.resize((300,200))
            img = ImageTk.PhotoImage(new_image)
            label3= Label(e_pg,text='Selected Image')
            label3.config(font=('Times new roman',14,'bold'))
            label3.grid()
            board = Label(e_pg, image=img)
            board.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = my_img.size
            board.grid()
            label2 = Label(e_pg, text='Enter the message')
            label2.config(font=('Times New Roman',18,'bold'))
            label2.grid(pady=15)
            text_a = Text(e_pg, width=50, height=10)
            text_a.grid()
            encode_button = Button(e_pg, text='Cancel', command=lambda : IMG_Stegno.back(self,e_pg))
            encode_button.config(font=('Arial Black',14,'bold'), bg='#586EE8',fg='#FFFFFF')
            data = text_a.get("1.0", "end-1c")
            button_back = Button(e_pg, text='Encode', command=lambda : [self.enc_fun(text_a,my_img),IMG_Stegno.back(self,e_pg)])
            button_back.config(font=('Arial Black',14,'bold'), bg='#586EE8',fg='#FFFFFF')
            button_back.grid(pady=15)
            encode_button.grid()
            e_pg.grid(row=1)
            e_F2.destroy()

    def decode_frame2(self,d_F2):
        d_F3 = Frame(root)
        d_F3.grid(row=1)
        d_F3.place(relx=.5, rely=.5, anchor="center")
        myfiles = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfiles:
            messagebox.showerror("Error","You have selected nothing! ")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(my_image)
            label4= Label(d_F3,text='Selected Image :')
            label4.config(font=('Times New Roman',14,'bold'))
            label4.grid()
            board = Label(d_F3, image=img)
            board.image = img
            board.grid()
            hidden_data = self.decode(my_img)
            label2 = Label(d_F3, text='Hidden data is :')
            label2.config(font=('Times New Roman',14,'bold'))
            label2.grid(pady=10)
            text_a = Text(d_F3, width=50, height=10)
            text_a.insert(INSERT, hidden_data)
            text_a.configure(state='disabled')
            text_a.grid()
            button_back = Button(d_F3, text='Main Menu', command= lambda :self.frame_3(d_F3))
            button_back.config(font=('Arial Black',14,'bold'),bg='#586EE8',fg='#FFFFFF')
            button_back.grid(pady=15)
            button_back.grid()
            d_F2.destroy()

    def decode(self, image):
        image_data = iter(image.getdata())
        data = ''

        while (True):
            pixels = [value for value in image_data.__next__()[:3] +
                      image_data.__next__()[:3] +
                      image_data.__next__()[:3]]
            binary_str = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_str += '0'
                else:
                    binary_str += '1'

            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0:
                return data

    def generate_Data(self,data):
        new_data = []

        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data

    def modify_Pix(self,pix, data):
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)
        for i in range(dataLen):
            # Extracting 3 pixels at a time
            pix = [value for value in imgData.__next__()[:3] +
                   imgData.__next__()[:3] +
                   imgData.__next__()[:3]]
            
            for j in range(0, 8):
                if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
                    if (pix[j] % 2 != 0):
                        pix[j] -= 1

                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            
            if (i == dataLen - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]
    
    def encode_enc(self,newImg, data):
        w = newImg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modify_Pix(newImg.getdata(), data):

            # Putting modified pixels in the new image
            newImg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def enc_fun(self,text_a,myImg):
        data = text_a.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert","Kindly enter text in TextBox")
        else:
            newImg = myImg.copy()
            self.encode_enc(newImg, data)
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myImg.filename))[0]
            newImg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newImg.size
            messagebox.showinfo("Success","Encoding Successful")

    def frame_3(self,frame):
        frame.destroy()
        self.main(root)


root = Tk() #GUILOOP
o = IMG_Stegno()
o.main(root)
root.mainloop()