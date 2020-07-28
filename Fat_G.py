import sys, textwrap
from tkinter import *  #loads everything from tk inter 
from tkinter import filedialog # loads dialog box
import tkinter as tk

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageTk  
except ImportError:
    print("Please install Pillow from: the web")
    
    sys.exit(1)


########## set headline ########## 

MHDL = 'MAIN HEADLINE' # MHDL = MAINHEADLINE
MHDLSPL = textwrap.wrap(MHDL, width=16) #MHDLSPL MAINHEADLINE SPLIT- > to split after 16 chars

########## set sub headline ########## 

SHDL = 'SUB HEADLINE' #SDHL = SUBHEADLINE
SHDLSPL = textwrap.wrap(SHDL, width=32) #SHDLSPL SUBHEADLINE SPLIT -> to split after 32 chars 

########## set size in a way i am able to change sizes later on, color profile including transparency, set background color ########## 

#image size, colorspace, color, transparency
XMAX, YMAX = 1000, 1000 # image size 
BIM = Image.new('RGBA', (XMAX, YMAX), (255, 255, 255, 255)) # BIM -> BACKGROUND IMAGE -> RGBA R,G,B,A  A=Visibility 0 = translucent 255 = opaque
draw = ImageDraw.Draw(BIM)

########## set fonts to use (maby use windows system delivered fonts so i have not to include them) ########## 

#font and font sitze for Main Headline
MHDLfont = ImageFont.truetype( 
    'openSans-Semibold.ttf', 100)

#font and font sitze for Sub Headline
SHDLfont = ImageFont.truetype( 
    'openSans-Semibold.ttf', 50)

########## set text positions on image  ########## 

#position Main Headline to 50% of image calculated from the top, font color #stolen from stack overflow an mondified to work seem overcomplicated but i did not finde something other
current_h, pad = (XMAX/100*40), 0
for line in MHDLSPL:
    w, h = draw.textsize(line, font=MHDLfont)
    draw.text(((XMAX - w) / 2, current_h), line, font=MHDLfont, fill="black")
    current_h += h + pad

#position Sub Headline to 75% of image calculated from the top, font color
current_h, pad = (XMAX/100*65), 0
for line2 in SHDLSPL:
    w, h = draw.textsize(line2, font=SHDLfont)
    draw.text(((XMAX - w) / 2, current_h), line2, font=SHDLfont, fill="black")
    current_h += h + pad

########## load logo images  ########## 

#load logo images
im1 = Image.open('01.png')
im2 = Image.open('02.png')
im3 = Image.open('03.png')
im4 = Image.open('04.png')


########## resize log image based on backgroudn size si later on i am able to generate different sizes ########## 

#resize images to Xand Y to 25% of Thumbnail size, better use some images in 1:1 ratio giiirrrlllll if not expect "pixelgulasch"
#im1
resizedImage = im1.resize((round(BIM.size[0]*.25), round(BIM.size[1]*.25))).save("img_01_rezised.png")
#im2
resizedImage = im2.resize((round(BIM.size[0]*.25), round(BIM.size[1]*.25))).save("img_02_rezised.png")
#im3
resizedImage = im3.resize((round(BIM.size[0]*.25), round(BIM.size[1]*.25))).save("img_03_rezised.png")
#im4
resizedImage = im4.resize((round(BIM.size[0]*.25), round(BIM.size[1]*.25))).save("img_04_rezised.png")

########## close loaded image files ########## 

#Close original images
im1.close
im2.close
im3.close
im4.close

########## open modified image files ########## 

#Load rezized logo images 
rim1 = Image.open('img_01_rezised.png')
rim2 = Image.open('img_02_rezised.png')
rim3 = Image.open('img_03_rezised.png')
rim4 = Image.open('img_04_rezised.png')


########## put logo files on background  ########## 

#add logo image to background, use them as mask i think it uses the alphachannel to do so = transparent background, position thmen based on file dimensions, still have to figure out what happens if non transparent images are used
BIM = BIM.copy()
XPOS = (XMAX//100) #to position logos based on image dimensions
BIM.paste(rim1, (0, 50), rim1) #pos = top left corner of background image
BIM.paste(rim2, ((XPOS*25), 50), rim2) #pos = 25% of background dimension
BIM.paste(rim3, ((XPOS*50), 50), rim3) #pos = 50% of background dimension
BIM.paste(rim4, ((XPOS*75), 50), rim4) #pos = 75% of background dimension

########## save backgroudn with image on top as a new image ########## 

BIM.save('genrated_test.png')
#BIM.show()

######################################################################################################
########## the gui stuf  ########## 
######################################################################################################

########## open main windows   ########## 
# create a window using tk 
root = Tk() 


########## set backgroudn color to black  ########## 
root.configure(background='#000000') # window color = black


########## set window titel  ########## 
# title
root.title("FAT G") # window titel 

########## set windows size  ########## 
# window size
root.geometry("1500x1000") # this needs to be changed, its to big for small screens 
#image size in window schould be the same even if user has option to change out put resolution of image

########## make Window not resizable ########## 
root.resizable(width = False, height = False) 

########## open genrated image and show it in gui  ########## 
Loadlogo001=Button(root, text="Load image", command = root.destroy)
Loadlogo001.grid(row=0, column=1, sticky=NW, padx=200, pady=100) 

#open filename # notwirking needs a button
def openfilename(): 

	# open file dialog box to select image 
	filename = filedialog.askopenfilename(title ='"pen') 
	return filename 

 # loading the image 
img = ImageTk.PhotoImage(Image.open("genrated_test.png")) 
  
# reading the image 
panel = tk.Label(root, image = img) 
  
# setting the application 
panel.grid(column=0, row=0, ipadx=0, pady=0, sticky=tk.W) 

########## button to close program/window  ########## 
CloseWindow=Button(root, text="KiLL that FATG", command = root.destroy)
CloseWindow.grid(row=0, column=1, sticky=S, padx=200, pady=100)          

root.mainloop() 