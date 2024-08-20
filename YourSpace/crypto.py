

from cryptography.fernet import Fernet
import glob
import zlib
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d


def write_key(username):
    """ Generates a key and save it into a file """
    key = Fernet.generate_key()
    with open(f"keys\\{username}.key", "wb") as key_file:
        key_file.write(key)


def load_key(username):
    """ Loads the key from the current directory named `{name}.key` """
    return open(f"keys\\{username}.key", "rb").read()


def encrypt_or_decrypt(filepath, key, FLAG):
    f = Fernet(key)
    with open(filepath, "rb") as file:
        # read all file data
        file_data = file.read()
    # obscure the data or unobscure the data and then encrypt/decrypt the data
    if FLAG:
        obscured_file_data = obscure(file_data)
        encrypted_data = f.encrypt(obscured_file_data)
        final_data = encrypted_data
    else:
        decrypted_data = f.decrypt(file_data)
        unobscured_file_data = unobscure(decrypted_data)
        final_data = unobscured_file_data
    # write the encrypt/decrypt file
    with open(filepath, "wb") as file:
        file.write(final_data)


def encrypt(filepath, username):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    encrypt_or_decrypt(filepath, load_key(username), FLAG=True)


def decrypt(filepath, username):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    encrypt_or_decrypt(filepath, load_key(username), FLAG=False)


def encrypt_or_crypt_directory(username, FLAG):
    folder_path = f"spaces\\{username}"
    # Get directory filenames
    filepaths = glob.glob(f"{folder_path}\\*")  # [] if no files -> it will not enter the For
    # Encrypt or Decrypt every file in folder
    for path in filepaths:
        try:
            if FLAG:
                encrypt(path, username)
            else:
                decrypt(path, username)
        except:
            pass


def encrypt_directory(username):
    """
    Encrypt all the file in the directory
    """
    encrypt_or_crypt_directory(username, FLAG=True)


def decrypt_directory(username):
    """
    Decrypt all the file in the directory
    """
    encrypt_or_crypt_directory(username, FLAG=False)


def encrypt_the_encrypted_data(data):
    pass


def obscure(data: bytes) -> bytes:
    return b64e(zlib.compress(data, 9))


def unobscure(obscured: bytes) -> bytes:
    return zlib.decompress(b64d(obscured))


def delete():
    import os
    import glob

    username = "asaf"

    files = glob.glob(f'spaces\\{username}\\*')
    for f in files:
        os.remove(f)
    os.rmdir(f"spaces\\{username}")
    os.remove(f"saved_img\\{username}.png")
    os.remove(f"keys\\{username}.key")
    os.remove(f"saved_img\\chk.png")