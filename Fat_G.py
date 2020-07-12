import sys, textwrap

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
except ImportError:
    print("Please install Pillow from: https://pypi.python.org/pypi/Pillow/3.0.0")
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


#Define logo images by name
im1 = Image.open('01.png')
im2 = Image.open('02.png')
im3 = Image.open('03.png')
im4 = Image.open('04.png')

L01POS = 2, 1


#add logo image to background, define them as mask to use transparency, position thmen based on file size
BIM = BIM.copy()
BIM.paste(im1, ((L01POS), 50), im1)
BIM.paste(im2, (250, 50), im2)
BIM.paste(im3, (500, 50), im3)
BIM.paste(im4, (750, 50), im4)


#BIM.save('test.png')
BIM.show()

#Logo size single image 250x250 = per logo 25% of image width / max 4 logos.