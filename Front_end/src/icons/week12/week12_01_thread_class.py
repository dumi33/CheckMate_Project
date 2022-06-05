import threading
import time


class Worker(threading.Thread):  # threading 모듈의 Thread 클래스를 상속
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'작업 스레드 시작 : {threading.currentThread().getName()}')
        time.sleep(3)
        print(f'작업 스레드 끝 : {threading.currentThread().getName()}')


if __name__ == "__main__":
    print('메인 스레드 시작')
    for i in range(3):
        t = Worker(f'{i}번 스레드')
        t.start()  # 스레드를 runnable
    print('메인 스레드 끝')



