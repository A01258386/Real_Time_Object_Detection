import os 
import re

DIR_TARGET = os.path.abspath("uncheck_picture")
DIR_OUT ="result"
UNCHECKED_FOLDER = 'uncheck_picture'

# pictures = os.listdir(DIR_TARGET)

# #runs detect on all files in uncheck_picture directory
# for item in pictures:
#     print(os.path.join(DIR_TARGET,item))
#     os.system('python detect.py --source ./%s --project %s --name detect' % (os.path.join(UNCHECKED_FOLDER, item),DIR_OUT))

# DIR_TARGET = os.path.abspath("../dataset/Endangered-Animals-1/test/images")
# print(DIR_TARGET)
# # os.system("python detect.py --weights runs/train/exp/weights/best.pt --img 416 --conf 0.1 --source '%s' " % (DIR_TARGET))
# print("python detect.py --weights runs/train/exp/weights/best.pt --img 416 --conf 0.1 --source '%s' " % (DIR_TARGET))

# python detect.py --weights runs/train/exp/weights/best.pt --img 416 --conf 0.1 --source 
# 'c:\Users\sjtee\Desktop\BCIT Term 3\Algo\yolo_discord_Bot\dataset\Endangered-Animals-1\test\images' 
# python detect.py --weights runs/train/exp/weights/best.pt --img 416 --conf 0.1 --source 
# 'C:\Users\sjtee\Desktop\BCIT Term 3\test\yolo\content\datasets\Endangered-Animals-1\test\images'

# 'C:\Users\sjtee\Desktop\BCIT Term 3\Algo\yolo_discord_Bot\datasets\Endangered-Animals-1\test\images'
target = os.sys.argv

if target[1] == 'nano':
    os.system(r"python detect.py --weights runs/train/exp/weights/bestnano.pt --img 416 --conf 0.1 --source ..\datasets\Endangered-Animals-1\test\images")
elif target[1] == 'small':
    os.system(r"python detect.py --weights runs/train/exp/weights/bestsmall.pt --img 416 --conf 0.1 --source ..\datasets\Endangered-Animals-1\test\images")
else :
    print('something happened')