
## find the size of a folder name in the system
# size is the total file size with all the dirs and files under selected directory
# you can use the size information to check user limit, compare and run other program

# if you select c:\\windows dir for windows os , this will run for long as there are many subfolders and files

import os
count = 0
size = 0

# update below folder name c:\\windows with the folder name you want to check, type full path with drive and use \\
for folderName, subfolders, filenames in os.walk('C:\\downloads'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
	    print('SUBFOLDER OF ' + folderName + ':' + subfolder)
    for filename in filenames:
	    print('FILE INSIDE ' + folderName + ':' + filename)
	    count = count + 1
	    print('')
	    size = size + os.path.getsize(os.path.join(folderName,filename))
	    #print(size) //working now - drop line before print
		
print('TOTAL NUMBER OF FILE AND FOLDER ' + ':' + str(count))
dir_in_gb = size / (1024*1024*1024)
print("Total size for this main dir in GB: ", dir_in_gb)

