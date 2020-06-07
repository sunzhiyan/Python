# -*- encoding: utf-8 -*-
import datetime
import mysql
from sqlalchemy import Column, create_engine, CHAR, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'Messageboard1'

    # 表的结构:
    ID = Column(CHAR(20), primary_key=True)
    THEME = Column(CHAR(100))
    PERSON = Column(CHAR(20))
    TIME = Column(DateTime)
    is_delete = Column(Integer)


# 创建表
def init_db():
    # 创建表
    engine1 = create_engine(
        'mysql+mysqlconnector://root:root@localhost:3306/testdb',
        max_overflow=2,  # 超过连接池大小外最多创建的数量,
        pool_size=5,  # 连接池的大小
        pool_timeout=30,  # 池中没有线程最多等待的时间
        pool_recycle=-1,  # 多久之后对线程中的线程进行一次连接的回收(重置)

    )
    Base.metadata.create_all(engine1)


# 插入数据
def insert():
    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/testdb')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    id1 = input("输入id：")
    theme = input("输入内容:")
    person = input("输入留言人：")
    is_delete1 = int(input("输入是否删除0/1"))
    new_user = User(ID=id1, THEME=theme, PERSON=person, TIME=datetime.datetime.now(), is_delete=is_delete1)
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


# 删除数据
def delete():
    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/testdb')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    id1 = input("输入要删除id ：")
    user = session.query(User).filter_by(ID=id1).first()
    session.delete(user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


# 修改数据
def update():
    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/testdb')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    id1 = input("输入要修改id ：")
    theme = input("输入修改后的内容：")
    user = session.query(User).filter_by(ID=id1).first()
    user.THEME = theme
    user.TIME = datetime.datetime.now()
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


# 查询数据
def search():
    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/testdb')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    id1 = input("输入要查询id ：")
    user = session.query(User).filter(User.ID == id1).one()
    print('id:', user.ID, 'theme:', user.THEME, 'person:', user.PERSON, 'time:', user.TIME, 'is_delete:', user.is_delete)
    # 关闭session:
    session.close()


def menu():
    print('-----------------------')
    print(' 1.创建表    2.插入')
    print(' 3.删除      4.修改')
    print(' 5.查询      0.退出')
    print('-----------------------')


if __name__ == '__main__':
    menu()
    a = 1
    while a:
        a = int(input("输入要选择的序号:"))
        if a == 1:
            init_db()
        elif a == 2:
            insert()
        elif a == 3:
            delete()
        elif a == 4:
            update()
        elif a == 5:
            search()
        else:
            exit(0)
