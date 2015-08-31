import os
from flask import Flask, url_for, render_template, request, session

app = Flask(__name__)

app.secret_key='djakf82y834h2hjksdyfiwe'; 

@app.route('/')
def helloRoot():
    return render_template('home.html')

@app.route('/choosefilter')
def filters():
    return render_template('choosefilter.html')

@app.route('/applyfilter', methods=['GET', 'POST'])
def applyfilter():
    session["filter"]=request.form['filters']
    session["oldimage"]=request.form['file']
    newImage = processimage(session["oldimage"], session["filter"])
    return render_template('applyfilter.html', newImage = newImage)

def processimage(oldimage, filter):
    return "stub.jpg"
##this is where you put the pil code that applies the filter to
##old image and returns the file name of new image

@app.route('/greyscale')
def greyscale():
    return render_template('greyscale.html')

@app.route('/doGreyscale')
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

@app.route('/invert')
def invert():
    return render_template('invert.html')

@app.route('/doInvert')
def doInvert(im):
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
    im.show()
    
@app.route('/binarize')
def binarize():
    return render_template('binarize.html')

@app.route('/doBinarize')
def doBinarize(im, thresh):
    '''changes the image to black and white depending on the specified thresh'''
    draw = ImageDraw.Draw(im)

    (width, height) = im.size
    for x in range(width):
        for y in range(height):
            (red, green, blue) = im.getpixel((x,y))
            if thresh <= ((red + green + blue)/3):
                newRed= 255
                newGreen= 255
                newBlue= 255
            else:
                newRed= 0
                newGreen= 0
                newBlue= 0
            draw.point([(x,y)], (newRed, newGreen, newBlue))
    im.show()
    
@app.route('/mirrorVert')
def mirrorVert():
    return render_template('mirrorvertically.html')

@app.route('/domirrorVert')
def domirrorVert(im):
    '''mirrors the top half of the image across its horizontal axis'''
    draw = ImageDraw.Draw(im)

    (width, height) = im.size
    for x in range(width):
        for y in range(height/2, height):
            fromX = x
            fromY = height - y
            (newRed, newGreen, newBlue) = im.getpixel( (fromX, fromY))
            im.putpixel( (x,y) , (newRed, newGreen, newBlue) )
    im.show()

@app.route('/mirrorHoriz')
def mirrorHoriz():
    return render_template('mirrorhorizontally.html')

@app.route('/domirrorHoriz')
def domirrorHoriz(im):
    '''mirrors the right half of the image onto the left half'''
    draw = ImageDraw.Draw(im)

    (width, height) = im.size
    for x in range(width/2, width):
        for y in range(height):
            fromX = width - x
            fromY = y
            (newRed, newGreen, newBlue) = im.getpixel( (fromX, fromY))
            im.putpixel( (x,y) , (newRed, newGreen, newBlue) )
    im.show()

@app.route('/flipVert')
def flipVert():
    return render_template('mirrorvertically.html')

@app.route('/doflipVert')
def doflipVert(im):
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
    im.show()

@app.route('/flipHoriz')
def flipHoriz():
    return render_template('fliphorizontally.html')

@app.route('/doflipHoriz')
def doflipHoriz(im):
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
    im.show()
    
if __name__=="__main__":
    app.run(debug=False)
    app.run(port=5000)
