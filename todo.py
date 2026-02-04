def to_do_list():
    taskes = []

    while True:
        print("1. add task")
        print("2. view tasks")
        print("3. remove task")
        print("4. exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task: ")
            taskes.append(task)
            print("Task added.")
        elif choice == '2':
            if not taskes:
                print("No tasks in the list.")
            else:
                print("Tasks:")
                for idx, task in enumerate(taskes, start=1):
                    print(f"{idx}. {task}")
        elif choice == '3':
            if not taskes:
                print("No tasks to remove.")
            else:
                print("Tasks:")
                for idx, task in enumerate(taskes, start=1):
                    print(f"{idx}. {task}")
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(taskes):
                    removed_task = taskes.pop(task_num - 1)
                    print(f"Removed task: {removed_task}")
                else:
                    print("Invalid task number.")
        elif choice == '4':
            print("Exiting the to-do list application.")
            with open('report.txt', 'w') as report_file:
                report_file.write("# To-Do List Report\n\n")
                report_file.write("This file contains the results of the To-Do List.\n\n")
                report_file.write("## Completed Tasks\n\n")
                for task in taskes:
                    report_file.write(f"- {task}\n")
                report_file.write("\n## Pending Tasks\n\n")
                # Add logic for pending tasks if needed
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    to_do_list()