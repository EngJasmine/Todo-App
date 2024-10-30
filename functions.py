def get_todos(filepath='todo.txt'):
    """Read a text file and return the list of
    to-do items.
    """

    with open(filepath,'r') as f:
        todos_local=f.readlines()
    return todos_local

def write_todos(todos_arg,filepath='todo.txt'):
    """write the list of to-do items in the text file.
        """
    with open(filepath,'w') as f:
        f.writelines(todos_arg)


if __name__=='__main__':
    get_todos()
