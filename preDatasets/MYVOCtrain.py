import xml.etree.ElementTree as ET
from os import getcwd
import os
import cv2
sets = [('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
classes = ["AAC","brick", "concrete" ,"glass" ,"gypsum" ,"paper" ,"plastic" ,"rubber" ,"tile" ,"timber" ,"woven"]

def check_file(file_path):
    # os.chdir(file_path)
    # one_dir=os.path.abspath(os.curdir)
    # file_dir.append()
    all_file = os.listdir(file_path)
    # print(all_file)
    files = []
    files2 = []
    files3 = []
    for f in all_file:
        if os.path.isdir(f):
            files.extend(check_file(file_path+'/'+f))
            os.chdir(file_path)
        else:
            files.append(file_path+'/'+f)
            files2.append(f)
            f_png = f.replace(".jpg","")
            files3.append(f_png)
    return files,files2,files3


def convert_annotation(name, list_file):
    in_file = open('./Annotations/'+name+".xml", encoding='utf-8')
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        print(name)
        print("XXXXXXXXXXXXXXX")
        difficult = 0
        if obj.find('difficult') != None:
            difficult = obj.find('difficult').text
        cls = obj.find('name').text
        print(type(cls))
        print((cls))

        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')

        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
             int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

if __name__ == '__main__':
    file, name, realname = check_file("Data/JPEGImages/")
    print(file)
    print(name)
    print(realname)
    list_file = open('./val.txt', 'w')
    for i in range(len(realname)):
        list_file.write("/home/nvidia-3080/PycharmProjects/yolov4-pytorch-master/VOCdevkit/VOC2007/JPEGImages/"+name[i])
        convert_annotation(realname[i], list_file)
        list_file.write('\n')
    list_file.close()

    # for i in range(len(file)):
    #     tem = cv2.imread(file[i])
    #     cv2.imwrite("./color/picjpg/"+realname[i]+".jpg",tem)



# wd = getcwd()
#
# for year, image_set in sets:
#     image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt' % (year, image_set)).read().strip().split()
#     list_file = open('%s_%s.txt' % (year, image_set), 'w')
#     for image_id in image_ids:
#         list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg' % (wd, year, image_id))
#         convert_annotation(year, image_id, list_file)
#         list_file.write('\n')
#     list_file.close()
# ————————————————
# 版权声明：本文为CSDN博主「纯氧゜」的原创文章，遵循CC
# 4.0
# BY - SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / weixin_45560365 / article / details / 118557163