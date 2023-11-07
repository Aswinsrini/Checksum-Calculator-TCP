import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.bind(('localhost', 12345))
tcp.listen(1)
buff_size = 2004
print("TCP Client Waiting for the connection...")
connection, add = tcp.accept()
print("connected to address: ", add)


def ones_complement(data):
    res = ""
    for ele in data:
        if ele == '1':
            res += '0'
        else:
            res += '1'
    k = int(res, 2)
    if k <= 9:
        k = str(k)
    elif k == 10:
        k = 'A'
    elif k == 11:
        k = 'B'
    elif k == 12:
        k = 'C'
    elif k == 13:
        k = 'D'
    elif k == 14:
        k = 'E'
    elif k == 15:
        k = 'F'
    print("The calculated checksum is : ", k)
    return k


def calculate_md5_checksum(data):
    initial = 0
    for ele in data:
        if ele == 'A':
            initial += 10
        elif ele == 'B':
            initial += 11
        elif ele == 'C':
            initial += 12
        elif ele == 'D':
            initial += 13
        elif ele == 'E':
            initial += 14
        elif ele == 'F':
            initial += 15
        else:
            initial += int(ele)
    if initial <= 15:
        initial = bin(initial)[2:].zfill(4)
        return ones_complement(str(initial))
    else:
        last = int(bin(initial)[-4:], 2)
        first = int(bin(initial)[2:][:-4], 2)
        final = bin(first + last)[2:]
        return ones_complement(str(final))
    return "ok"


while True:
    data = connection.recv(buff_size).decode()
    if data == "close":
        print("Application terminated successfully...")
        break
    else:
        connection.send(calculate_md5_checksum(data).encode())

connection.close()
tcp.close()
