from models.database import Session
from models.educators import Educators
from models.entry import Entry


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
            educator = Educators(row[1], row[2], row[3], row[4], row[5], row[6], row[7], float(row[8]))
            session.add(educator)
        except Exception as ex:
            print(ex, row[1], row[2], row[3], row[4], row[5], row[6], row[7], float(row[8]))
        session.commit()
    session.close()


def get_entry(row):
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
                entry = get_entry(row)
                session.add(entry)
                session.commit()
        except Exception as ex:
            print(ex)
            input()
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
