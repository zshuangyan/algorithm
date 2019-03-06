import random

HOSTS = ['gs-server-3238', 'gs-server-4171', 'gs-server-5693']

class LoadBalancer:
    def __init__(self, backends: list):
        if not backends:
            raise ValueError("backends is empty")
        self.backends = backends
        self.poll_index = 0

    def poll(self):
        try:
            backend = self.backends[self.poll_index]
        except IndexError:
            raise

        if self.poll_index == len(self.backends) - 1:
            self.poll_index = 0
        else:
            self.poll_index += 1
        
        return backend

    def random(self):
        index = random.randint(0, len(self.backends)-1)
        return self.backends[index]

    def hash_by_source(self, source:str):
        hash_value = hash(source)
        index = hash_value % len(self.backends)
        return self.backends[index]


if __name__ == "__main__":
    print("主机列表:", HOSTS)
    lb = LoadBalancer(HOSTS)
    for i in range(5):
        print("第%s次轮询, 返回主机: %s" % (i+1, lb.poll()))
    for i in range(5):
        print("第%s次随机, 返回主机: %s" % (i+1, lb.random()))
    sources = ("192.168.11.12", "192.168.11.19")
    for i in range(2):
        for j in range(2):
            print("第%s次基于源地址hash, 源: %s对应主机: %s" % (i+1, sources[j], lb.hash_by_source(sources[j])))

        
