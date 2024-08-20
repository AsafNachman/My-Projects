

from crypto import decrypt, encrypt
import face_recognition

username = "asaf"
img_place = "saved_img\\asaf.png"

decrypt(img_place, username)
check_image = face_recognition.load_image_file(img_place)
encrypt(img_place, username)

try:
    # checking if same face
    check_image_encoding = face_recognition.face_encodings(check_image)[0]
    face_recognition.compare_faces([check_image_encoding], check_image_encoding)
except:
    # if it crashes it means that in the chk picture a face was not found -> cant check if same face -> False
    print("Face was not found")
    print(False)
print(True)

