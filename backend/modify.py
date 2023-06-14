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
    if workload is not None:
        json_obj = []
        for class_instance in session.query(Entry).filter(Entry.workload.in_(workload)):
            vars(class_instance).pop('_sa_instance_state')
            json_obj.append(vars(class_instance))
        return json_obj


get_tb_entry_with_filters(['Практические', "Лекционные"])


def get_tb_educator(id: int):
    session = Session()
    obj = vars(session.query(Educators).get(id))
    obj.pop('_sa_instance_state')
    return obj


def get_educators_XL(row):
    rank = row[7]
    if rank is not None:
        try:
            mx, mn = rates[rank.lower()]
        except:
            mx = None
            mn = None
    else:
        mx = None
        mn = None
    return Educators(row[1], row[2], row[3], row[4], row[5], row[6], row[7], float(row[8]), mx, mn)


def insert_educators(df):
    """
    Парсит строки Dataframe с преподавателями
    и инсертит в БД
    :param df: Dataframe
    """
    session = Session()
    for row in df.itertuples():
        # _, unit, post, name, email, state, degree, rank, rate = row
        try:
            educator = get_educators_XL(row)
            session.add(educator)
        except Exception as ex:
            print(ex)
        session.commit()
    session.close()


def get_entry_XL(row):
    """
    Заполняет объект класса Entry данными из Dataframe Row
    :param row: строка Dataframe
    :return: заполненный объект класса Entry
    """
    unit = row[2]  # str
    department = row[3]  # str
    ID1Cdep = int(row[4])
    discipline = row[5]
    disciplineID = int(row[6])
    workload = row[7]
    group = row[8]
    block = row[9].split(',')
    semestr = row[10].split(',')
    _period = int(row[11])
    plan = [i.strip() for i in row[12].split(',')]
    planUnit = row[13].split(',')
    ID1Cunit = [int(i) for i in row[14].split(',')]
    studyForm = row[15]
    levelStudy = row[16].split(',')
    directionStudy = row[17].split(',')
    if row[18] is not None:
        profile = row[18].split(',')
    else:
        profile = None
    if row[19] is not None:
        _program = row[19].split(',')
    else:
        _program = None
    if row[20] is not None:
        studentsCount = int(float(row[20].replace(',', '.')))
    else:
        studentsCount = None
    hours = float(row[21].replace(',', '.'))
    hoursBudget = float(row[22].replace(',', '.'))
    try:
        hoursNonBudget = float(row[23].replace(',', '.'))
    except:
        hoursNonBudget = None
    hoursAuditory = float(row[24].replace(',', '.'))
    try:
        hoursRatingControl = float(row[25].replace(',', '.'))
    except:
        hoursRatingControl = None
    try:
        ZETcount = float(row[26].replace(',', '.'))
    except:
        ZETcount = None
    return Entry(unit, department, ID1Cdep, discipline, disciplineID, workload, group, block, semestr, _period, plan,
                 planUnit, ID1Cunit, studyForm, levelStudy, directionStudy, profile, _program, studentsCount, hours,
                 hoursBudget, hoursNonBudget, hoursAuditory, hoursRatingControl, ZETcount)


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


def insert_entry(df):
    """
    Инсертит Dataframe входного файла в БД
    :param df: Dataframe входного файла
    """
    session = Session()
    for row in df.itertuples():
        try:
            if str(row[1]) == 'Итого':
                print('Итого')
            else:
                entry = get_entry_XL(row)
                session.add(entry)
                session.commit()
        except Exception as ex:
            print(ex)
    session.close()


def test_insert():
    session = Session()
    educator = Educators('Кафедра безопасности информационных технологий',
                         'Старший преподаватель', 'Алексеев Дмитрий Михайлович',
                         'dalekseev@sfedu.ru',
                         'Работа',
                         None,
                         None,
                         0.5)
    session.add(educator)
    session.commit()
    session.close()

# print(get_educators())
