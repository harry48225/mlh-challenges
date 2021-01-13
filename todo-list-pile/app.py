# displays your todos in a pile for example

#       pet the cat
#      feed the cat
#    install a catflap
# take the cat for a walk

art = [ "_            _                 _ _      ",
        "| |_ ___   __| | ___      _ __ (_) | ___ ",
        "| __/ _ \ / _` |/ _ \    | '_ \| | |/ _ \\",
        "| || (_) | (_| | (_) |   | |_) | | |  __/",
        " \__\___/ \__,_|\___/____| .__/|_|_|\___|",
        "                   |_____|_|    "]


class todo_list(object):

    def __init__(self):

        self.todos = self.__load_todos()
        self.sort_list()

    def __load_todos(self):

        with open("todos.txt") as f:

            todo_list = [line.strip() for line in f.readlines()]

            f.close()

        return todo_list


    def add_to_list(self, item):

        self.todos.append(item)

        self.sort_list()

        self.__save_list()


    def sort_list(self):
        self.todos = sorted(self.todos, key = lambda x : len(x)) # Sort the todolist in order of increasing length


    def print_todos(self):

        longest_length = len(self.todos[-1])

        for i, todo in enumerate(self.todos):

            padding = " " * ((longest_length - len(todo)) // 2)

            print("[{}]: ".format(i) + padding + todo)

    def get_number_of_todos(self):
        
        return len(self.todos)

    def remove_todo_at_index(self, index):

        del self.todos[index]

        self.__save_list()
       
    def __save_list(self):

        with open("todos.txt", 'w') as f:
            f.writelines([todo + "\n" for todo in self.todos])
            f.close()

        print("saved")


# Program loop

todos = todo_list()

while True:

    for line in art:
        print(line)
    print("________________________________________")
    print()
    todos.print_todos()
    
    response = input("Enter the number of a todo to remove it, else enter a new todo, or type exit: ")

    if response in [str(i) for i in range(todos.get_number_of_todos())]:

        todos.remove_todo_at_index(int(response))

    elif response == "exit":
        break

    else:

        todos.add_to_list(response)



