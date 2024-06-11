def Todo():
    tasks=[]

    while True:
        print(f"TODO List")
        print(f"1.TO ADD task.")
        print(f"2. Show task.")
        print(f"3. Mark task as Done.")
        print(f"4.Exit.")

        choice=int(input(f"Enter Your Choice: "))

        if (choice==1):
            addTask=int(input(f"How many task you want to ADD."))
            for i in range(addTask):
                task=input("Enter your task.")
                tasks.append({"task":task, "done": False})
                print(f"Task Added!")

        elif(choice==2):
            print(f"\n Tasks")
            for index,task in enumerate(tasks):
                status="Done" if task["done"] else "Not Done"
                print(f"{index+1}.{task['task']}-{status}")

        elif(choice==3):
            task_index=int(input(f"Enter the task number to mark as done: "))-1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif(choice==4):
            print(f"Exiting to the Todo List")
            break
        else:
            print(f"Please try Again.")

Todo()



            


