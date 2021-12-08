import numpy as np
import cv2
from pathlib import Path

for img_file1 in Path.iterdir(Path.cwd()):
    img1 = cv2.imread(str(img_file1))
    for img_file2 in Path.iterdir(Path.cwd()):
        if img_file2 == img_file1:
            break
        img2 = cv2.imread(str(img_file2))
        if img2.shape == img1.shape:
            x = int(img1.shape[0] / 2)
            y = int(img1.shape[1] / 2)
            if img1[x, y, 0] == img2[x, y, 0]:
                Path.unlink(img_file2)
