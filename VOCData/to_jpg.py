# 将所有的图片转换成为jpg格式（防止因为图片格式造成的cv2.imread()异常）

import PIL.Image as Image
import os


Path = 'D:/anaconda/envs/yolov5/yolov5/VOCData/'

def start(Path):
    filelist = os.listdir(Path + 'images/')
    for file in filelist:
        img = Image.open(Path + 'images/' + file).convert('RGB')
        # print(img)
        img.save(Path + file)
    print('Done!')

start(Path)