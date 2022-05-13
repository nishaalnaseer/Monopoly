from os import _exit
import info

key = storedInfo.key()
ipDict = storedInfo.ipHash()

keyq = input("Do you wish to update key?'y' ")

if keyq == 'y':
    key = str(input("Enter new key: "))

inputStatement = "Do you wish to update dict?'y' "
dictq = input(inputStatement)

while dictq == 'y':
    name = input("Input Name: ")
    try:
        ipDict[name]
    except KeyError:
        check = input("Entry doesnt exist. Do you wish create a new one with that name?'y' ")
        if check == 'y':
            pass
        else:
            break

    yourIP = str(input("Enter your IP: "))
    ipDict.update({name: yourIP})

    inputStatement = "Do you wish to update dict again?'y' "
    dictq = input(inputStatement)

file = f'def key():\n    return "{key}"\n\nipDict = {ipDict}\n\ndef ipList():\n    ipList = []\n    for k, v in ipDict.items():\n        ipList.append(v)\n    return ipList\n\ndef ipHash():\n    return ipDict'

with open("info.py", 'w') as f:
    f.write(file)

