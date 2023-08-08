def get_todos(filePath="todos.txt"):
    """ Reads a text file and
    returns list of to-do items."""
    with open(filePath, 'r') as file_todo:
        todo_items = file_todo.readlines()
    return todo_items

def write_todos(content, filePath="todos.txt"):
    """ Write to-do items in a text file """
    with open(filePath, 'w') as file:
        file.writelines(content)

print("Hello, I will be executed from any module which imports function or if I am called directly")

print(__name__)
if __name__ == "__main__":
    print("Hello, I will only be executed when someone calls this script directly")