def doGreyscale(im):
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
    im.show() 
    im.save("Greyscale.jpg")

def doPurpleOverlay(im, color="#C7A4EB", alpha=0.5):
    '''makes the image purple'''
    overlay = Image.new(im.mode, im.size, color)
    bw_src = ImageEnhance.Color(im).enhance(0.0)
    return Image.blend(bw_src, overlay, alpha)
