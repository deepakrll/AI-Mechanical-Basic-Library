import cv2

# Load sample image
image = cv2.imread('sample_part.jpg', 0)  # Convert to grayscale

# Apply edge detection (Canny)
edges = cv2.Canny(image, 100, 200)

# Show images
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
