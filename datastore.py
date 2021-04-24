import time


data = {}


def create(key, value, timeout=0):
    """
    Performs create operation.

    Performs create key-value operation of file based key-value data store.

    Args:
        key (str): The key to be stored in data store. Should not exceed
            32 characters.
        value (JSON object): The value to be stored in data store. Should not
            exceed 16KB.
        timeout (int, optional): If provided, it will be evaluated as an
            integer defining the number of seconds the key must be retained in
            the data store. Once the Time-To-Live for a key has expired, the
            key will no longer be available for Read or Delete operations.
    """
    if key in data:
        print("error: Key already exists.")
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
                        print("error: Key size should not exceed"
                              "32 characters.")
                else:
                    print("error: Value size should not exceed 16KB.")
            else:
                print("error: Memory limit exceeded.")
        else:
            print("error: Key should be a string.")


def read(key):
    """
    Performs read operation.

    Performs read value operation of file based key-value data store.

    Args:
        key (str): The key whose value is required to be returned to user.

    Returns:
        json_obj (JSON Object): The value corresponding to given key as a
            JSON Object.
    """
    if key not in data:
        print("error: Entered key doesn't exist in data store."
              "Enter a valid key.")
    else:
        res_value = data[key]
        if res_value[1] != 0:
            if time.time() < res_value[1]:
                json_obj = str(key) + ":" + str(res_value[0])
                return json_obj
            else:
                print("error: Time-To-Live for", key, "has expired.")
        else:
            json_obj = str(key) + ":" + str(res_value[0])
            return json_obj


def delete(key):
    """
    Performs delete operation.

    Performs delete key-value pair of given key operation of file based
    key-value data store.

    Args:
        key (str): The key whose key-value pair is required to be deleted by
            user.
    """
    if key not in data:
        print("error: Entered key doesn't exist in data store."
              "Enter a valid key.")
    else:
        del_value = data[key]
        if del_value[1] != 0:
            if time.time() < del_value[1]:
                del data[key]
                print("Key successfully deleted.")
            else:
                print("error: Time-To-Live for", key, "has expired.")
        else:
            del data[key]
            print("Key successfully deleted.")
