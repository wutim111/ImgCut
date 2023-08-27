import cv2
import numpy
import os
filepath = './img_input'
filelist=os.listdir(filepath)
repeat_range=300

for filename in filelist :
    img = cv2.imread("./img_input/"+filename)
    img_heigh = img.shape[0]
    heigh_begin=[0,(img_heigh//3)-repeat_range,2*(img_heigh//3)-repeat_range]
    dot=filename.index('.')
    for i in range(0,3):
        New_img=img[heigh_begin[i]:img.shape[0]//3*(i+1),0:img.shape[1]]
        cv2.imwrite('./result/'+filename[:dot]+'_'+str(i)+'.jpg', New_img)