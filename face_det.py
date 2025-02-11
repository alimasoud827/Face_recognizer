import cv2
import sys
import requests
import numpy as np
import os

image_source = sys.argv[1]
output_path = sys.argv[2]

if image_source.startswith("http://") or image_source.startswith("https://"):
    response = requests.get(image_source)
    if response.status_code != 200:
        print("❌ Error: Unable to download image")
        sys.exit(1)

    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

else:
    if not os.path.exists(image_source):
        print("❌ Error: File not found")
        sys.exit(1)

    image = cv2.imread(image_source)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imwrite(output_path, image)
print(f"Face detection complete. Saved to {output_path}")

# import cv2
# import sys
# import requests
# import numpy as np
# import os

# image_source = sys.argv[1]
# output_path = sys.argv[2]

# if image_source.startswith("http://") or image_source.startswith("https://"):
#     response = requests.get(image_source)
#     if response.status_code != 200:
#         print("❌ Error: Unable to download image")
#         sys.exit(1)

#     image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
#     image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

# else:
#     if not os.path.exists(image_source):
#         print("❌ Error: File not found")
#         sys.exit(1)

#     image = cv2.imread(image_source)

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

# cv2.imwrite(output_path, image)
# print(f"Face detection complete. Saved to {output_path}")
