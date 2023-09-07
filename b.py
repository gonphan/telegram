import pickle
from os import listdir
import cv2
import numpy as np
""" hàm để xử lý dữ liệu data chay"""
raw_folder = "bb/"
def save_data(raw_folder = raw_folder):
    # đặt tên biến để tất cả chuyển về 128x128
    dest_size =(1598,935)
    print("bắt đầu xử lý ảnh ")

    pixel =[]

    for file in listdir(raw_folder):
        if file !=".DS_Store":
            print("file",file)
                    #append cho tất cả các ảnh về 128x128
            pixel.append(cv2.resize(cv2.imread(raw_folder + "/" + file), dsize=(1598,935)))
                    #labeys.append(folder)

    pixel = np.array(pixel)#chứa đặc trung futer 1 tấm ảnh trên nhiều tấm ảnh
    print("anhhhhhhhhhhhhh",pixel)
print(save_data())

