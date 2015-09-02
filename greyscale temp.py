from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

im = Image.open("kittens.jpg")

def greyscale(im):
    '''changes the image to greyscale'''
    draw = ImageDraw.Draw(im)

    (width, height) = im.size
    for x in range(0, width):
        for y in range (0, height):
            (red, green, blue) = im.getpixel((x,y))
            newRed = int(red * .21 + green * .72 + blue * .07)
            newGreen = int(red * .21 + green * .72 + blue * .07)
            newBlue = int(red * .21 + green * .72 + blue * .07)
            draw.point([(x,y)], (newRed, newGreen, newBlue))
    im.save("catgreyscale.jpg")

def sepia(im):
    """ which calls for writing a pixel function for sepia toning"""
    draw = ImageDraw.Draw(im)

    (width, height) = im.size
    for x in range(0, width):
        for y in range(0, height):
            (red, green, blue) = im.getpixel((x,y))
            newRed = int(red * .393 + green*.769 + blue * .189)
            if newRed > 254:
                newRed = 255
            newGreen = int(red * .349 + green*.686 + blue * .168)
            if newGreen > 254:
                newGreen = 255
            newBlue = int(red * .272 + green*.534 + blue * .131)
            if newBlue > 254:
                newBlue = 255
            draw.point([(x,y)], (newRed, newGreen, newBlue))
    im.save("catsepia.jpg")
            
def invert(im):
    '''changes the image to negative'''
    draw = ImageDraw.Draw(im)

    (width, height) = im.size
    for x in range(0, width):
        for y in range (0, height):
            (red, green, blue) = im.getpixel((x,y))
            newRed = 255 - red
            newGreen = 255 - green
            newBlue = 255 - blue
            draw.point([(x,y)], (newRed, newGreen, newBlue))
    im.save("catinvert.jpg")

def mirrorVert(im):
    '''mirrors the top half of the image across its horizontal axis'''
    draw = ImageDraw.Draw(im)

    (width, height) = im.size
    for x in range(width):
        for y in range(height/2, height):
            fromX = x
            fromY = height - y
            (newRed, newGreen, newBlue) = im.getpixel( (fromX, fromY))
            im.putpixel( (x,y) , (newRed, newGreen, newBlue) )
    im.save("catmirrorvert.jpg")

def mirrorHoriz(im):
    '''mirrors the right half of the image onto the left half'''
    draw = ImageDraw.Draw(im)

    (width, height) = im.size
    for x in range(width/2, width):
        for y in range(height):
            fromX = width - x
            fromY = y
            (newRed, newGreen, newBlue) = im.getpixel( (fromX, fromY))
            im.putpixel( (x,y) , (newRed, newGreen, newBlue) )
    im.save("catmirrorhoriz.jpg")

def flipVert(im):
    '''flips the image vertically'''
    draw = ImageDraw.Draw(im)

    (width, height) = im.size
    for x in range(0,width):
        for y in range(0,height/2):
            fromX = x
            fromY = height - 1 - y 
            (newRed, newGreen, newBlue) = im.getpixel( (fromX, y))
            (newRed2, newGreen2,newBlue2) = im.getpixel( (x, fromY) )
            im.putpixel( (x,height-1- y) , (newRed, newGreen, newBlue) )
            im.putpixel( (x,y) , (newRed2, newGreen2,newBlue2))
    im.save("catflipvert.jpg")

def flipHoriz(im):
    '''flips the image horizontally'''
    draw = ImageDraw.Draw(im)

    (width, height) = im.size
    for x in range(width/2):
        for y in range(height):
            fromX = width -1 -x
            fromY = y 
            (newRed, newGreen, newBlue) = im.getpixel( (x, fromY))
            (newRed2, newGreen2,newBlue2) = im.getpixel( (fromX, y) )
            im.putpixel( (width -1-x,y) , (newRed, newGreen, newBlue) )
            im.putpixel( (x,y) , (newRed2, newGreen2,newBlue2))
    im.save("catfliphoriz.jpg")

def blur(im):
    '''blurs image'''
    pic = im.filter(ImageFilter.BLUR)
    pic.save("catblur.jpg")

def sharpen(im):
    '''sharpens image'''
    pic = im.filter(ImageFilter.SHARPEN)
    pic.save("catsharpen.jpg")

def edge(im):
    '''edges'''
    pic = im.filter(ImageFilter.EDGE_ENHANCE)
    pic.save("catedge.jpg")

def redTint(im):
    '''red tinted image'''
    layer = Image.new('RGB', im.size, 'red')
    pic = Image.blend(im, layer, 0.5)
    pic.save("catredtint.jpg")

def blueTint(im):
    '''blue tinted image'''
    layer = Image.new('RGB', im.size, 'blue')
    pic = Image.blend(im, layer, 0.5)
    pic.save("catbluetint.jpg")

def greenTint(im):
    '''green tinted image'''
    layer = Image.new('RGB', im.size, 'green')
    pic = Image.blend(im, layer, 0.5)
    pic.save("catgreentint.jpg")

def purpleTint(im):
    '''purple tinted image'''
    layer = Image.new('RGB', im.size, 'purple')
    pic = Image.blend(im, layer, 0.5)
    pic.save("catpurpletint.jpg")

