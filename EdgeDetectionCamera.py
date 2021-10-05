import cv2

videoFeed = cv2.VideoCapture(0)
t1 = 30 #Low threshold (0 - 100)
t2 = 100 #High threshold (0 - 100)
kernalSize = 7 #Kernal Size 3x3, 5x5, 7x7

while True:
    
    if cv2.waitKey(1) == ord("e"):
        break

    _, frame = videoFeed.read()
    #Create frames
    gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gs, t1, t2, kernalSize)

    #Display frames
    cv2.imshow("Edges \'E\' to Exit", edges)
    cv2.imshow("Grayscale \'E\' to Exit", gs)

videoFeed.release()
cv2.destroyAllWindows()
