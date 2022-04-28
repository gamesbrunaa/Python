import threading
import time

class myThread(threading.Thread):

    def __init__(self, nome, contador, delay, sinc):
        super(myThread, self).__init__()
        self.nome = nome
        self.contador = contador
        self.delay = delay
        self.sinc = sinc

    def run(self):
        print("Iniciando" + self.nome)
        self.sinc.acquire()
        self.print_time(self.nome, self.contador, self.delay)
        self.sinc.release()
        print("Finalizando " + self.nome)

    def print_time(self, threadName, contador, delay):
        while contador:
            time.sleep(delay)
            print("{}: {}".format(threadName, time.ctime(time.time())))
            contador -= 1

sinc = threading.Lock()

th1 = myThread('Thread-1', 15, 1, sinc)
th2 = myThread('Thread-2', 15, 1, sinc)

th1.start()
th2.start()

th1.join()
th2.join()

print("Finalizando a thread principal!")