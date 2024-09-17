users=[]
database=[]
class Registration:
    def registrate():
        user = {
            "username": input("Enter username: "),
            "password": input("password: ")
        }
        users.append(user)
        print("You registered, now log in")
    def login():
        username = input("Enter username: ")
        password = input("password: ")
        user = {"username": username, "password": password}
        if user in users:
            cnt = 0
            while True:
                user_input = input("->")
                if user_input == "1":
                    cnt += 1
                    task = {
                        "id": cnt,
                        "name": input("task: "),
                        "due_date": input("due_date: "),
                        "time": input("time: "),
                        "is_completed": False,
                        "username": username
                    }
                    database.append(task)
                elif user_input == '2':
                    user_tasks = [task for task in database if task["username"] == username]
                    print(user_tasks)
                elif user_input == '3':
                    id = int(input("id = "))
                    for task in database:
                        if id == task["id"] and task["username"] == username:
                            task["name"] = input("new_task: ")
                elif user_input == '4':
                    id = int(input("id = "))
                    for task in database:
                        if id == task["id"] and task["username"] == username:
                            for key, value in task.items():
                                print(f"{key}: {value}")
                elif user_input == '5':
                    id = int(input("id = "))
                    for task in database:
                        if id == task["id"] and task["username"] == username:
                            database.remove(task)
                            break
                elif user_input == '6':
                    break
        else:
            print("User not found. Please register first.")
    def delete():
        username = input("Enter username to delete: ")
        password = input("password: ")
        user = {"username": username, "password": password}
        if user in users:
            users.remove(user)
            print("User deleted.")
        else:
            print("User not found.")
while True:
    q=input("reg or log or del or stop: ")
    if q=="reg":
        obj=Registration
        obj.registrate()
    elif q=="log":
        obj=Registration
        obj.login()
    elif q=="del":
        obj=Registration
        obj.delete()
    elif q=="stop":
        break
    else:
        print("Enter correctly")
