from PIL import Image
import os
import glob

# 4 different areas for the 4 pictures on the scanner. 
area = [0,0,1200,1775],[1195, 0, 2400, 1775],[0, 1775, 1200, 3500],[1195, 1775, 2400, 3500]

newpath = r'oppdelt' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

imagelist = (glob.glob('*.png'))

for imgs in imagelist:
    print('Current image: ' + imgs)
    for i in range(0,4):
        im = Image.open(imgs)
        print('mode:' + im.mode)
        im = im.crop((area[i]))
        im = im.transpose(Image.ROTATE_90) # Rotate image 90degrees
        imgName = imgs[:-4] #remove .png before appending numbers
        print('Saving: ' + imgName + '_0' + str(i) + '.png')
        im.save( 'oppdelt\\' + imgName + '_0' + str(i) + '.png' )

    print(' ')
        
