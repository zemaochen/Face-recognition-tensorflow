import cv2

def get_the_data_set(window_name, camera_idx, catch_pic_num, path_name):
    cv2.namedWindow(window_name)

    #获取摄像头
    cap = cv2.VideoCapture(camera_idx)

    # 告诉OpenCV使用人脸识别分类器
    classfier = cv2.CascadeClassifier("file/haarcascade_frontalface_alt2.xml")

    # 识别出人脸后要画的边框的颜色，RGB格式
    color = (0, 0, 255)

    #第几张图片
    num = 0
    while cap.isOpened():
        ok, frame = cap.read()  # 读取一帧数据
        if not ok:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将当前桢图像转换成灰度图像

        # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
        # 大于0则检测到人脸
        if len(faceRects) > 0:
            # 单独框出每一张人脸
            for faceRect in faceRects:
                x, y, w, h = faceRect

                # 将当前帧保存为图片
                img_name = '%s/%d.jpg ' %(path_name, num)
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                cv2.imwrite(img_name, image)

                num += 1
                # 如果超过指定最大保存数量退出循环
                if num > (catch_pic_num):
                    break

                # 画出矩形框
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)

                # 显示当前捕捉到了多少人脸图片
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame ,'num:%d' % (num) ,(x + 30, y + 30), font, 1, (255 ,0 ,255) ,4)

        # 超过指定最大保存数量结束程序
        if num > (catch_pic_num): break

        # 显示图像
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

    # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    get_the_data_set("截取人脸", 0, 1, 'img/test')