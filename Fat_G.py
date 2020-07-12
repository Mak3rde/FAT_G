import sys, textwrap

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    #from resizeimage import resizeimage #not neeed it seems
except ImportError:
    print("Please install Pillow from: https://pypi.org/project/Pillow/#files")
    #print("Please install resize-image from: https://pypi.org/project/python-resize-image/#files") #not needed it seems
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
resizedImage = im1.resize((round(BIM.size[0]*.25), round(BIM.size[1]*.25)))
resizedImage.save("img_01_rezised.png")

#im2
resizedImage = im2.resize((round(BIM.size[0]*.25), round(BIM.size[1]*.25)))
resizedImage.save("img_02_rezised.png")

#im3
resizedImage = im3.resize((round(BIM.size[0]*.25), round(BIM.size[1]*.25)))
resizedImage.save("img_03_rezised.png")

#im4
resizedImage = im4.resize((round(BIM.size[0]*.25), round(BIM.size[1]*.25)))
resizedImage.save("img_04_rezised.png")

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


#BIM.save('genrated_test.png')
BIM.show()

#Logo size single image 250x250 = per logo 25% of image width / max 4 logos.