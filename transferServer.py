import socket, aes, info, os, tools

key = info.key()
encryption = aes.AESCipher(key)

def _send(client, msg):
    # c is client
    encryptedMsg = encryption.encrypt(msg)
    client.send(encryptedMsg)

def _recieve(client, buffer=10240):
    try:
        encryptedMsg = client.recv(buffer)
        msg = encryption.decrypt(encryptedMsg)
    except ValueError as e:
        print(e)
        print("Client code might have been editted and nothing is being sent")
    except Exception as e:
        print(e)

    return msg

excluded_files = [
    # no point in transfering these and some may cause issues
    "server", "act.bat", "de.bat", "kill.bat", "__pycache__", 
    "transferServer.py"
            ]

server_dir = os.getcwd()
files = os.listdir(server_dir)

for file in files:
    if file in excluded_files:
        files.remove(file)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip, port = "172.104.181.124", 60001
ip = "192.168.100.4"
server.bind((ip, port))
server.listen(1)
print(f"Server is listening on port: {port}, ip: {ip}")

while True:
    client, addr = server.accept()
    home_ips = info.ipList()
    if addr[0] not in home_ips:
        print("UNKOWN IP: {addr[0]} has connected!")
        continue

    mode = _recieve(client, 1024)
    if mode == 'u':
        for file in files:
            message = f"file="
            if file == files[-1]:
                message += "last"
            else:
                message = f"{message} {file}"

            _send(client, message)

            if _recieve(client, 1024) == "OK":
                with open(file, 'r') as f:
                    file_content = f.read()
                    _send(client, file_content)
                print(f"{file} has been sent.")
            else:
                print(f"{file} has been skipped.")

    elif mode == "d":
        contact = _recieve(client, 1024)
        file_name = (tools.separator(contact))[1]
        _send(client, "OK")
        file = _recieve(client)

        with open(file_name, "w") as f:
            f.write(file)
        print(f"{file_name} has been saved.")

server.close()
os._exit(0)
