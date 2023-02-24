import cv2
pic = cv2.imread("./cat.png")
cv2.rectangle(pic,(70,90),(170,190),color=(0,0,255),thickness=2)
cv2.imshow('title',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()