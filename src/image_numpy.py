import cv2

image = cv2.imread('data/flower.jpg')

print("Image shape:", image.shape)

height, width, channels = image.shape

print("\nheight:", height)
print("width:", width)
print("channels:", channels)

# Top-left quarter
cropped = image[:height // 2, :width // 2]

print("\nCropped image shape:", cropped.shape)

cv2.imshow("Original Image", image)
cv2.imshow("Cropped Image", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()