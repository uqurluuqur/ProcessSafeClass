from multiprocessing import shared_memory
import pickle

# the class does not use lock, user is responsible in using locks
# todo cannot add methods that does not start with '_'


class ProcessSafeClass:
    def __init__(self):
        # Create shared memory for attribute dictionary
        self._shm = shared_memory.SharedMemory(create=True, size=4096)
        self._initialize_dict()

    def _initialize_dict(self):
        # Initialize an empty dictionary in shared memory
        initial_dict = {}
        encoded_dict = pickle.dumps(initial_dict)
        buffer = self._shm.buf
        buffer[:len(encoded_dict)] = encoded_dict

    def _get_dict(self):
        # Retrieve the dictionary from shared memory
        buffer = self._shm.buf
        encoded_dict = bytes(buffer[:self._shm.size])
        return pickle.loads(encoded_dict)

    def _set_dict(self, dictionary):
        # Store the dictionary in shared memory
        encoded_dict = pickle.dumps(dictionary)
        if len(encoded_dict) > self._shm.size:
            raise ValueError("Shared memory size is too small to hold the dictionary")
            # todo raise the shm size and continue
        buffer = self._shm.buf
        buffer[:len(encoded_dict)] = encoded_dict

    def __getattribute__(self, item):
        if item.startswith('_'):
            return super().__getattribute__(item)
        shm_dict = self._get_dict()
        if item in shm_dict:
            return shm_dict[item]
        else:
            raise AttributeError(f"'ProcessSafeClass' object has no attribute '{item}'")

    def __setattr__(self, attr_name, attr):
        # Custom attribute setting
        if attr_name.startswith('_'):
            super().__setattr__(attr_name, attr)
        else:
            shm_dict = self._get_dict()
            shm_dict[attr_name] = attr
            self._set_dict(shm_dict)

    def _cleanup(self):
        # Clean up shared memory
        self._shm.close()
        self._shm.unlink()





