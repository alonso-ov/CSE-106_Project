from backend import *

with app.app_context():
    newUser = User(u_userId=2, u_userName='hepworth', u_password='123')
    #db.session.add(newUser)

    newTeacher = Teacher(t_teacherId=1, t_userId=2, t_name='Ammon')
    db.session.add(newTeacher)
    db.session.commit()