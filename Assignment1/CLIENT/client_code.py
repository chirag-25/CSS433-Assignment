
import socket
import os

format_ = "utf-8"
packetSize = 1024

# cryto mpode 2 defination : Substitute
def substituteEncryption(a):
    ans = ""

    for i in range(len(a)):
        asciiValue = ord(a[i])
        if asciiValue >= 48 and asciiValue <= 57:
            ans = ans + chr(48 + (asciiValue - 48 + 2) % 10)
        elif asciiValue >= 65 and asciiValue <= 90:
            ans = ans + chr(65 + (asciiValue - 65 + 2) % 26)
        elif asciiValue >= 97 and asciiValue <= 122:
            ans = ans + chr(97 + (asciiValue - 97 + 2) % 26)
        else:
            ans = ans + a[i]
    return ans
def substituteDecryption(a):
    ans = ""
    for i in range(len(a)):
        asciiValue = ord(a[i])

        if asciiValue >= 48 and asciiValue <= 57:
            ans = ans + chr(48 + (asciiValue - 48 - 2) % 10)
        elif asciiValue >= 65 and asciiValue <= 90:
            ans = ans + chr(65 + (asciiValue - 65 - 2) % 26)
        elif asciiValue >= 97 and asciiValue <= 122:
            ans = ans + chr(97 + (asciiValue - 97 - 2) % 26)
        else:
            ans = ans + a[i]
    return ans

# crypto mode 3 definatio: transpose
def transposeEncryption(a):
    tempList = a.split()
    for i in range(len(tempList)):
        tempList[i] = tempList[i][::-1]
    st = ' '.join(tempList)
    return st
def transposeDecryption(a):
    tempList = a.split()
    for i in range(len(tempList)):
        tempList[i] = tempList[i][::-1]
    st = ' '.join(tempList)
    return st

# checking which encryption and decryption
def encryption(a):
    if a[0] == "1":
        return a
    elif a[0] == "2":
        return a[0] + substituteEncryption(a[1:])
    else:
        return a[0] + transposeEncryption(a[1:])
def decryption(a):
    if a[0] == "1":
        return a
    elif a[0] == "2":
        return a[0] + substituteDecryption(a[1:])
    else:
        return a[0] + transposeDecryption(a[1:])


print("[RUNNING] Client started running")

# server_ip = socket.gethostbyname(socket.gethostname())
# port_no = 5050
server_ip = input("IP address of the host - ")
port_no = int(input("Port no of the host - "))
server_location = (server_ip, port_no)

# creating the socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET --- address family of IPv4
# SOCK_STREAM --- connection oriented tcp protocol


print("[CREATED] clinet socket successfully created")

client_socket.connect(server_location)
print("[REQUESTING] client requesting for connection")


# setting the server response to null initailly
server_response = "NULL"

# asking for the crpto layer
crypto_layer_format = input("Which cypto mode you want to use ")

# while loop to make the connection persistent
while 1:

    # user input
    current_ins = input('User command - ').split()
    current_command = current_ins[0]
    print(f"[SENDING] {current_command} commnad to Server")

    if current_command == "UPD":
        filename = current_ins[1]       
        if filename not in os.listdir(os.getcwd()): # checking whether the file is present on the client
            print("[NOK] File not found at the client")
            continue
                
        file = open(filename, 'r') # reading the file
        data_in_file = file.read()
        
        sending_string = crypto_layer_format + current_command + " " + filename + " " + data_in_file
        sending_string = encryption(sending_string) # applying the crypto layer
        print("Sending packet to the server ", sending_string)
        client_socket.send(sending_string.encode(format_)) # sending the packet

    elif current_command == "DWD":
        filename = current_ins[1]
        sending_string = crypto_layer_format + current_command + " " + filename
        sending_string = encryption(sending_string) # crypto layer
        print("Sending packet to the server ", sending_string)
        client_socket.send(sending_string.encode(format_)) # sending packet

        server_response = decryption(client_socket.recv(packetSize).decode(format_)) # decrypting the sent message
        server_response = server_response[1:].split()
        filename = server_response[0]
        if filename == "[NOK]":
            print("[NOK] File Not Found on the server")
        else:
            new_file = open(filename, 'w') # creating the file
            new_file.write(" ".join(server_response[1:]))
            new_file.close()
            print(filename, "downloaded successfully")
        continue
    else: # not to worry to send the name of the file in the rest of the command
        sending_string = " ".join(current_ins)
        sending_string = crypto_layer_format + sending_string
        sending_string = encryption(sending_string) # encrypting the layer
        print("Sending packet to the server ", sending_string)
        client_socket.send(sending_string.encode(format_)) # sending the packet

    if current_command != "DWD": # decrypting responde is handled above
        server_response = decryption(client_socket.recv(packetSize).decode(format_))
        print("[RESPONSE] server response:", server_response[1:])
        if server_response[1:] == "exit()":
            break

# closing the socket
client_socket.close()
print("[CLOSED] Clinet connection closed")
