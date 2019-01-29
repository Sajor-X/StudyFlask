import random

from flask import Blueprint, render_template

from App.ext import db
from App.models import Student

blue = Blueprint('first_blue', __name__)


def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():
    return 'Hello Flask'


@blue.route('/addstudent/')
def add_student():

    student = Student()

    student.s_name = "小花"

    db.session.add(student)

    db.session.commit()

    return 'Add Success'


@blue.route('/addstudents/')
def add_students():

    # s1 = Student()
    # s1.s_name = "好好听课"
    #
    # s2 = Student()
    # s2.s_name = "好好学习"
    #
    # s3 = Student()
    # s3.s_name = "好好休息"
    #
    # db.session.add(s1)
    # db.session.add(s2)
    # db.session.add(s3)
    #
    # db.session.commit()

    students = []

    for i in range(10):
        student = Student()
        student.s_name = "爱学习的小明%d" % random.randrange(100)
        students.append(student)

    db.session.add_all(students)
    db.session.commit()

    return 'Add Success'




@blue.route('/getstudents/')
def get_students():

    students = Student.query.all()

    for student in students:
        print(student.s_name)

    return render_template('StudentList.html', students=students)


@blue.route('/modifystudent/')
def modify_student():

    # 查
    student = Student.query.first()

    student.s_name = "小明滚出去了"

    db.session.add(student)

    db.session.commit()

    return 'Modify Success'


@blue.route('/deletestudent/')
def delete_student():

    student = Student.query.first()

    db.session.delete(student)

    db.session.commit()

    return 'Delete Success'