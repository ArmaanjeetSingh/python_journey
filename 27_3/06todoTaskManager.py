class Task:
    def __init__(self,title):
        self.task = {
            "title":title,
            "completed":False
        }


class TodoList:
    def __init__(self):
        self.tasks_list = []

    def add_task(self,title):
        self.tasks_list.append(Task(title))
        print("Task {} is added to ToDo list".format(title))

    
    def show_tasks(self):
        if not self.tasks_list:
            print("No tasks available")
            return
        for i,task in enumerate(self.tasks_list,start=1):
            status = "completed" if task.task['completed'] == True else "pending"
            print(f"{i} Task : {task.title} status : {status}")

        
    def complete_task(self,index):
        if 0 <= index < len(self.tasks_list):
           task = self.tasks_list[index]
           print(task.task['title'],'is completed')
           self.tasks_list[index].task['completed']  = True
        else:
            print("Invalid Index")

    def delete_task(self,index):
        if 0<= self.tasks_list[index] < len(self.tasks_list):
            value = self.tasks_list.pop(index)
            print(value.task['title'],'is delted')
        else:
            print("Invalid Index")

    def show_pending_task(self):
        pending =  [item.task['title'] for item in self.tasks_list if item.task['completed'] == False]
        for task in pending:
            print(task)




if __name__ == '__main__':
    todo = TodoList()

    todo.add_task("Study Python")
    todo.add_task("Go Gym")

    # todo.show_tasks()

    todo.complete_task(1)
    todo.delete_task(1)
    todo.show_pending_task()