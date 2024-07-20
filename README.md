This class enables sharing attributes between processes. In a traditional object, when it is sent to a process, a copy of the object is created. When an attribute is changed, only the process that has the copy sees the changes. This class uses [multiprocessing.shared_memory](https://docs.python.org/3/library/multiprocessing.shared_memory.html#module-multiprocessing.shared_memory)' to store the attributes in a shared memory so that every process can see the current versions of attributes.

It has two use cases:
1) It can directly be used as a shared_memory wrapper.
2) It can be inherited by another class. However, currently in this use case, every method of the class should start with an underscore ("_").

This class does not include internal locking mechanisms. Users should use Python’s multiprocessing.Lock() to not to face any concurrency problems.
