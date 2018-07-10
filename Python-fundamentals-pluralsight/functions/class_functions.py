import socket

class Resolver:

    def __init__(self):
        self._cache={}

    def __call__(self,host):
        if host not in self._cache:
            self._cache[host]= socket.gethostbyname(host)
        return self._cache[host]
    
    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache

    
if __name__ == '__main__':
    resolve = Resolver()
    print(resolve('pluralsight.com'))
    print(resolve.__call__('pluralsight.com'))
    print(resolve._cache)
    resolve('datacamp.com')
    print(resolve._cache)