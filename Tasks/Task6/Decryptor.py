import os

import AES_realisation


def main():
    password = ""
    with open("shaKeys", "r") as passwordFile:
        password = passwordFile.readLine()
    password = AES_realisation.getKey(password)

    for root, dirs, files in os.walk("C:\\TestFolder", topdown=True):
        if (str(root).__contains__("System32")):
            continue
        else:
            for fileName in files:
                filePath = root + "\\" + fileName
                AES_realisation.decrypt(password, filePath)


if __name__ == "__main__":
    main()