import cv2

def decrypt_message_from_image(image_path, password):
    img = cv2.imread(image_path)
    c = {}

    # Generate a dictionary for decoding pixel values back to characters
    for i in range(255):
        c[i] = chr(i)

    message = ""
    n = 0
    m = 0
    z = 0

    # Ask for the password
    pas = input("Enter password for Decryption: ")

    # Check if the password matches
    if password == pas:
        # Extract the embedded message from the image
        for i in range(100):  # Assuming the message is up to 100 characters
            # Retrieve the pixel's value and convert it back to a character
            message += c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3  # Cycle through RGB channels

        print("Decrypted message:", message)
    else:
        print("Invalid password! Unable to decrypt.")

# Input
password = input("Enter password for decryption: ")

# Decrypt the message from the encrypted image
decrypt_message_from_image("Encryptedmsg.jpg", password)
