import time


data = {}


def create(key, value, timeout=0):
    if key in data:
        print("error: key already exists")
    else:
        if key.isalpha():
            if len(data) < (1024 ** 3):
                if value <= (16 * 1024 ** 2):
                    if timeout == 0:
                        data_value = [value, timeout]
                    else:
                        data_value = [value, time.time() + timeout]
                    if len(key) <= 32:
                        data[key] = data_value
                    else:
                        print("error: key size should not exceed 32 characters")
                else:
                    print("error: value size should not exceed 16KB")
            else:
                print("error: memory limit exceeded")
        else:
            print("error: key should be a string")
