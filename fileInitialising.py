import socket, storedInfo

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip, port = "172.104.181.124", 50000

# seerver

# server.bind((ip, port))
# server.listen(1)

# while True:
#     client, addr = server.accept()
#     homeIps = storedInfo.ipList()
#     print(homeIps)
#     if addr[0] not in homeIps:
#         print("FUCK")
#         break

#     file = client.recv(100000, socket.MSG_WAITALL)
#     file = file.decode("utf-8")
#     break

# with open("aes.py", 'w') as f:
#     f.write(file)

# client

filename = str(input("Enter filename to transfer: "))
with open(filename, 'r') as f:
    file = f.read()


client.connect((ip, port))
client.send(file.encode("utf-8"))