from task import Task

class Section:
    def __init__(self,name):
        self.name = name
        self.tasks = []

    def add_task(self,new_task:Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to section"
        return f'Task is already in section {self.name}'


    def complete_task(self,task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f'Completed task {task_name}'
        return f"Could not find task with the name {task_name}"

    
    def view_section(self):
        data='/n'.join([task.details() for task in self.tasks])
        return f"Section {self.name} :\n{data}"

if __name__ == '__main__':
    task = Task("Make bed", "27/05/2020")
    print(task.change_name("Go to University"))
    print(task.change_due_date("28.05.2020"))

    task.add_comment("Don't forget laptop")
    print(task.edit_comment(0, "Don't forget laptop and notebook"))
    print(task.details())

    section = Section("Daily tasks")
    print(section.add_task(task))
    print(section.view_section())


