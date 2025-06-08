import numpy as np
import cv2


img = cv2.imread('alf.jpg')
size = 7 # only odd
max_step = (size - 1) / 2

for i in range(max_step, img.rows - max_step, size):
    for j in range(max_step, img.cols - max_step, size):



for (int i = max_step; i < m.cols- max_step; size):



    for (int j = max_step; j < m.cols- max_step; j+=size) {
        Vec3b colour = m.at<Vec3b>(Point(j, i));
        for (int k = -max_step; k <= max_step; k++) {
            for (int l = -max_step; l <= max_step; l++) {
                m.at<Vec3b>(Point(j - k, i - l)) = colour;
            }
        }
    }
}
imshow("pixeled", m);
waitKey(0);


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()