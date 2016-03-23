from messaging_client.messaging_client import MessagingClient

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8700


class App():

    def __init__(self):
        self.client = MessagingClient()
        self.values = self.client.parse_command_line()

    def _get_host(self):
        try:
            host = self.values['host']
        except KeyError:
            host = DEFAULT_HOST
        return host

    def _get_port(self):
        try:
            port = self.values['port']
        except KeyError:
            port = DEFAULT_PORT
        return port

    def run(self, listen_first=False):
        host = self._get_host()
        port = self._get_port()
        print("Connecting to '" + host + ":" + str(port) + "'...\n")
        self.client.connect(host, port)
        if listen_first:
            response = self.client.receive_response()
            print(response)
        print("Sending message...")
        self.client.send_file_message(self.values['file'])
        response = self.client.receive_response()
        print("Received response:")
        print(response)
        self.client.close()


def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
