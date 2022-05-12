import socket, storedInfo, aes
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
encryption = aes.AESCipher(key)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip, port = "172.104.40.56", 50000
homeIp = "69.94.39.86"

server.bind((ip, port))
server.listen(1)
print(f"Server listening on port: {port}, ip: {ip}")

while True:
    client, addr = server.accept()
    clientIp = addr[0]
    homeIps = storedInfo.ipList()

    if clientIp not in homeIps:
        print("WARNING WARNING WARNING WARNING WARNING WARNING"*5)
        print("HOME IP DOES NOT MATCH CLIENT IP"*2)
        print("ABORT ABORT ABORT ABORT ABORT ABORT ABORT ABORT"*2)
        print("WARNING WARNING WARNING WARNING WARNING WARNING"*5)
        server.close()
        _exit(0)

    if mode == 'r':
        #  needs decrypting
        encryptedFile = client.recv(8000000)
        file = encryption.decrypt(encryptedFile)
        with open(filename, 'w') as f:
            file = str(file)
            f.write(file)
        print(f"File saved as {filename}")
        break
    else:
        # needs encrypting
        file = encryption.encrypt(file)
        print("File encrypted")
        client.send(file)
        print('File sent')
        break

server.close()
