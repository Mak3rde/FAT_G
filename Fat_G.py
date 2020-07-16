import sys, textwrap
from tkinter import *  #loads everything from tk inter 
from tkinter import filedialog # loads dialog box

import tkinter as tk

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageTk  
except ImportError:
    print("Please install Pillow from: the web")
    
    sys.exit(1)

MHDL = 'MAIN HEADLINE' # MHDL = MAINHEADLINE
MHDLSPL = textwrap.wrap(MHDL, width=16) #MHDLSPL MAINHEADLINE SPLIT- > to split after 16 chars

SHDL = 'SUB HEADLINE' #SDHL = SUBHEADLINE
SHDLSPL = textwrap.wrap(SHDL, width=32) #SHDLSPL SUBHEADLINE SPLIT -> to split after 32 chars 

#defines image size, colorspace, color, transparency
XMAX, YMAX = 1000, 1000 # image size 
BIM = Image.new('RGBA', (XMAX, YMAX), (255, 255, 255, 255)) # BIM -> BACKGROUND IMAGE -> RGBA R,G,B,A  A=Visibility 0 = translucent 255 = opaque
draw = ImageDraw.Draw(BIM)

#defines font and font sitze for Main Headline
MHDLfont = ImageFont.truetype( 
    'openSans-Semibold.ttf', 100)

#defines font and font sitze for Sub Headline
SHDLfont = ImageFont.truetype( 
    'openSans-Semibold.ttf', 50)

#position Main Headline to 50% of image calculated from the top, defines font color
current_h, pad = (XMAX/100*40), 0
for line in MHDLSPL:
    w, h = draw.textsize(line, font=MHDLfont)
    draw.text(((XMAX - w) / 2, current_h), line, font=MHDLfont, fill="black")
    current_h += h + pad

#position Sub Headline to 75% of image calculated from the top, defines font color
current_h, pad = (XMAX/100*65), 0
for line2 in SHDLSPL:
    w, h = draw.textsize(line2, font=SHDLfont)
    draw.text(((XMAX - w) / 2, current_h), line2, font=SHDLfont, fill="black")
    current_h += h + pad


#load logo images
im1 = Image.open('01.png')
im2 = Image.open('02.png')
im3 = Image.open('03.png')
im4 = Image.open('04.png')

#resizue images to Xand Y to 25% of Thumbnail size, better use some images in 1:1 ratio giiirrrlllll
#im1
resizedImage = im1.resize((round(BIM.size[0]*.25), round(BIM.size[1]*.25))).save("img_01_rezised.png")
#im2
resizedImage = im2.resize((round(BIM.size[0]*.25), round(BIM.size[1]*.25))).save("img_02_rezised.png")
#im3
resizedImage = im3.resize((round(BIM.size[0]*.25), round(BIM.size[1]*.25))).save("img_03_rezised.png")
#im4
resizedImage = im4.resize((round(BIM.size[0]*.25), round(BIM.size[1]*.25))).save("img_04_rezised.png")

#Close original images
im1.close
im2.close
im3.close
im4.close

#Load rezized logo images 
rim1 = Image.open('img_01_rezised.png')
rim2 = Image.open('img_02_rezised.png')
rim3 = Image.open('img_03_rezised.png')
rim4 = Image.open('img_04_rezised.png')


#add logo image to background, define them as mask to use transparency, position thmen based on file size
BIM = BIM.copy()
XPOS = (XMAX//100) #to position logos based on image size
BIM.paste(rim1, (0, 50), rim1) 
BIM.paste(rim2, ((XPOS*25), 50), rim2)
BIM.paste(rim3, ((XPOS*50), 50), rim3)
BIM.paste(rim4, ((XPOS*75), 50), rim4)


BIM.save('genrated_test.png')
#BIM.show()

# create windows 
root = Tk() 

root.configure(background='#000000')

# title
root.title("FAT G") 

# window size
root.geometry("1500x1000") 

# make Window not resizable 
root.resizable(width = False, height = False) 

#defines open image
def open_img(): 
	# Select the Imagename from a folder 
	x = openfilename() 

	# opens the image 
	img = Image.open(x) 
	
	# resize the image and apply a high-quality down sampling filter 
	#img = img.resize((250, 250), Image.ANTIALIAS) 

	# PhotoImage class is used to add image to widgets, icons etc 
	img = ImageTk.PhotoImage(img) 

	# create a label 
	panel = Label(root, image = img) 
	
	# set the image as img 
	panel.image = img 
	panel.grid(row = 2) 

#defines open filename
def openfilename(): 

	# open file dialog box to select image 
	# The dialogue box has a title "Open" 
	filename = filedialog.askopenfilename(title ='"pen') 
	return filename 


 # loading the image 
img = ImageTk.PhotoImage(Image.open("genrated_test.png")) 
  
# reading the image 
panel = tk.Label(root, image = img) 
  
# setting the application 
panel.grid(column=0, row=0, ipadx=0, pady=0, sticky=tk.W) 

CloseWindow=Button(root, text="KiLL that FATG", command = root.destroy)
CloseWindow.grid(row=0, column=1, sticky=S, padx=200, pady=100)          

root.mainloop() 