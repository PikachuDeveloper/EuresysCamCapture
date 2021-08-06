import cv2
import numpy as np

#frame title
wTitle = 'jpg'

# true if mouse is pressed
drawing = False

# coordinates (x0, y0), (x1, y1) of the top left and
# bottom right corners to draw a ROI
Rect = [(1, 1), (2, 2)]

#image, that will be shown in a frame
img = np.zeros((512,512,3), np.uint8)

#True if rectangle should be drawn on a screen
#False if Rbutton pressed or rectangle was not drawn yet
mode = False

# mouse callback function
#when Lbutton down - we draw ROI
#when Lbutton up - ROI is on the screen
#when Rbutton clicked - rectangle should disappear
def draw(event,x,y,flags,param):
    global drawing, Rect, mode, img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        Rect[0] = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        img = cv2.rectangle(img,Rect[0],(x,y),(0,255,0),0)
        cv2.imshow(wTitle, img)

    elif event == cv2.EVENT_LBUTTONUP:
        mode = True
        drawing = False
        Rect[1] = (x, y)
        img = cv2.rectangle(img,Rect[0],Rect[1],(0,255,0),0)
        cv2.imshow(wTitle, img)

    elif event == cv2.EVENT_RBUTTONDOWN:
        mode = False
        drawing = False


vid = cv2.VideoCapture(0)
cv2.namedWindow(wTitle)
cv2.setMouseCallback(wTitle, draw)
while(vid.isOpened()):
    _, img = vid.read()
    if mode:
        img = cv2.rectangle(img, Rect[0], Rect[1], (0, 255, 0), 0)
    cv2.imshow(wTitle, img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        print(Rect)
        break
cv2.destroyAllWindows()
