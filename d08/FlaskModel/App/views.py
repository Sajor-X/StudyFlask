import random

from flask import Blueprint, render_template

from App.models import Person, db

blue = Blueprint('first_blue', __name__)


@blue.route('/')
def index():
    return 'Hello Flask'


@blue.route('/createdb/')
def create_db():
    """建表"""
    db.create_all()

    return 'DB Create Success'


@blue.route('/addperson/')
def add_person():
    """添加成员"""
    p = Person()

    p.p_name = "小朋友%d号" % random.randrange(100)

    db.session.add(p)

    db.session.commit()

    return 'Person Add Success'


@blue.route('/getpersons/')
def get_persons():
    """查询所有成员"""
    persons = Person.query.all()

    # for person in persons:
    #     print(person.p_name)

    print(type(persons))

    print(persons)

    return render_template('PersonList.html', persons=persons)