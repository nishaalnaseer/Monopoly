import socket, aes, storedInfo
from os import _exit

mode = input("Are you sending('s') or recieving('r') a file? ")

if mode == "s":
    filename = input("Enter filename to transfer: ");
    with open(filename, "r") as f:
        file = f.read()
elif mode == 'r':
    confirm = ""
    while confirm != "y":
        filename = input("Save file as: ")
        if filename[-3:] != ".py":
            filename += ".py"
        confirm = input(f"Save file as {filename}: (y/n) ")
else:
    _exit(0)

key = storedInfo.key()
ecryption = aes.AESCipher(key)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip, port = "172.104.40.56", 12000
homeIp = "69.94.39.86"

client.connect((ip, port))
while True:
    if mode == 'r':
        #  needs decrypting
        encryptedFile = client.recv(8000000, socket.MSG_WAITALL)
        # encryptedFile = encryptedFile.decode("utf-8")
        file = ecryption.decrypt(encryptedFile)
        with open(filename, 'w') as f:
            file = str(file)
            f.write(file)
        print(f"File saved as {filename}")
        break
    else:
        # needs encrypting
        file = ecryption.encrypt(file)
        print("File encrypted")
        client.send(file)
        print('File sent')
        # print(file)
        break

client.close()