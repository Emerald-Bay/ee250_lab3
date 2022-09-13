"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():

    HOST = "20.38.171.207"
    PORT = 8080
    
    # TODO: Create a socket and connect it to the server at the designated IP and port
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # TODO: Get user input and send it to the server using your TCP socket
    
    message = input("Please type in the message you want to send to the server: ")
    client.send(message.encode())

    # TODO: Receive a response from the server and close the TCP connection

    response = client.recv(256)
    print(response)

    client.close()

if __name__ == '__main__':
    main()
