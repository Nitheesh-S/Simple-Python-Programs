import os

file_list = os.listdir(path='.')

file_list_length = len(file_list)

f = open('file_list.txt','w')
for i in range(file_list_length):
    f.write(file_list[i])
    f.write('\n')
f.close()