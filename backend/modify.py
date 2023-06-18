import json
from sqlalchemy import select
from models.database import Session
from models.educators import Educators
from models.entry import Entry
import pickle as pk

rates = {
    'ассистент': [900.0, 250.0],
    'преподаватель': [900.0, 250.0],
    'директор института': [600.0, 70.0],
    'доцент': [800.0, 150.0],
    'заведующий кафедрой': [650.0, 100.0],
    'профессор': [700.0, 120.0],
    'старший преподаватель': [850, 200]
}


def get_tb_educators():
    session = Session()
    json_obj = []
    for class_instance in session.query(Educators).all():
        vars(class_instance).pop('_sa_instance_state')
        json_obj.append(vars(class_instance))
    return json_obj


def get_tb_entry_with_filters(workload: list = None):
    session = Session()
    # if workload is not None:
    json_obj = []
    for class_instance in session.query(Entry).filter(Entry.workload.in_(workload)):
        vars(class_instance).pop('_sa_instance_state')
        json_obj.append(vars(class_instance))
    return json_obj


def get_tb_educators_with_filters(unit: list = None, post: list = None, rate: list = None):
    # Кафедра = unit, должность = post, ставка = rate
    session = Session()
    sess_query = session.query(Educators)
    if unit is not None:
        sess_query = sess_query.filter(Educators.unit.in_(unit))
    if post is not None:
        sess_query = sess_query.filter(Educators.post.in_(post))
    if rate is not None:
        sess_query = sess_query.filter(Educators.rate.in_(rate))
    json_obj = []
    for class_instance in sess_query:
        vars(class_instance).pop('_sa_instance_state')
        json_obj.append(vars(class_instance))
    return json_obj


def get_tb_educator(id: int):
    session = Session()
    obj = vars(session.query(Educators).get(id))
    obj.pop('_sa_instance_state')
    return obj


def get_tb_entry(id: int):
    session = Session()
    obj = vars(session.query(Entry).get(id))
    obj.pop('_sa_instance_state')
    return obj


def get_tb_entrys():
    session = Session()
    json_obj = []
    for class_instance in session.query(Entry).all():
        vars(class_instance).pop('_sa_instance_state')
        json_obj.append(vars(class_instance))
    return json_obj

# print(get_educators())
