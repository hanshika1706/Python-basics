#todo_cli.py
tasks = []

while True:
    cmd = input("add/view/exit: ")

    if cmd == "add":
        tasks.append(input("Task: "))
    elif cmd == "view":
        for i, t in enumerate(tasks):
            print(i+1, t)
    else:
        break
