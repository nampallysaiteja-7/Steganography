![mypic](https://github.com/user-attachments/assets/1dbd5a3d-70a3-4651-88c1-63cdc86dba1d)
What is Steganography?
Steganography is the practice of hiding a secret message inside something else, like a picture, sound, or video, so no one can see the hidden message unless they know where to look.

In this project, we hide a message inside an image. We change the colors of the image's pixels just a little bit, so the picture still looks normal, but the message is hidden inside it.
There are two parts in this project:

Encryption (Hiding the Message): The secret message is hidden inside the picture. This part changes some of the image's pixel values to store the message.
Decryption (Getting the Message Back): The hidden message is retrieved from the picture. You need the correct password to see the message.

Step-by-Step Process:

1. Hiding the Message (Encryption):
Step 1: Choose a picture (e.g., mypic.jpg) and the message you want to hide (e.g., "Hello, World!").
Step 2: Enter the message and a password into the encryption program.
Step 3: The program will make small changes to the picture, hiding each letter of your message in the colors of the pixels.
Step 4: The result will be a new picture (Encryptedmsg.jpg). The picture looks the same, but the secret message is hidden inside it.

3. Getting the Message Back (Decryption):
Step 1: Open the new picture (Encryptedmsg.jpg) and enter the correct password.
Step 2: If the password is correct, the program will scan the pixels of the picture and get the hidden message.
Step 3: The message you hid, like "Hello, World!", will be shown.
