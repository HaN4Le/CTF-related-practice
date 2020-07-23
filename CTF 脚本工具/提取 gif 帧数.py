from PIL import Image
import os

gifFileName = "E:\信息安全实验室\其他CTF\CTF\XCTF\misc\新手进阶\\give_you_flag\\4b0799f9a4d649f09a882b6b1130bb70.gif"

im = Image.open(gifFileName)                            # 使用Image模块的open()方法打开gif动态图像时，默认是第一帧
pngDir = gifFileName[:-4]                              

os.mkdir(pngDir)                                        # 创建存放每帧图片的文件夹

try:
    while True:
        current = im.tell()                             # 保存当前帧图片
        im.save(pngDir + "/" + str(current) + '.png')
        im.seek(current + 1)                            # 获取下一帧图片
except EOFError:
    print("Reach the end of gif sequence")
    pass