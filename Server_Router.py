class Server:
    ip = 0

    def __new__(cls, *args, **kwargs):
        cls.ip += 1
        return object.__new__(cls)

    def __init__(self):
        self.ip = Server.ip
        self.buffer = []
        self.buffer_out = []

    def __del__(self):
        if Server.ip != 0:
            Server.ip -= 1
        else:
            raise ValueError('You have not any server')

    def send_data(self, data):
        Router.buffer.append(data)
        # Router.send_data()

    def get_data(self):
        self.buffer.clear()
        return self.buffer_out

    def get_ip(self):
        return self.ip


class Router:
    buffer = []

    servers = []

    @staticmethod
    def link(server):
        Router.servers.append(server)

    @staticmethod
    def unlink(server):
        index = Router.servers.index(server)
        del Router.servers[index]

    @staticmethod
    def send_data():
        for b in Router.buffer:
            for s in Router.servers:
                if s.ip == b.ip:
                    s.buffer.append(b)
                    s.buffer_out.append(b)
        Router.buffer.clear()


class Data:

    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


# Testing
router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
msg_lst_from2 = sv_from2.get_data()
