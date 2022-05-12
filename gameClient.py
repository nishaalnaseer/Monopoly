import socket, aes, tools, os, time, threading, storedInfo

serverIp, port = "127.0.0.1", 36969

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverIp, port))
print(f"Connected to: {serverIp}, port: {port}")

key = storedInfo.key()
encryption = aes.AESCipher(key)

def send(c, msg):
    # c is client
    encryptedMsg = encryption.encrypt(msg)
    c.send(encryptedMsg)

def recieve(c):
    encryptedMsg = c.recv(10240)
    msg = encryption.decrypt(encryptedMsg)
    return msg

fromServer = recieve(client)

if fromServer == "in":
    username = input("Enter username: ")
    password = input("Enter password: ")
    msg = username + " " + password
    send(client, msg)
else:
    print(msg)