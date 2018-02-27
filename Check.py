#======================================================#
import os
#======================================================#
imageFolderPath = "./古籍馆图片"
filePath = "list.txt"
#======================================================#
eName = 0
ePicture = 0
imgsum = 0

def main():
    name_list = loadNameList(filePath)
    folder_list = listDir(imageFolderPath)
    # for i in range(len(folder_list)):
    for i in range(0,34):
        path = imageFolderPath+'/'+'P'+adjust(i,2)+'001-P'+adjust(i+1,2)+'000'
        image_list = listDir(path)
        check(image_list,name_list,i)        
    print("Count of eName    :",eName)
    print("Count of ePicture :",ePicture)
    print("Count of image    :", imgsum)

def check(img, name,index):
    relname = name[index*1000:min((index+1)*1000,len(name))]
    img_len = len(img)
    for i in range(len(relname)):
        if relname[i] in img:
            img.remove(relname[i])
            relname[i]= None            
    
    relname = remNone(relname)
    nimg = rem(img)

    print("-" * 80,'Start-with-',index*1000)
    print(">>>Name(%d): "%len(relname))
    for i in range(len(relname)):                
        print(relname[i])

    print("-" * 50, 'imageCount=', img_len)

    print(">>>Image(%d):"%len(img))
    for i in range(len(img)):        
        print(img[i])
        # print(nimg[i])
    print("-" * 80,'End-with-',(index+1)*1000)
    print()

    global eName ,ePicture,imgsum
    eName += len(relname)
    ePicture += len(img)
    imgsum += img_len

def rem(lis):
    new=[]
    for i in range(len(lis)):
        s=lis[i]
        s=s[0:s.rfind('-')]
        new.append(s)
    return new

def remNone(lis):
    while lis.count(None) != 0:
        lis.remove(None)
    return lis

def loadNameList(path):
    with open(path, "r") as fopen:
        lines = fopen.readlines()

    if(lines[0] == '文件名\n'):
        lines.remove('文件名\n')    
    while(lines[len(lines)-1] == '\n'):
        lines.pop()
        
    length = len(lines)
    for i in range(length):
        lines[i] = lines[i].replace("\n", "")
    return lines

def listDir(path):
    return os.listdir(path)


def adjust(num, length):
    num = '0' * length + str(num)
    num = num[len(num) - length:]
    return num
#======================================================#
if __name__ == '__main__':
    main()
#======================================================#
