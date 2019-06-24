"""
    Python program using OpenCV to convert a pixel image to an ASCII image.
    ~~ by Eli Anderson ~~
"""
# TODO -- clean up code, let user decide detail in webcam
import cv2 as cv
import numpy as np
import time

# setup
np.set_printoptions(threshold=np.inf)
ascii_vals = [' ', '.', "'", '^', ',', ':', ';', '!', 'i', 'l', '<', '>', 'u', 'o', 'x', '+', 'z', 'k', 'U', 'O',
                  'X', 'Z', '#', '0', 'K', 'M', '@']


def img_conv():
    strang = input('Enter file name: ')
    detail = float(input('Enter level of detail (1.0 to 3.0, with 1 being the most detailed): ')) * 10
    img = cv.imread(strang, 0)

    # convert data to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BAYER_BG2GRAY)

    # resize to fit screen
    resized = cv.resize(gray, (200, 100))
    rows1, cols1 = resized.shape

    # assign an ASCII char for each pixel value
    ascii_img = np.empty([rows1, cols1], dtype='S1')
    for i in range(rows1):
        for j in range(cols1):
            val = int(resized[i, j] // detail)
            ascii_img[i, j] = ascii_vals[val]

    print('\n'.join((''.join(str(row, encoding='UTF-8')) for row in ascii_img)), end='')


# Live ASCII webcam
def webcam():
    detail = float(input('Enter level of detail (1.0 to 3.0, with 1.0 being the most detailed): ')) * 10
    camcap = cv.VideoCapture(0)

    while (cv.waitKey(1) & 0xFF) != ord('q'):
        ret, frame = camcap.read()

        # convert to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # resize to fit screen
        resized = cv.resize(gray, (200, 100))
        rows, cols = resized.shape

        ascii_img = np.empty([rows, cols], dtype='S1')
        for i in range(rows):
            for j in range(cols):
                val = int(resized[i, j] // detail)
                ascii_img[i, j] = ascii_vals[val]

        print('\n'.join((''.join(str(row, encoding='UTF-8')) for row in ascii_img)), end='')
        time.sleep(0.05)

    # release the capture and destroy windows when done
    camcap.release()
    cv.destroyAllWindows()
    return


if __name__ == '__main__':
    ans = input('Image conversion or ASCII webcam? (Press I or W) ')
    if ans == 'I':
        img_conv()
    else:
        webcam()
