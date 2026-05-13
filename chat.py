#!/usr/bin/env python3
import argparse
import socket

DEFAULT_PORT = 3222
BUFSIZE = 4096


def main() -> None:
    
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="mode", required=True)
    
    send_parser = subparser.add_parser("send", help="send a message to another computer")
    send_parser.add_argument("host", help="IPv4 of host computer")
    send_parser.add_argument("message", help="message that will be sent")
    send_parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="specify host port")
    
    listen_parser = subparser.add_parser("listen", help="listen for incoming connections")
    listen_parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="specify port to listen on")
    
    args = parser.parse_args()
    
    
    if args.mode == "send":
        send(args.host, args.message, args.port)

    elif args.mode == "listen":
        listen(args.port)

    else:
        print("Unknown option")



def send(host: str, message: str, port: int) -> None:
    print("Started")
    try:
        with socket.create_connection((host, port)) as c:
            print("2. Step")
            c.sendall(message.encode())
            print("finished")
    except Exception as e:
        print(f"Send error: {e}")



def listen(port: int) -> None:
    
    try:
        with socket.create_server(("", port)) as s:
            print(f"Listening on port {port}...")
            while True:
                conn, addr = s.accept()
                with conn:
                    rmsg = conn.recv(BUFSIZE)
                    if rmsg:
                        print(f"{addr}: {rmsg.decode()}")

    except Exception as e:
        print(f"Listen error: {e}")



if __name__ == "__main__":
    main()
    