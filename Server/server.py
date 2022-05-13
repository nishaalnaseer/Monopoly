import socket, aes, tools, os, time, game, threading, info, users

serverIp, port = "127.0.0.1", 36969

def exitCommand():
    os._exit(0)
    server.close()

def helpCommand():
    for command, info in commands.items():
        print(f"'{command}': {info[0]}")

commands = {
    "exit": ["Stop server", exitCommand],
    "help": ["Display all avaiable commands", helpCommand]
    }
def console():
    global inp
    while True:
        inp = str(input("Enter command: "))

        try:
            commandInfo = commands[inp]
            commandFunc = commandInfo[1]
        except KeyError:
            print("Key Not Found in Dict")
        else:
            commandFunc()

        print("")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((serverIp, port))
server.listen(1)
print(f"Server is listening on port: {port}. IP: {serverIp}")

key = storedInfo.key()
encryption = aes.AESCipher(key)

consoleThread = threading.Thread(target=console)
consoleThread.start()

def send(c, msg):
    # c is client
    encryptedMsg = encryption.encrypt(msg)
    c.send(encryptedMsg)

def recieve(c):
    try:
        encryptedMsg = c.recv(10240)
        msg = encryption.decrypt(encryptedMsg)
    except ValueError as e:
        print(e)
        print("Client code might have been editted and nothing is being sent")
    except Exception as e:
        print(e)

    return msg

newUsers = {}

while True:
    client, address = server.accept()
    if address[0] in storedInfo.ipList():  # if ip in list proceed
        send(client, "in")
        userData = recieve(client)

        args = tools.separator(userData)
        if len(args) > 2:  # if more than 2 args are in text because " " is used as a separator
            send(client, "code0001:f")
        elif len(args) < 2:
            send(client, "code0003:f")
        else:
            username = args[0]
            password = args[1]
            userCheck = users.userCheck(username)

            if userCheck != 1:
                send(client, userCheck)
            else:
                send(client, users.logged(username, password, 'a'))

        print(args)