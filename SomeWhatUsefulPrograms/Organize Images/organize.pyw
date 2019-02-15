import os
from PIL import Image

_Portrait_count = 1
_4k_count = 1
_1080p_count = 1
_720p_count = 1
_others_count = 1

# Making directories
if os.path.isdir("4k"):
    os.rename("4k","4k_old") # To Overcome File Deletion problem 
    os.mkdir("4k")
    # _4k_count = len(os.listdir('.\\4k')) + 1
else:
    os.mkdir("4k")
if os.path.isdir("1080p"):
    os.rename("1080p","1080p_old")
    os.mkdir("1080p")
    # _1080p_count = len(os.listdir('.\\1080p')) + 1
else:
    os.mkdir("1080p")
if os.path.isdir("720p"):
    os.rename("720p","720p_old")
    os.mkdir("720p")
    # _720p_count = len(os.listdir('.\\720p')) + 1
else:
    os.mkdir("720p")
if os.path.isdir("Portrait"):
    os.rename("Portrait","Portrait_old")
    os.mkdir("Portrait")
    # _Portrait_count = len(os.listdir('.\\Portrait')) + 1
else:
    os.mkdir("Portrait")
if os.path.isdir("OtherFiles"):
    os.rename("OtherFiles","OtherFiles_old")
    os.mkdir("OtherFiles")
    # _others_count = len(os.listdir('.\\OtherFiles')) + 1
else:
    os.mkdir("OtherFiles")

fullPath = ''
temp = ''

# Heart of the program
for (dirname, dirs, files) in os.walk('.'):
    if '.\\Portrait' != dirname and '.\\720p' != dirname and '.\\1080p' != dirname and '.\\4k' != dirname:
        for fileName in files:
            fullPath = dirname + '\\' + fileName
            temp = '.' + fileName.split('.')[-1]
            if fileName.endswith('.JPG') or fileName.endswith('.jpg') or fileName.endswith('.jpeg') or fileName.endswith('.png') or fileName.endswith('.PNG') :
                if Image.open(fullPath).size[1] > Image.open(fullPath).size[0]:
                    temp = str(_Portrait_count) + temp
                    os.rename(fullPath, 'Portrait\\'+ temp)
                    _Portrait_count = _Portrait_count + 1
                elif Image.open(fullPath).size[1] > 1080:
                    temp = str(_4k_count) + temp
                    os.rename(fullPath, '4k\\'+ temp)
                    _4k_count = _4k_count + 1
                elif Image.open(fullPath).size[1] > 720:
                    temp = str(_1080p_count) + temp
                    os.rename(fullPath, '1080p\\'+ temp)
                    _1080p_count = _1080p_count + 1
                elif Image.open(fullPath).size[1] <= 720:
                    temp = str(_720p_count) + temp
                    os.rename(fullPath, '720p\\'+ temp)
                    _720p_count = _720p_count + 1
                temp = ''
            elif not fileName.endswith('.pyw'):
                temp = '_' + str(_others_count) + temp
                fileName = fileName.split('.')[:-1][0]
                os.rename(fullPath, 'OtherFiles\\'+ fileName + temp)
                _others_count = _others_count + 1
                temp = ''


# Removing Empty directories
for (dirname, dirs, files) in os.walk('.', topdown=False):
    if not os.listdir(dirname) and '.\\Portrait' != dirname and '.\\720p' != dirname and '.\\1080p' != dirname and '.\\4k' != dirname:
        os.rmdir(dirname)
        # print('removed',dirname, len(os.listdir(dirname)))

print('Total no. of Portrait Images', _Portrait_count)
print('Total no. of 4k Images', _4k_count)
print('Total no. of 1080p Images', _1080p_count)
print('Total no. of 720p Images', _720p_count)