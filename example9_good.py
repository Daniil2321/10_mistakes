from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Создание базы данных
engine = create_engine('sqlite:///example.db')

# Создание базового класса для моделей
Base = declarative_base()

# Определение модели User
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Создание таблицы
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Выполнение запроса
    query = session.query(User).filter(User.age > 20)
    result = query.all()

    # Получение данных
    for user in result:
        print(user.name, user.age)
finally:
    # Закрытие сессии
    session.close()