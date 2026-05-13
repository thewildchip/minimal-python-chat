#!/usr/bin/env python3
import socket
import sys
import argparse


def send(msg, goal):
    print("Started")
    try:
        with socket.create_connection((goal, 3222)) as c:
            print("2. Step")
            c.sendall(msg.encode())
            print("finished")
    except Exception as e:
        print(f"Send error: {e}")


def listen():
    
    try:
        with socket.create_server(("", 3222)) as s:
            print("Listening on port 3222...")
            while True:
                conn, addr = s.accept()
                with conn:
                    rmsg = conn.recv(4096)
                    if rmsg:
                        print(f"{addr}: {rmsg.decode()}")
    except Exception as e:
        print(f"Listen error: {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  -s <host> <message>   Send message")
        print("  -l                    Listen")
        return

    if sys.argv[1] == "-s":
        if len(sys.argv) != 4:
            print("Usage: -s <host> <message>")
            return
        victim = sys.argv[2]
        msg = sys.argv[3]
        send(msg, victim)

    elif sys.argv[1] == "-l":
        listen()

    else:
        print("Unknown option")


if __name__ == "__main__":
    main()
