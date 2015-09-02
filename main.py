import os
from flask import Flask, url_for, render_template, request, session, redirect
from flask import send_from_directory
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter
from werkzeug import secure_filename
import tempfile

app = Flask(__name__)

app.secret_key='djakf82y834h2hjksdyfiwe';

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB


def check_file(file):
    # Check if the file is one of the allowed types/extensions
    if not allowed_file(file.filename):
        print "Block 1"
        message = "Sorry. Only files that end with one of these "
        message += "extensions is permitted: " 
        message += str(app.config['ALLOWED_EXTENSIONS'])
        message += "<a href='" + url_for("index") + "'>Try again</a>"
        return message
    elif not file:
        print "block 2"
        message = "Sorry. There was an error with that file.<br>"
        message += "<a href='" + url_for("index") + "'>Try again</a>"
        return message
    return ''

# If the file you are trying to upload is too big, you'll get this message
@app.errorhandler(413)
def request_entity_too_large(error):
    message = 'The file is too large, my friend.<br>'
    maxFileSizeKB = app.config['MAX_CONTENT_LENGTH']/(1024)
    message += "The biggest I can handle is " + str(maxFileSizeKB) + "KB"
    message += "<a href='" + url_for("filters") + "'>Try again</a>"
    return message, 413

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    result = check_file(file)
    if result != '':
        print "result was not blank, result =", result
        return result
    else:
        print "result was blank"
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)

        fullFilename = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
        session['file'] = fullFilename
        print "session['file'] =" ,session['file']
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(fullFilename)
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        session["filter"]=request.form['filters']
        newImage = processimage(session["filter"])
        return render_template('applyfilter.html', newImage = fixupfilename(newImage))

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

####

@app.route('/')
def helloRoot():
    return render_template('home.html')

@app.route('/choosefilter')
def filters():
    return render_template('choosefilter.html')

def getTempFileName(myPrefix):
    f = tempfile.NamedTemporaryFile(suffix = ".jpg", prefix = myPrefix, delete=False, dir=app.config['UPLOAD_FOLDER'])
    f.close()
    return f.name

def processimage(filter):
    im = Image.open(session["file"])
    if filter == "Greyscale":
        greyscale(im)
    if filter == "Sepia":
        sepia(im)
    if filter == "Invert":
        invert(im)
    if filter == "Mirror Vertically":
        mirrorVert(im)
    if filter == "Mirror Horizontally":
        mirrorHoriz(im)
    if filter == "Flip Vertically":
        flipVert(im)
    if filter == "Flip Horizontally":
        flipHoriz(im)
    if filter == "Blur":
        blur(im)
    if filter == "Sharpen":
        sharpen(im)
    if filter == "Edge":
        edge(im)
    if filter == "Red Tint":
        redTint(im)
    if filter == "Blue Tint":
        blueTint(im)
    if filter == "Green Tint":
        greenTint(im)
    if filter == "Purple Tint":
        purpleTint(im)
    name = getTempFileName("newImage")
    print "In processimage, name=", name
    im.save(name)
    return name
        
##this is where you put the pil code that applies the filter to
##old image and returns the file name of new image

def fixupfilename(stupidfilename):
    '''change a file name such as
    home/linux/ieng6/spis15/spis15ak/github/SPIS15-Project-Web-Sierra-Lauren/uploads/newImagehMICau.jpg
    into /uploads/newImagehMICau.jpg'''
    goodfilename = "/" + app.config['UPLOAD_FOLDER'] + os.path.basename(stupidfilename)
    return goodfilename

@app.route('/greyscale')
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

@app.route('/sepia')
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
            
@app.route('/invert')
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

@app.route('/mirrorVert')
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

@app.route('/mirrorHoriz')
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

@app.route('/flipVert')
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

@app.route('/flipHoriz')
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

@app.route('/blur')
def blur(im):
    '''blurs image'''
    im.filter(ImageFilter.BLUR)

@app.route('/sharpen')
def sharpen(im):
    '''sharpens image'''
    im = im.filter(ImageFilter.SHARPEN)
    
@app.route('/edge')
def edge(im):
    '''edges'''
    im.filter(ImageFilter.EDGE_ENHANCE)

@app.route('/redTint')
def redTint(im):
    '''red tinted image'''
    layer = Image.new('RGB', im.size, 'red')
    Image.blend(im, layer, 0.5)

@app.route('/blueTint')
def blueTint(im):
    '''blue tinted image'''
    layer = Image.new('RGB', im.size, 'blue')
    Image.blend(im, layer, 0.5)

@app.route('/greenTint')
def greenTint(im):
    '''green tinted image'''
    layer = Image.new('RGB', im.size, 'green')
    Image.blend(im, layer, 0.5)

@app.route('/purpleTint')
def purpleTint(im):
    '''purple tinted image'''
    layer = Image.new('RGB', im.size, 'purple')
    Image.blend(im, layer, 0.5)

if __name__=="__main__":
    app.run(debug=False)
    app.run(port=5000)
