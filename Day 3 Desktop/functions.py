def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_args):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_args)

##print("Hi Jack")
##print(__name__)

if __name__ == "__main__":
    print("Hello")