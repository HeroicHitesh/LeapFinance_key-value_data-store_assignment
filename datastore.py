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


def read(key):
    if key not in data:
        print("error: entered key doesn't exist in data store. Enter a valid key")
    else:
        res_value = data[key]
        if res_value[1] != 0:
            if time.time() < res_value[1]:
                json_obj = str(key) + ":" + str(res_value[0])
                return json_obj
            else:
                print("error: Time-To-Live for", key, "has expired")
        else:
            json_obj = str(key) + ":" + str(res_value[0])
            return json_obj
