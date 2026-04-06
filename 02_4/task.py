class Task:
    def __init__(self,name,due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self,new_name):
        if self.name != new_name:
            self.name = new_name
            return self.name
        return "Name can't be same."

    def change_due_date(self,new_date):
        if self.due_date != new_date:
           self.due_date = new_date
           return self.due_date
        return "Date can't be same"

    def add_comment(self,comment):
        self.comments.append(comment)

    def edit_comment(self,comment_number,new_number):
        if 0 <= comment_number <= len(self.comments):
            self.comments[comment_number] = new_number
            return ','.join(self.comments)
        return "Can't find comment"

    def details(self):
        return f"Name: {self.name} - Due date: {self.due_date}"

