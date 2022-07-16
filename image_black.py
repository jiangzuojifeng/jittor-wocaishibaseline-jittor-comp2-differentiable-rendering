import cv2
import os
rootpath = "./data/Easyship/train"
savepath = "./data/Easyship/train_b"

image_list = os.listdir(rootpath)
if not os.path.exists(savepath):
    os.mkdir(savepath)

for image_file in image_list:

    image = cv2.imread(os.path.join(rootpath,image_file),-1)

    #alpha = image[:,:,3]
    #cv2.imwrite(os.path.join(savepath,image_file),)
    image[:,:,0] = 255-image[:,:,3]
    image[:,:,1] = 255-image[:,:,3]
    image[:,:,2] = 255-image[:,:,3]
    cv2.imwrite(os.path.join(savepath,image_file),image)
    #save = 1