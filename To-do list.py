## plan
## A to-do List so we can use List formatting for the tasks.
tasks = [] #empty list
# 3 possible cases for user... 1. add a task 2. delete/ completed task. 3.View tasks

def add_task(task):
    tasks.append(task)
    print('task added.')

def delete_task(index):
    try:
        del tasks[index]
        print('task deleted')
    except IndexError:
        print('Invalid index')
def view_tasks():
    if tasks:
        print('Your to do list')
        for index, task in enumerate(tasks):
            print(str(index + 1) + ". " + task)


def main():
    while True:
        # Menu options
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Quit")

        # User choice input
        choice = input("Enter your choice: ")

        # Menu options handling
        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            index = int(input("Enter index of task to delete: ")) - 1
            delete_task(index)
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
