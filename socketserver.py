import socket
import sys
import _thread
import threading
HOST = ''  # Symbolic name, meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])

    sys.exit()

print('Socket bind complete')


# Start listening on socket
s.listen(10)
print('Socket now listening')



# Function for handling connections. This will be used to create threads
def clientthread(conn):
    # Sending message to connected client
#     conn.sendall('Welcome to the server. Type something and hit enter\n'.encode('utf-8'))

    # send only takes string
    # infinite loop so that function do not terminate and thread do not end.
    global bufferedrecv
    bufferedrecv = ''
    while True:
        # Receiving from client
        data = conn.recv(1024)
        if not data:
            break
        bufferedrecv += data.decode("utf-8")
#         reply = 'Copy that'
        
#         conn.sendall(reply.encode('utf-8'))

    # came out of loop
    conn.close()
    print(bufferedrecv)


# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    _thread.start_new_thread(clientthread, (conn,))
s.close()

