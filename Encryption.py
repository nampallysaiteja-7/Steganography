import cv2
import os

def encrypt_message_in_image(image_path, message, password):
    img = cv2.imread(image_path)
    d = {}

    for i in range(255):
        d[chr(i)] = i

    m = 0
    n = 0
    z = 0


    for i in range(len(message)):
        img[n, m, z] = d[message[i]]  # Modify the pixel value
        n = n + 1
        m = m + 1
        z = (z + 1) % 3  # Cycle through the RGB channels

    
    encrypted_image_path = "Encryptedmsg.jpg"
    cv2.imwrite(encrypted_image_path, img)

  
    os.system(f"start {encrypted_image_path}")
    print("Message encrypted and saved in Encryptedmsg.jpg")

    return encrypted_image_path, password

msg = input("Enter secret message: ")
password = input("Enter password: ")


encrypt_message_in_image("mypic.jpg", msg, password)
