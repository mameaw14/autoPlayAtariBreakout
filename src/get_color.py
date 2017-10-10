import cv2
import os
import numpy as np

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
img = None
pos_x, pos_y = 0, 0


def get_position(event, x, y, flags, param):
    global img, pos_x, pos_y
    if event == cv2.EVENT_MOUSEMOVE and img is not None:
        pos_x, pos_y = x, y
        print('row: ', y, ', col: ', x, ', color value: ', img[y, x])


def get_color():
    global img, pos_x, pos_y
    img = cv2.imread(DIR_PATH + '\\images\\ss.png', 1)
    cv2.namedWindow('image')
    # cv2.setMouseCallback('image', get_position)

    r, c, ch = img.shape
    r = int(r / 2)
    c = int(c / 2)
    img = cv2.resize(img, (c, r))

    # lowerb = [153, 153, 153]
    # lowerb = np.array(lowerb, dtype=np.uint8)

    # upperb = [153, 153, 153]
    # upperb = np.array(upperb, dtype=np.uint8)
    lowerb = [255, 130, 0]
    lowerb = np.array(lowerb, dtype=np.uint8)

    upperb = [255, 140, 5]
    upperb = np.array(upperb, dtype=np.uint8)

    img_cir = cv2.inRange(img, lowerb, upperb)

    ret, th = cv2.threshold(img_cir.copy(), 250, 255, 0)
    _, cnts, h = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  
    
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        # if 70 < area < 80:
        cv2.drawContours(img, cnt, -1, (255, 255, 0), 3)
        x,y,w,h = cv2.boundingRect(cnt)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, "area: {0:.2f}".format(area), (int(x),int(y)),font,0.5,(255,255,255),1)

        print(area)

    # color = np.array(np.zeros((200, 200, 3), dtype=np.uint8))

    while True:
        # c1, c2, c3 = cv2.split(color)
        # c1 *= 0
        # c2 *= 0
        # c3 *= 0
        # c1 += img[pos_y, pos_x][0]
        # c2 += img[pos_y, pos_x][1]
        # c3 += img[pos_y, pos_x][2]
        # color = cv2.merge((c1, c2, c3))

        cv2.imshow('image', img)
        # cv2.imshow('img_cir', img_cir)
        key = cv2.waitKey(1) & 0xff
        if key == ord('q'):
            break


if __name__ == '__main__':
    get_color()
