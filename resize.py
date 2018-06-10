import cv2
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images
count = 0
for img in load_images_from_folder('E:/Program Files/Haar_Training/p/'):
  resized_image = cv2.resize(img,(64,64)) 
  cv2.imwrite("img/"+'pos_'+str(count)+'.jpg',resized_image)
  count+=1

