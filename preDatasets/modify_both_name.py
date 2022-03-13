import os
import cv2
import numpy
import shutil


def listdir(path, list_name, list_name2, type = '.jpg'):  # , list_name2):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name, list_name2,type=type)  # list_name2)
        elif os.path.splitext(file_path)[1] == type:
            list_name.append(file_path)
            list_name2.append(file)
# 下面这一段是用来更改标签和图片的名字的，批量更改，而且要同步更改，名字相同的图片和标签文件要变成相同的名字

# def format_converter(names):
#     for i in range(len(names)):
#         cv2.imread(names)
#
#
#         cv2.imwrite()
if __name__ == '__main__':
    if 1:
        path = "./Data/"
        filelist=[]
        filelist2=[]
        listdir(path,filelist,filelist2, type= ".jpg")
        count = 0
        for i in range(len(filelist)):
            print(filelist[i])
            print(filelist2[i])


        for i in range(len(filelist)):
            count = count + 1
            # MainName = file.split(".")[0]
            MainName = filelist2[i][0:len(filelist2[i])-4]
            realPath =  filelist[i][0:len(filelist[i])-len(filelist2[i])-1]+"/"
            print(MainName, realPath)
            # 旧图像名字
            Olddir = filelist[i]
            if os.path.isdir(Olddir):
                continue
            # filename = os.path.splitext(filelist2[i])[0]
            # 新图像名字
            Newdir = os.path.join(realPath, str(count).zfill(6) + str(".jpg"))
            # 旧标签的名字
            Olddir2 = realPath + MainName + ".xml"
            # 新标签的名字
            Newdir2 = realPath + str(count).zfill(6) + ".xml"
            # # 操作不可逆，风险较大，正式操作之前的检验打印，检验无误，取消紧随两行的注释再次运行即可
            print("NUM: ", count)
            print(Olddir)
            print(Newdir)
            print(Olddir2)
            print(Newdir2)
            os.rename(Olddir, Newdir)
            os.rename(Olddir2, Newdir2)
        print("Finally！！！！！")
    else:
        path = "./Data/"
        filelist = []
        filelist2 = []
        listdir(path, filelist, filelist2, type=".png")
        count = 0

        for i in range(len(filelist)):
            print(filelist[i])
            print(filelist2[i])

        for i in range(len(filelist)):

            count = count + 1
            # MainName = file.split(".")[0]
            MainName = filelist2[i][0:len(filelist2[i]) - 4]
            realPath = filelist[i][0:len(filelist[i]) - len(filelist2[i]) - 1] + "/"
            # 旧图像名字
            Olddir = filelist[i]
            if os.path.isdir(Olddir):
                continue
            # filename = os.path.splitext(filelist2[i])[0]
            # 新图像名字
            Newdir = Olddir[0:len(Olddir) - 4]+".jpg"
            # # 操作不可逆，风险较大，正式操作之前的检验打印，检验无误，取消紧随两行的注释再次运行即可
            print("NUM: ", count)
            print(Olddir)
            print(Newdir)
            I = cv2.imread(Olddir)
            cv2.imwrite(Newdir,I)
        print("Finally！！！！！")