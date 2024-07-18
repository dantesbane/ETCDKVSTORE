# run etcd.exe first in terminal 1
# set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python in terminal 2
# run python script.py in terminal 2

import etcd3


def list_all_keys(etcd):
    key_list = list(etcd.get_all())
    if len(key_list) == 0:
        print("\nNo keys present!")
    else:
        print("\nList of Keys:")
        for i in key_list:
            print(i[1].key.decode("utf-8"))


def get_key_and_print_value(etcd):
    key_list = list(etcd.get_all())
    if len(key_list) == 0:
        print("\nNo keys present!")
        return;

    print("\nEnter the key whose value you want to find:")
    input_key = input()
    value = etcd.get(input_key)[0]
    if value is None:
        print("\nKey does not exist!")
    else:
        print("\nThe value is:", value.decode("utf-8"))


def get_key_and_value_and_put(etcd):
    print("\nEnter the key to be inserted:")
    input_key = input()
    print("Enter the value to be associated with the key:")
    input_value = input()
    try:
        etcd.put(input_key, input_value)
    except:
        print("Something went wrong!")


if __name__ == "__main__":
    etcd = etcd3.client()
    list_all_keys(etcd)
    get_key_and_print_value(etcd)
    get_key_and_value_and_put(etcd)
    list_all_keys(etcd)