import threading
import asyncore
total = 0


class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        global total
        data = self.recv(2048)
        if data:
            total += 1
            print(total)
            try:
                print(data.encode("utf-8"))
                self.handle_close()
            except Exception as e:
                print(e)


class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))
        handler = EchoHandler(sock)


server = EchoServer('0.0.0.0', 9090)


loop_thread = threading.Thread(target=asyncore.loop, name="Asyncore Loop")
# If you want to make the thread a daemon
# loop_thread.daemon = True
loop_thread.start()


# asyncore.loop()
print("end")
