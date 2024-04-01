import cv2
import pickle
width = 52   
height = 27
try:
    with open("CarParkPos", "rb") as f:
        postlist = pickle.load(f)
except:
    postlist = []

def mouseclick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        postlist.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(postlist):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y <y1 + height:
                postlist.pop(i)
    with open("CarParkPos","wb") as f: 
        pickle.dump(postlist, f)          

while True:
    img =cv2.imread("first_frame.jpg")
    for pos in postlist:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255,0,0), 2)
    # print("postlist: ",postlist)

    cv2.imshow("img",img)
    cv2.setMouseCallback("img", mouseclick)
    cv2.waitKey(1)