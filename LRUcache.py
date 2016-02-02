# test implementation of LRU cache.
from collections import OrderedDict


class LRUCache(object):
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__cache = OrderedDict()

    def set(self, key, value):
        try:
            self.__cache.pop(key)
        except KeyError:
            if len(self.__cache) >= self.__capacity:
                self.__cache.popitem(last=False)
        self.__cache[key] = value

    def get(self, key):
        try:
            value = self.__cache.pop(key)
            self.__cache[key] = value
            return value
        except KeyError:
            return -1

    def get_cache_details(self):
        return self.__cache


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.set('name', 'john')
    cache.set('age', '12')
    print cache.get_cache_details()
    cache.set('name', 'doey')
    print cache.get_cache_details()
    print cache.get('age')
    print cache.get_cache_details()
    cache.set('aaa', 'aaaaa')
    print cache.get_cache_details()
    print cache.get('age')
    print cache.get_cache_details()
