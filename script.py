import cv2
import glob

files = glob.glob("*.jpeg")
print(files)
# set to make all images half size

for image in files:
    img = cv2.imread(image, 0)
    resizedImg = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
    # cv2.imshow("Hey", resizedImg)
    # cv2.waitKey(500)
    # cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image, resizedImg)
