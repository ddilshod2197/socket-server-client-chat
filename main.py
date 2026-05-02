import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

    def handle_client(self, conn, addr):
        while True:
            try:
                message = conn.recv(1024)
                if not message:
                    break
                print(f"[{addr}] {message.decode()}")
                conn.send(message)
            except:
                break
        print(f"[{addr}] disconnected")
        conn.close()

    def start(self):
        print(f"Server started on {self.host}:{self.port}")
        while True:
            conn, addr = self.server.accept()
            print(f"[{addr}] connected")
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def send_message(self, message):
        self.client.send(message.encode())

    def receive_message(self):
        return self.client.recv(1024).decode()

    def start(self):
        while True:
            message = input()
            self.send_message(message)
            print(self.receive_message())

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345

    server = Server(host, port)
    server.start()

    client = Client(host, port)
    client.start()
```

Server va Client klasslari yaratilib, ularni ishga tushirish uchun start metodlari yozilgan. Server klassida, server socket yaratilib, u uni listen modda qoldiradi. Klient klassida, client socket yaratilib, u server bilan connect qiladi. Server va Client klasslari o'zaro aloqada bo'lish uchun threading yordamida ishlaydi.
