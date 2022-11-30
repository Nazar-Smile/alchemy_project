from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from sqlalchemy.ext.declarative import declarative_base
from models import StudentGroup, Student, Base
import os

engine = create_engine("mysql+pymysql://root:djh895kjh924y@localhost/alchemy_project")

Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = Session()

def clear_terminal():
    # os.system("clear")
    os.system("cls||clear") # Windows


while True:
    print("Выберите действие: ")
    print("""
        1. Добавить группу
        2. Получить все группы
    """)
    action_number = int(input("Введите номер действия:"))
    clear_terminal()
    if action_number == 1:
        name = input("Введите название группы:")
        start = input("Введите время начала обучения группы:")
        end = input("Введите время завершения обучения:")
        group = StudentGroup(
            name = name,
            start = start,
            end = end    
        )

        session.add(group)
        session.commit()
        clear_terminal()
        print("Группа успешно создана")
    elif action_number == 2:
        groups = session.query(StudentGroup).all()
        print("Все группы: ")
        for n, g in enumerate(groups, start=1):
            print(f"{n}) {g.name} = {g.start} = {g.end}")


    message = "Желаете ли вы завершить работу программы, введите Y,y, если нет, нажмите Enter"
    text = input(message)
    if text.lower() == "y":
        break













































# connect = engine.connect()
# result = connect.execute("SELECT * FROM student_group;")
# print(result.fetchall())