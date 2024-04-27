# Automatic File in File Explorer
import os, shutil
path = r"/Users/amandadu/Desktop/coding/python/"
files = os.listdir(path)

print(files)


folder_names = ["csv file","image files","text files"]
for loop in range(0,3):
    if not os.path.exists(path+folder_names[loop]):
# 检查当前遍历到的文件夹是否存在。os.path.exists() 函数用于检查指定的文件或目录是否存在。
        print(path + folder_names[loop])
        os.makedirs((path + folder_names[loop]))
# 如果文件夹不存在，则调用 os.makedirs() 函数创建文件夹。

exit = os.path.exists(path + "csv file")

print(exit)

for file in files: #files = os.listdir(path)
    if ".csv" in files and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".png" in files and not os.path.exists(path + "image files" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in files and not os.path.exists(path + "text files" + file):
        shutil.move(path + file, path + "text files/" + file)
    else:
        print("There are files in this path that were not moved!")

#这段代码的逻辑是：

#如果文件以 .csv 结尾，并且在 csv files 文件夹中不存在同名文件，则将其移动到 csv files 文件夹中。
#如果文件以 .png 结尾，并且在 image files 文件夹中不存在同名文件，则将其移动到 image files 文件夹中。
#如果文件以 .txt 结尾，并且在 text files 文件夹中不存在同名文件，则将其移动到 text files 文件夹中。
#如果文件不满足以上条件，则打印出未移动的文件。

