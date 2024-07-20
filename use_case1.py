from main import ProcessSafeClass
from multiprocessing import Process


def worker(obj):
    obj.val = "Hello from process"
    print("In process: ", obj.val)


if __name__ == "__main__":
    a = ProcessSafeClass()
    a.val = 'merhaba'
    print("Main before process: ", a.val)

    p = Process(target=worker, args=(a,))
    p.start()
    p.join()

    print("Main after process: ", a.val)

    a._cleanup()
