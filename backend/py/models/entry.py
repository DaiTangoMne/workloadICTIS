from sqlalchemy import Column, Integer, String, REAL, ARRAY
from models.database import Base


class Entry(Base):
    __tablename__ = 'entry'

    ID = Column(Integer, primary_key=True)
    unit = Column(String)
    department = Column(String)
    ID1Cdep = Column(Integer)
    discipline = Column(String)
    disciplineID = Column(Integer)
    workload = Column(String)
    group = Column(String)
    block = Column(ARRAY(String))
    semestr = Column(ARRAY(String))
    _period = Column(Integer)
    plan = Column(ARRAY(String))
    planUnit = Column(ARRAY(String))
    ID1Cunit = Column(Integer)
    studyForm = Column(String)
    levelStudy = Column(ARRAY(String))
    directionStudy = Column(ARRAY(String))
    profile = Column(ARRAY(String))
    _program = Column(ARRAY(String))
    studentsCount = Column(Integer)
    hours = Column(REAL)
    hoursBudget = Column(REAL)
    hoursNonBudget = Column(REAL)
    hoursAuditory = Column(REAL)
    hoursRatingControl = Column(REAL)
    ZETcount = Column(REAL)

    def __init__(self, unit: str, department: str, ID1Cdep: int, discipline: str, disciplineID: int, #6
                 workload: str, group: str, block: list, semestr: list, _period: int, plan: list, #12
                 planUnit: list, ID1Cunit: list, studyForm: str, levelStudy: list, directionStudy: list,
                 profile: list, _program: list, studentsCount: int, hours: float, hoursBudget: float,
                 hoursNonBudget: float, hoursAuditory: float, hoursRatingControl: float, ZETcount: float):
        self.unit = unit
        self.department = department
        self.ID1Cdep = ID1Cdep
        self.discipline = discipline
        self.disciplineID = disciplineID
        self.workload = workload
        self.group = group
        self.block = block
        self.semestr = semestr
        self._period = _period
        self.plan = plan
        self.planUnit = planUnit
        self.ID1Cunit = ID1Cunit
        self.studyForm = studyForm
        self.levelStudy = levelStudy
        self.directionStudy = directionStudy
        self.profile = profile
        self._program = _program
        self.studentsCount = studentsCount
        self.hours = hours
        self.hoursBudget = hoursBudget
        self.hoursNonBudget = hoursNonBudget
        self.hoursAuditory = hoursAuditory
        self.hoursRatingControl = hoursRatingControl
        self.ZETcount = ZETcount

    def __repr__(self):
        info: str = f'ID: {self.ID}\n' \
                    f'Дисциплина: {self.discipline}({self.disciplineID})\n' \
                    f'Часы: {self.hours}'
        return info