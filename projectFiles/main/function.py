from projectFiles.models import Task
from projectFiles import db
from projectFiles.models import Complated
from datetime import datetime

timeNow = datetime.now().day

def check(newTask):
    result = Task.query.filter_by(content=newTask).first()
    if result:
        return False
    else:
        return True


def delete():
    tasks = Complated.query.all()
    print(tasks)
    for task in tasks:
        taskTime = task.datePost.day
        if taskTime - timeNow >= 3:
           deleteTask = Complated.query.filter_by(id=task.id).delete()
