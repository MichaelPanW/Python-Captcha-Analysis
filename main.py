

import pytesseract
import cv2
import numpy as np
import os
import glob


def detect_image_text(path):
    # 讀取圖片
    image = cv2.imread(path)
    # 進行閾值處理，將灰色部分轉為純白
    _, thresholded = cv2.threshold(
        image, 128, 255, cv2.THRESH_BINARY)
    # 將圖片轉換成灰度
    gray_image = cv2.cvtColor(thresholded, cv2.COLOR_BGR2GRAY)

    # 使用中值濾波器去除黑色雜點
    blur_image = cv2.medianBlur(gray_image, 3)

    # 使用中值濾波器去除黑色雜點
    output_image = cv2.medianBlur(blur_image, 3)

    # # 使用Tesseract進行文字辨識
    text = pytesseract.image_to_string(output_image)
    return (text)


if __name__ == '__main__':

    folder_path = 'image'
    images = glob.glob(os.path.join(folder_path, "*.jpg"))  # 可以修改為需要的圖片檔案類型
    # 列印所有圖片檔案路徑
    for image in images:
        print(detect_image_text(image))
