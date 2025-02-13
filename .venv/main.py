from PIL import Image, ImageFilter, ImageEnhance

#

with Image.open("tulips.jpg") as picture:
    #picture.show()
    
    black_white = picture.convert('L') 
    black_white.save("blackandwhite.png")
    
    mirror = picture.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save("mirrored.png")
    
    blur = picture.filter(ImageFilter.BLUR)
    blur.save("blurred.png")
    
    #enhance
    contrast = ImageEnhance.Contrast(picture)
    contrast = contrast.enhance(2)
    contrast.save("contrast.png")
    
    color = ImageEnhance.Color(picture).enhance(1.7)
    color.save("color.png")
    