import os
import random
if __name__ == '__main__':
    path = "./VOCdevkit/VOC2007/ImageSets/Main/trainval.txt"
    file = open(path, mode='w')
    list_str = []
    # shuffle()使用样例

    for count in range(1, 511):
        count = count + 1
        list_str.append(str(count).zfill(6))

    x = [i for i in range(len(list_str))]
    print(type(x), x)
    random.shuffle(x)
    random.shuffle(list_str)
    print(x)

    for i in range(len(list_str)):
        file.write("/home/nvidia-3080/PycharmProjects/yolov4-pytorch-master/VOCdevkit/VOC2007/JPEGImages/"+list_str[i]+".jpg\n")
        print(list_str[i])

    file.close()
