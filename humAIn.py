import numpy
import imutils
import cv2
import pytesseract


#Reading an image from the dataset       
img=cv2.imread('1.jpeg')

#Convert the image to Grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Threshold is applied for image filteration
ret, thresh=cv2.threshold(gray,127,255,0)

#Edge detection
a=cv2.Canny(gray,170,200)

#The images are displayed
cv2.imshow('image',img)
cv2.imshow(' Gray Image',gray)
cv2.imshow('new image',a)

#The contours has been applited to detect the number plate
(cnts, _) = cv2.findContours(a.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
NumberPlateCnt=None

count=0
for c in cnts:
    d=cv2.arcLength(c,True)
    approx= cv2.approxPolyDP(c,0.02*d,True)
    if len(approx)==4:
        NumberPlateCnt= approx
        break

cv2.drawContours(img,[NumberPlateCnt], -1,(0,255,0),3)
cv2.imshow("Final imagee with Number Plate detected",img)

cv2.waitKey(0)


cv2.imwrite('D:\pytho\1.jpeg',img)
text=pytesseract.image_to_string(Image.open('images.jpg'))
print(text)


cv2.destroyAllWindows()
