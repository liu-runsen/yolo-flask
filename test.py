# coding:utf-8
import requests

import os

url = 'http://127.0.0.1:5000/v1'


# 图片路径
img_path = "./images/"

files_name = os.listdir(img_path)  # 得到文件夹下的所有文件名称

num = 0  # 图片上传初始计数

for file in files_name:
    # 参数rb，以二进制格式打开一个文件用于只读
    f = {"image": (file, open("./images/" + file, "rb"), "image/jpeg")}

    r = requests.post(url, files=f)

    print(r.json())

    num = num + 1

print('-------------上传结束---------共上传', num, '张图片------------------')