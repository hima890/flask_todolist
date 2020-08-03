# import all the packigs
from flask import Blueprint, redirect, render_template, url_for, request, flash, redirect
from projectFiles.models import Task, Complated
from projectFiles import db
from projectFiles.main.function import check, delete

# the main bluebrint
home_page = Blueprint('home', __name__,
    template_folder='templates',
    static_folder='static')

# I am not going to explain this nonsense. You should be familiar with the flask framework
@home_page.route("/", methods=["POST", "GET"])
@home_page.route("/todolist", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        delete()
        newTask = request.form.get("task")
        if newTask == "":
            combltedTask = Complated.query.order_by(Complated.datePost.desc()).all()
            allTasks = Task.query.order_by(Task.datePost.desc()).all()
            flash("please inter a task", "danger")
            return render_template("index.html", title="TODOlist", allTasks=allTasks, combltedTask=combltedTask)
        else:
            functionResult = check(newTask)
            if functionResult:
                new = Task(content=newTask)
                db.session.add(new)
                db.session.commit()
                combltedTask = Complated.query.order_by(Complated.datePost.desc()).all()
                allTasks = Task.query.order_by(Task.datePost.desc()).all()
                return render_template("index.html", title="TODOlist", allTasks=allTasks, combltedTask=combltedTask)
            else:
                flash("seem task already threre", "warning")
                combltedTask = Complated.query.order_by(Complated.datePost.desc()).all()
                allTasks = Task.query.order_by(Task.datePost.desc()).all()
                return render_template("index.html", title="TODOlist", allTasks=allTasks, combltedTask=combltedTask)
    combltedTask = Complated.query.order_by(Complated.datePost.desc()).all()
    delete()
    allTasks = Task.query.order_by(Task.datePost.desc()).all()
    return render_template("index.html", title="TODOlist", allTasks=allTasks, combltedTask=combltedTask)


@home_page.route("/delete/<int:id>", methods=["GET"])
def deleteFunction(id):
    task = Task.query.filter_by(id=id).first()
    if task:
        newComplted = Complated(datePost=task.datePost, content=task.content)
        deleteTask = Task.query.filter_by(id=id).delete()
        db.session.add(newComplted)
        db.session.commit()

    allTasks = Task.query.order_by(Task.datePost.desc()).all()
    combltedTask = Complated.query.order_by(Complated.datePost.desc()).all()
    return render_template("index.html", title="TODOlist", allTasks=allTasks, combltedTask=combltedTask)


    

