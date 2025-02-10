import face_recognition

known_image = face_recognition.load_image_file("known_face.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

unknown_image = face_recognition.load_image_file("unknown_face.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([known_encoding], unknown_encoding)

if results[0]:
  print("✅ Face Match Found!")
else:
  print("❌ No Match Found!")