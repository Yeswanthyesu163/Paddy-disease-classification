from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import shutil
import test




class Root(Tk):
 def __init__(self):
  super(Root,self).__init__()
  self.title("Cassava Disease Classification")
  self.minsize(800,600)
  self.wm_iconbitmap('icon1.ico')
  self.configure(background='#eceaf9')
  self.labelFrame=ttk.LabelFrame(self, text="Select an Image/Folder:")
  self.labelFrame.grid(column=0, row=0, padx=40, pady=20)
  self.button()
  self.button1()
  self.button2()
  self.button3()




 def button(self):
  self.button = ttk.Button(self.labelFrame, text="Browse an image", command=self.fileDialog)
  self.button.grid(column=2, row=0, columnspan = 100, padx=200, pady=5)

 def button1(self):
  self.button1 = ttk.Button(self.labelFrame, text="FIND", command=self.classify)
  self.button1.grid(column=0, row=2, padx=40, pady=20)

 def button2(self):
  self.button2 = ttk.Button(self.labelFrame, text="RESET", command=self.clearLabels)
  self.button2.grid(column=2, row=2, padx=200, pady=50)

 def button3(self):
  self.button3 = ttk.Button(self.labelFrame, text=" Browse a Folder ", command = self.Browse)
  self.button3.grid(column=2, row=1, columnspan = 100, padx=200, pady=5)


 def classify(self):
  result=[]
  result = test.main()
  result = test.folder(self.filename1)
  if result==0:
   global label3
   label3=ttk.Label(self.labelFrame,text=" NO .JPG or .JPEG FILE FOUND/ FOLDER FOUND !", font='times 12 ', foreground='red')
   label3.grid(column=0, row=6)
   return




 def fileDialog(self):
  self.filename = filedialog.askopenfilename(initialdir="/", title="Select Image", filetype=(("jpeg", "*.jpg"), ("All Files", "*.*")))
  global label
  label = ttk.Label(self.labelFrame, text="")
  label.grid(column=0, row=0)
  label.configure(text=self.filename, font='times 14 italic', foreground='#d2691e')
  if not (self.filename.lower().endswith(".jpg") or self.filename.lower().endswith(".jpeg")):
   global label3
   label3=ttk.Label(self.labelFrame, text=" NO .JPG or .JPEG FILE FOUND !", font='times 12', foreground='red')
   label3.grid(column=0, row=8)
   return
  dir=os.getcwd() + "\\test_images"
  for files in os.listdir(dir):
    os.remove(dir + '/' + files)
  if os.path.exists(self.filename):
    shutil.copy(self.filename,dir)
  else:
    global label1
    label1=ttk.Label(root, text="FILE NOT FOUND!", font='times 12 ', foreground='red')
    label1.grid(column=0, row=4)




 def Browse(self):
   self.filename1 = filedialog.askdirectory(title="Select Folder")
   global label9
   label9 = ttk.Label(self.labelFrame, text="")
   label9.grid(column=0, row=1)
   label9.configure(text=self.filename1, font='times 14 italic', foreground='#d2691e')
   if not (os.path.exists(self.filename1)):
    global label10
    label10=ttk.Label(self.labelFrame, text="         NO FOLDER FOUND!        ", font='times 12', foreground='red')
    label10.grid(column=0, row=8)
    return



 def clearLabels(self):
  self.clearLabels1()
  self.clearLabels2()
  dir=os.getcwd() + "\\test_images"
  for files in os.listdir(dir):
    os.remove(dir + '/' + files)
  event_dir = os.getcwd()
  for files in os.listdir(event_dir):
     if files.startswith("events"):
         os.remove(files)


 def clearLabels1(self):
  try:
   if ((label.winfo_exists()==1) or label1.winfo_exists()==1 or label3.winfo_exists()==1):
    label.grid_forget()
    label3.grid_forget()
    label1.grid_forget()
  except:
   return
 def clearLabels2(self):
  try:
   if(label9.winfo_exists()==1 or label10.winfo_exists()==1):
    label9.grid_forget()
    label10.grid_forget()
  except:
   return


if __name__=='__main__':
 dir=os.getcwd() + "\\test_images"
 for files in os.listdir(dir):
   os.remove(dir + '/' + files)
 event_dir = os.getcwd()
 for files in os.listdir(event_dir):
     if files.startswith("events"):
         os.remove(files)
 root=Root()
 root.mainloop()


