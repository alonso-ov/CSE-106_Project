from backend import *

with app.app_context():

    #create students
    newUser1 = User(u_userId=1, u_userName='alonso', u_password='123')
    newUser2 = User(u_userId=2, u_userName='alexis', u_password='123')
    newUser3 = User(u_userId=3, u_userName='bryan', u_password='123')
    newUser4 = User(u_userId=4, u_userName='david', u_password='123')
    db.session.add(newUser1)
    db.session.add(newUser2)
    db.session.add(newUser3)
    db.session.add(newUser4)

    newStudent1 = Student(s_studentId=10, s_userId=1 ,s_name='Alonso Ortiz')
    newStudent2 = Student(s_studentId=20, s_userId=2 ,s_name='Alexis Herrera')
    newStudent3 = Student(s_studentId=30, s_userId=3 ,s_name='Bryan Jimenez')
    newStudent4 = Student(s_studentId=40, s_userId=4 ,s_name='David Guiterrez')
    db.session.add(newStudent1)
    db.session.add(newStudent2)
    db.session.add(newStudent3)
    db.session.add(newStudent4)

    #create teachers
    newUser5 = User(u_userId=5, u_userName='ammon', u_password='123')
    newUser6 = User(u_userId=6, u_userName='florin', u_password='123')
    db.session.add(newUser5)
    db.session.add(newUser6)

    newTeacher1 = Teacher(t_teacherId=10, t_userId=5, t_name='Hepworth')
    newTeacher2 = Teacher(t_teacherId=20, t_userId=6, t_name='Rusu')
    db.session.add(newTeacher1)
    db.session.add(newTeacher2)

    #create classes
    newClass = Class(c_classId=1, c_courseName='CSE-106', c_teacherId=10, c_enrollmentNum=0, c_capacity=1, c_time='TR 5:00-7:00 PM')
    db.session.add(newClass)
    newClass = Class(c_classId=2, c_courseName='CSE-165', c_teacherId=10, c_enrollmentNum=0, c_capacity=2, c_time='F 8:00-9:15 AM')
    db.session.add(newClass)
    newClass = Class(c_classId=3, c_courseName='CSE-111', c_teacherId=20, c_enrollmentNum=0, c_capacity=3, c_time='T 10:30-11:45 AM')
    db.session.add(newClass)
    newClass = Class(c_classId=4, c_courseName='CSE-177', c_teacherId=20, c_enrollmentNum=0, c_capacity=4, c_time='M 1:00-2:00 PM')
    db.session.add(newClass)

    db.session.commit()
