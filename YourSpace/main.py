import cv2
from tkinter import *
import face_recognition
import os
import glob
import webbrowser
from crypto import encrypt_directory, decrypt_directory, encrypt, decrypt, write_key
import psutil

def create_folder(username):
    path = f"spaces\\{username}"
    os.mkdir(path)
    print(f"Creating {username}'s space")



def create_current_frame_as_img(frame, filename):
    img_place = f"saved_img\\{filename}.png"
    cv2.imwrite(img_place, frame)
    return img_place



def load_encrypted_image(img_place, username):
    """
    Loading user image while trying to keep it encrypted
    """
    decrypt(img_place, username)
    image = face_recognition.load_image_file(img_place)
    encrypt(img_place, username)
    return image



def username_exist(username, text = True):
    """
    * Text = True == print the result

    if entered username exist:
        return True
    else:
        return False
    """
    if not os.path.exists(f"spaces\\{username}") or username=="":
        if text:
            print("The entered username was not found")
        return False
    return True



def get_user_input():
    """
    Loops until user enters a value above 3 characters
    """
    root = Tk()

    def retrieve_input():
        global txt
        inputValue = textBox.get("1.0", "end-1c")
        if len(inputValue) > 3:
            txt = inputValue.split("\n")[0]
            root.destroy()

    textBox = Text(root, height=2, width=10)
    textBox.pack()
    buttonCommit = Button(root, height=1, width=10, text="Commit", command=lambda: retrieve_input())
    # command=lambda: retrieve_input() >>> just means do this when I press the button
    buttonCommit.pack()

    mainloop()

    #check if txt exist
    try:
        txt
    except:
        return ""
    return txt




# Waits until file explorer is closed
def while_file_explorer_is_opened(username):
    """
    Check the current number of File Explorer's handlers
    When it is changed we can detect when the user exited file explorer
    """

    handlesPrevious = 0
    usualIncrease = 100

    # Check the current number of File Explorer's handlers
    for proc in psutil.process_iter():
        if 'explorer' in proc.name():
            handlesPrevious = proc.num_handles()

    print("Opening user's space")
    webbrowser.open(f"spaces\\asaf")
    # Detects if the user exit's the file his space
    while 1:
        for proc in psutil.process_iter():
            if 'explorer' in proc.name():
                handlesCurrent = proc.num_handles()
                if (handlesPrevious + usualIncrease) <= handlesCurrent:

                    handlesPrevious = handlesCurrent
                elif (handlesPrevious - usualIncrease) > handlesCurrent:
                    print("User exited his space")
                    handlesPrevious = handlesCurrent
                    return



def does_face_exist(img_place):
    check_image = face_recognition.load_image_file(img_place)
    try:
        # checking if same face
        check_image_encoding = face_recognition.face_encodings(check_image)[0]
        face_recognition.compare_faces([check_image_encoding], check_image_encoding)
    except:
        # if it crashes it means that in the chk picture a face was not found -> cant check if same face -> False
        print("Face was not found")
        return False
    return True


def is_same_face(frame):
    """
    Check if current frame has the same face as the typed username
    if user current camera captured frame matches the entered username image:
        return True, username
    Else:
        return False, ""
    """

    # get username from user
    username = get_user_input()
    # check if enter username exist
    if not username_exist(username):
        return False, ""

    # create current frame as a temporary saved img to compare images
    temp_img_place = create_current_frame_as_img(frame, filename="chk")
    # check if there is a face in the taken frame
    if not does_face_exist(temp_img_place):
        return False, ""

    # loads check image
    check_image = face_recognition.load_image_file(temp_img_place)
    # deleting the saved check img as it is no longer needed
    os.remove(temp_img_place)

    # loading user image while keeping it encrypted
    user_image = load_encrypted_image(f"saved_img\\{username}.png",username)

    # checking if same face
    check_image_encoding = face_recognition.face_encodings(check_image)[0]
    user_image_encoding = face_recognition.face_encodings(user_image)[0]
    results = face_recognition.compare_faces([check_image_encoding], user_image_encoding)

    print(results)
    return results, username



def main():
    # define a video capture object
    vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Check whether user selected camera is opened successfully.

    if not (vid.isOpened()):
        print("Couldn't find a camera device")
        return
    print("Found camera, Showing camera view")

    print("""Key Commands:
    ESC - Exit program
    Space - Create an account
    Enter - Enter account
    D Key - Delete account (user must have the username face)""")

    while True:

        # try to get to get camera and keyboard input - if suddenly stopped - the program won't crash
        try:
            # Capture the video frame by frame
            ret, frame = vid.read()

            # Display the resulting frame
            cv2.imshow('Camera', frame)

            # k = keys in ascci code
            k = cv2.waitKey(1)

        except:
            # if suddenly program stopped, exit program
            print("Closing program...")
            break

        if k % 256 == 27:
            # ESC pressed = exit program
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed = Saving image - Creating new space
            username = get_user_input()
            if username_exist(username, text=False): # Text = False == not to print the result
                print("Username taken... try again")
            else:
                # Create user's current frame as an image
                img_place = create_current_frame_as_img(frame, filename=username)
                # if face does not exist in the taken picture, an acount won't be made
                if does_face_exist(img_place):
                    # Create user's space
                    create_folder(username)
                    # Create user's key
                    write_key(username)
                    # Encrypt user's image for privacy
                    encrypt(img_place, username)
        elif k % 256 == 13:
            # ENTER pressed = Entering your space - Creating new space
            sameface, username = is_same_face(frame)
            if sameface:
                # Decrypt the user files back to normal files
                decrypt_directory(username)
                # checks and waits untill the user exits his space
                while_file_explorer_is_opened(username)
                # Encrypt the user files and image back to being encrypted
                encrypt_directory(username)
        elif k % 256 == 100:
            # D Key pressed = delete username
            # Delete user from system (user must have the username face)
            sameface, username = is_same_face(frame)
            if sameface:
                # Deleting user's space and its files
                files = glob.glob(f'spaces\\{username}\\*')
                for f in files:
                    os.remove(f)
                os.rmdir(f"spaces\\{username}")
                # Deleting user's key and image
                os.remove(f"saved_img\\{username}.png")
                os.remove(f"keys\\{username}.png")

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
