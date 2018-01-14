import os

# def printDirectory(pathToDirectory):
#     if (os.path.isfile(pathToDirectory)):
#         print("it's file")
#         return
#
#     print (pathToDirectory)
#
#     for item in os.listdir(pathToDirectory):
#         if(os.path.isdir(item)):
#             print('\t' + item + "/")
#         else:
#             print ("\t" + item)
#
# print (os.getcwd())
# print (os.curdir)
# print (str(os.listdir(os.curdir)))
#
# path = '/home/andrii/PycharmProjects/PythonStudy/Task4_web_server'
# os.chdir(path)
# print (os.getcwd())
#
# os.chdir('/home/andrii/PycharmProjects/PythonStudy')
# print (os.getcwd())
#
# parentFolder = os.path.split(path)[0]
# print (parentFolder)
# parentFolder = os.path.split(parentFolder)[0]
# print (parentFolder)
# parentFolder = os.path.split(parentFolder)[0]
# print (parentFolder)
# parentFolder = os.path.split(parentFolder)[0]
# print (parentFolder)
# print
#
# # os.chdir(parentFolder + "/andrii/.bashrc")
# printDirectory(os.getcwd())
# printDirectory(path)
#
# printDirectory(parentFolder)
#
# print (os.path.split("/1/1/1"))
# print (os.path.split("/1"))
# print (os.path.split("/1"))
print(type(os.path.split("C:\\TestFolder\\Testfolder_textFile.txt") ))
print(os.path.split("C:\\TestFolder\\Testfolder_textFile.txt"))
