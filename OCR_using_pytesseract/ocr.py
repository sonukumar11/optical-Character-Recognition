#downlaoding opencv library..
#!pip install opencv-python

#importing pytesseract library
#!pip install pytesseract

#Downlaod the pytesseract.exe file from the link
# https://github.com/UB-Mannheim/tesseract/wiki


#importing the opencv Library
import cv2
#importing the pytesseract Library
import pytesseract
#Settinng the path where to tesseract.exe is located
pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#reading image using opencv library
img = cv2.imread('data.png')
#Showing image using opencv Library
cv2.imshow('Sample Image',img)
#To destroy opened window using any key press..
cv2.waitKey(0)
cv2.destroyAllWindows()

#Converting image to string
myString = pytesseract.image_to_string(img)


#printing the text in the images
print(myString)