from PIL import Image
#Rajath Ganesh Project Recognition - EEL6825
def resizeImage(imageName):
    basewidth = 100
    img = Image.open(imageName)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(imageName)

for i in range(0, 101):
    # Mention the directory in which you wanna resize the images followed by the image name
    resizeImage("Dataset/FistImages/fist_" + str(i) + '.png')


