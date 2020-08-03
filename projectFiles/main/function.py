# import all the packigs
from projectFiles.models import Task
from projectFiles import db
from projectFiles.models import Complated
from datetime import datetime

timeNow = datetime.now().day

# this function chick if the task allredy in the databas 
def check(newTask):
    result = Task.query.filter_by(content=newTask).first()
    if result:
        return False
    else:
        return True

#this function delete the task after three days
def delete():
    tasks = Complated.query.all()
    for task in tasks:
        taskTime = task.datePost.day
        if taskTime - timeNow >= 3:
           deleteTask = Complated.query.filter_by(id=task.id).delete()
