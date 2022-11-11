
import socket
import os
import time

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


# dynamically defining the ip
#server_ip = socket.gethostbyname(socket.gethostname())
#print(type(server_ip))

# randomly assigned port
server_ip = "10.0.0.1"
port_no = 50505
addr_tuple = (server_ip, port_no)

# creating the socket
# fixing the location of server, binding the server
start = time.process_time()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(addr_tuple)
# AF_INET --- address family of IPv4
# SOCK_STREAM --- connection oriented tcp protocol

print("[RUNNING] Server running at IP =", server_ip, " and port number =", port_no)
# print("Server socket successfully created")

server_socket.listen()
print("[LISTENING] server is listening...  ")

conn, addr = server_socket.accept()
print("[CONNECTION SUCCESSFUL] Server accepts the connection of client at", addr)

result = "starting"

# while for persistent connection
flag = 0
while flag != 1:
    packet_received = conn.recv(packetSize).decode(format_)
    #print("The packet received at the server is ", packet_received)
    print("packet received at server")
    packet_received = decryption(packet_received) # decrypting the received message
    crypto_layer_format = packet_received[0]
    
    packet_received = packet_received[1:].split() # removing the crypto latyer format
    current_command = packet_received[0]
    print(f"[RECEIVED] {current_command} commnad at Server")

    if current_command == "CWD":
        result = os.getcwd() # get current working directory

    elif current_command == "LS":
        result_list = os.listdir(os.getcwd()) # list the directory
        result = " ".join(result_list)

    elif current_command == "UPD":
        filename = packet_received[1]
        print("File Location", os.getcwd())
        new_file = open(filename, 'w')
        new_file.write(" ".join(packet_received[2:]))
        new_file.close()
        result = "[OK]"

    elif current_command == "CD":
        list_of_dir = os.listdir(os.getcwd())
        if packet_received[1] in list_of_dir:
            ob.chdir(packet_received[1]) # change directory
            result = "[OK]"
        else:
            result = "[NOK] File not found"

    elif current_command == "DWD":
        list_of_dir = os.listdir(os.getcwd())
        if packet_received[1] in list_of_dir:
            filename = packet_received[1]
            new_file = open(filename, 'r')
            data_in_file = new_file.read()
            result = filename + " " + data_in_file

        else:
            result = "[NOK] File not found"

    elif current_command == "exit()":
        result = packet_received[0]
        flag = 1

    else:
        result = "Command Not Found"

    result = encryption(crypto_layer_format + result)
    conn.send(result.encode(format_))
    print("[SENT] Server sent response to client")
    flag = 1

# closing the socket
server_socket.close()
print("[CLOSED] server connection closed")
finish = time.process_time()
print("Start Time: ", start)
print("Finish Time: ", finish)
print("CPU Time: ", finish-start)
