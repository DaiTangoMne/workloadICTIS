from models.database import Session
from models.educators import Educators


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
