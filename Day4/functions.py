def get_todos():
    with open("todos.txt", 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args):
    with open('todos.txt', 'w') as file_local:
        file_local.writelines(todos_args)

##print("Hi Jack")
##print(__name__)

if __name__ == "__main__":
    print("Hello")