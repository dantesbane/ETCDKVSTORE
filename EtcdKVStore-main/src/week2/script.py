
# run etcd.exe first in terminal 1
# set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python in terminal 2
# run python script.py in terminal 2

import etcd3

def list_all_keys(etcd):
    try:
        key_list = list(etcd.get_all())
        if not key_list:
            print("\nNo keys present!")
        else:
            print("\nList of Keys:")
            for value, metadata in key_list:
                print(metadata.key.decode("utf-8"))
    except Exception as e:
        print(f"An error occurred: {e}")

def get_key_and_print_value(etcd):
    try:
        print("\nEnter the key whose value you want to find:")
        input_key = input()
        value, _ = etcd.get(input_key)
        if value is None:
            print("\nKey does not exist!")
        else:
            print("\nThe value is:", value.decode("utf-8"))
    except Exception as e:
        print(f"An error occurred: {e}")

def get_key_and_value_and_put(etcd):
    try:
        print("\nEnter the key to be inserted:")
        input_key = input()
        print("\nEnter the value to be associated with the key:")
        input_value = input()
        etcd.put(input_key, input_value)
        print("\nKey-value pair added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_key(etcd):
    try:
        print("\nEnter the key to be deleted:")
        input_key = input()
        deleted = etcd.delete(input_key)
        if deleted:
            print("\nKey deleted successfully!")
        else:
            print("\nKey not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

def range_scan_keys(etcd):
    try:
        print("\nEnter the start key for the range scan:")
        start_key = input()
        print("\nEnter the end key for the range scan:")
        end_key = input()
        
        print("\nFetching keys and values within the range...")
        key_list = list(etcd.get_range(start_key, end_key))
        if not key_list:
            print("\nNo keys present in the specified range!")
        else:
            print("\nList of Keys and Values within the range:")
            for value, metadata in key_list:
                print(f"Key: {metadata.key.decode('utf-8')}, Value: {value.decode('utf-8')}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main_menu(etcd):
    while True:
        print("\nPlease choose an option:")
        print("1: List all keys")
        print("2: Get the value of a key")
        print("3: Put a key-value pair")
        print("4: Delete a key")
        print("5: Range scan for keys")
        print("6: Exit")
        choice = input("> ")

        if choice == '1':
            list_all_keys(etcd)
        elif choice == '2':
            get_key_and_print_value(etcd)
        elif choice == '3':
            get_key_and_value_and_put(etcd)
        elif choice == '4':
            delete_key(etcd)
        elif choice == '5':
            range_scan_keys(etcd)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    try:
        etcd_client = etcd3.client()  # You can add host and port if needed
    except Exception as e:
        print(f"An error occurred: {e}")

    main_menu(etcd_client)
