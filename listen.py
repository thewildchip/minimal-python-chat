import socket
import sys
import argparse

BUFSIZE = 4096
DEFAULT_PORT = 3222

def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="specify port to listen on")

    args = parser.parse_args()

    listen(args.port)



def listen(port: int) -> None:

    try:
        with socket.create_server(("", port)) as s:
            print(f"Listening on port {port}...(You can exit this with ^C to stop the programm, use pkill)")
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
