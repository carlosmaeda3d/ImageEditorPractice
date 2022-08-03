from PIL import Image
import os

# Script creates thumbnails of all jpegs in folder, renames, and saves in another folder

path = 'C:/Users/carlo/Desktop/My Stuff/Python Stuff/ImageEditorPractice/Images'
pathOut = 'C:/Users/carlo/Desktop/My Stuff/Python Stuff/ImageEditorPractice/EditedImages'

size = 128, 128

for filename in os.listdir(path):
    img = Image.open(f'{path}/{filename}')
    img.thumbnail(size)
    clean_img = os.path.splitext(filename)[0]
    img.save(f'{pathOut}/{clean_img}_thumbnail.jpg')