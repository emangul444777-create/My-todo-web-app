FILEPATH = "todo_list.txt"

def get_todolist(filepath=FILEPATH):
    """ Read the text file and return a todo list."""
    with open(filepath, "r") as file_local:
        todolist = file_local.readlines()
        return todolist

def write_todolist(todolist, filepath=FILEPATH):
    """ Write the todo in the text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todolist)

# if __name__== "functions":
    # print("indirect")

if __name__ == "__main__":
    print(get_todolist())
    print("direct")