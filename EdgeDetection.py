import cv2
import os

#Path Strings
d = 'D:\CP\CP467\A1 - Edge Detection\Images' # Set to path of folder
ecStr = "Edges-Canny-"
esStr = "Edges-Sobel-"
gsStr = "Grayscale-"
blStr = "Blurred-"

ks = 3
kernel = (ks,ks) #Guassian blur kernel Size 3x3, 5x5, 7x7


#Canny parameters
t1 = 30 # Low threshold (0 - 100%)
t2 = 90 # High threshold (0 - 100%)

#Sobel parameters
x = 1 # 1 to detect on x axis 0 to skip
y = 1 # 1 to detect on y axis 0 to skip

#Go through each file in directory
for filename in os.listdir(d):
    if (filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".jpg")) and not (filename.startswith(gsStr) or filename.startswith(blStr) or filename.startswith(esStr) or filename.startswith(ecStr)):
        
        print("Processing: " + filename)
        
        #Open Image
        image = cv2.imread(os.path.join(d, filename))

        #Grayscale and blur the image
        grayscaleImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurredImg = cv2.GaussianBlur(grayscaleImg, kernel, 0)
        cv2.imwrite(os.path.join(d, (blStr + filename)), blurredImg)

        #Apply Sobel Operator
        edgesSobel = cv2.Sobel(src=blurredImg, ddepth=cv2.CV_64F, dx=x, dy=y)
        cv2.imwrite(os.path.join(d, (esStr + filename)) , edgesSobel)        

        #Apply Canny Operator
        edgesCanny = cv2.Canny(blurredImg, t1, t2)
        cv2.imwrite(os.path.join(d, (ecStr + filename)) , edgesCanny)
