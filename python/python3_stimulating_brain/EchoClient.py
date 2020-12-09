import socket
import sys


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("{0} <Bind IP> <Server IP> <Message>".format(sys.argv[0]))
        sys.exit()

    filename, bindIP, serverIP, message = tuple(sys.argv)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM은 TCP socket을 의미
    sock.bind((bindIP, 0))

    try:
        sock.connect((serverIP, 5425)) # 연결 요청 수행

        # 메아리 송신
        sbuff = bytes(message, encoding="utf-8")
        sock.send(sbuff) # 메시지 송신부
        print("송신: {0}".format(message))
        
        # 메아리 수신
        rbuff = sock.recv(1024) # 메시지 수신부
        received = str(rbuff, encoding="utf-8")
        print("수신: {0}".format(received))

    finally:
        sock.close()