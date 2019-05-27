import cv2


def open_camera(window_name, camera_idx):
    i = 1
    cv2.namedWindow(window_name)#该方法是写入打开时视频框的名称
    # 捕捉摄像头
    cap = cv2.VideoCapture(camera_idx)#camera_idx 的参数是0代表是打开笔记本的内置摄像头，也可以写上自己录制的视频路径
    cap.set(3,1080)
    while cap.isOpened():#判断摄像头是否打开，打开的话就是返回的是True
        ok, frame = cap.read()#读取一帧数据，该方法返回两个参数，第一个参数是布尔值，frame就是每一帧的图像，是个三维矩阵，当输入的是一个是视频文件，读完ok==flase
        if not ok:#如果读取帧数不是正确的则ok就是Flase则该语句就会执行
            break
        # 显示图像
        cv2.imshow(window_name, frame)#该方法就是现实该图像
        c = cv2.waitKey(10)
        if c & 0xFF == ord('y'):
            cv2.imwrite("img/yhy0/" + str(i) + ".png", frame)
            i=i+1
            continue
        if c & 0xFF == ord('q'):#q退出视频
            cv2.imwrite("img/"+"a"+".png",frame)
            break
            # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    open_camera("采集图像", 0)
