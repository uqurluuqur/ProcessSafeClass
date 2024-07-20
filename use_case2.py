from main import ProcessSafeClass
from multiprocessing import Process

# todo cannot add methods that does not start with '_'


class NewClass(ProcessSafeClass):
    def __init__(self):
        super().__init__()
        self.init_val = "Initial Value"

    def _multiply(self, value):
        print('class function', value*value)


def worker(obj):
    obj.aa = "Hello from process"
    obj.init_val = "Initial Value edited"
    print("In process: ", obj.aa)


if __name__ == "__main__":
    obj = NewClass()
    obj.aa = 'Main Value'
    print("Main before process: ", obj.aa)
    print('init value:', obj.init_val)

    p = Process(target=worker, args=(obj,))
    p.start()
    p.join()

    print("Main after process: ", obj.aa)
    print('init value:', obj.init_val)

    obj._multiply(2)

    obj._cleanup()
