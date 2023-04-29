import cv2 as cv
import numpy as np
import scipy.ndimage as ndimg
import matplotlib.pyplot as plt

Path = 'valve.png'
Image = cv.imread(Path, 0)

Sobel = ndimg.sobel(Image)


def fillter(image: np.ndarray, f: np.ndarray):
    h0, w0 = image.shape
    s1, s2 = f.shape
    h, w = h0-s1+1, w0-s2+1
    g = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            g[i, j] = np.multiply(image[i:i+s1, j:j+s2], f).sum()
    return g


F1 = np.array([[-1, 0, 0],
               [0, 0, 0],
               [0, 0, +1]])

Output1 = fillter(Image, F1)

# plt.imshow(Image, cmap='gray')
# plt.title('Original Image')
# plt.show()

# Fx = np.array([[-1, 0, +1],
#                [-2, 0, +2],
#                [-1, 0, +1]])
#
# h0, w0 = Image.shape
# s1, s2 = Fx.shape
# h, w = h0-s1+1, w0-s2+1
#
# Gx = np.zeros((h, w))
# for i in range(h):
#     for j in range(w):
#         Gx[i, j] = np.multiply(Image[i:i+s1, j:j+s2], Fx).sum()
#
plt.imshow(Output1, cmap='gray')
plt.title('Output1')
plt.show()
