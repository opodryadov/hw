import time


class Timer:

    def __init__(self, name, method):
        self.name = name
        self.method = method

    def __enter__(self):
        self.file_obj = open(self.name, self.method, encoding='utf-8')
        self.start = time.time()
        print('Время начала:', self.start)
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print('Время окончания:', self.start)
        self.interval = self.end - self.start
        print('Времени затрачено:', self.interval)


with Timer('netology.txt', 'r') as file:
    file.read()