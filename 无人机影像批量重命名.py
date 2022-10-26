'''
图像批量重命名
'''
import os

start = 120913 # 开始的序号

image_dir = 'C:/cnu_workplace/PycharmProjects/d2l/6——12-19/'  # 源图片路径
images_list = os.listdir(image_dir)
nums = len(os.listdir(image_dir))
print('found %d pictures' % nums)
output_dir = 'C:/cnu_workplace/PycharmProjects/d2l/new/'  # 图像重命名后的保存路径

for i in images_list:
    os.rename(image_dir+i,output_dir+str(start)+'.jpg') # 前面是旧的路径,后面是新路径
    start = start + 1

print('finished!')
