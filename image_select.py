import os
import cv2
import numpy as np


id = 'Car'
#id = 'Easyship'
rootpath1 = './logs/' + id + '/test'
rootpath2 = './data/' + id + '/train_b'
savepath = './data/' + id + '/train'

image_list = os.listdir(rootpath2)
save_list = []
for image_file in image_list:
    image_train = cv2.imread(os.path.join(rootpath2,image_file))
    image = cv2.imread(os.path.join(rootpath1, id + '_' + image_file),-1)
    image_train = image_train.astype(np.int16)
    image = image.astype(np.int16)
    
    error = abs(image - image_train)
    error_ct = error[:,:,0] + error[:,:,1] + error[:,:,2]
    error_ct[error_ct<30] = 0
    error_ct[error_ct>=30] = 1
    errors = error_ct.sum()

    #if errors < 50000:
    if errors < 20000:
        image_name,_ = os.path.splitext(image_file)
        save_list.append(image_name)
        #cv2.imwrite(os.path.join(savepath,image_file),error)
save_list = np.array(save_list)
print(save_list.shape[0])
np.save(savepath, save_list)