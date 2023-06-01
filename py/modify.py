from models.database import Session
from models.educators import Educators


session = Session()
educator = Educators('Кафедра безопасности информационных технологий',
                     'Заведующий кафедрой', 'Абрамов Евгений Сергеевич',
                     'abramov@sfedu.ru',
                     'Работа',
                     'Кандидат наук',
                     'Доцент',
                     1.0)
session.add(educator)
session.commit()
session.close()