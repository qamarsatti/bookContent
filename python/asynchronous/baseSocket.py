import asyncio
import time
import socket
HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 9090  # Port to listen on (non-privileged ports are > 1023)

async def call_api(conn):
    data = conn.recv(1024)
    print(data)
    if not data:
        pass
    else:
        conn.sendall(data)
    conn.close()


async def main():