from flask import Flask, redirect, url_for, request, abort, render_template, flash, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_manager, LoginManager, login_required, login_user, logout_user, current_user
from flask_cors import CORS

app = Flask(__name__)

# choose where to store database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

app.config['SECRET_KEY'] = 'place secret key here'


# call database
db = SQLAlchemy(app)

# Student table with student name and grade
class User(db.Model, UserMixin):
    u_userId = db.Column(db.Integer, primary_key=True)
    u_userName = db.Column(db.String, unique=True, nullable=False)
    u_password = db.Column(db.String, nullable=False)

    def get_id(self):
        return self.u_userId

    def check_password(self, password):
        return self.u_password == password

class Teacher(db.Model):
    t_teacherId = db.Column(db.Integer, primary_key=True)
    t_userId = db.Column(db.Integer, unique=True, nullable=False)
    t_name = db.Column(db.String, nullable=False)

class Student(db.Model):
    s_studentId = db.Column(db.Integer, primary_key=True)
    s_userId = db.Column(db.Integer, nullable=False)
    s_name = db.Column(db.String, nullable=False)

class Class(db.Model):
    c_classId = db.Column(db.Integer, primary_key=True)
    c_courseName = db.Column(db.String, unique=True, nullable=False)
    c_teacherId = db.Column(db.Integer, nullable=False)
    c_enrollmentNum = db.Column(db.Integer, nullable=False)
    c_capacity = db.Column(db.Integer, nullable=False)
    c_time = db.Column(db.String, nullable=False)

class Enrollment(db.Model):
    e_id = db.Column(db.Integer, primary_key=True)
    e_classId = db.Column(db.Integer, nullable=False)
    e_studentId = db.Column(db.Integer, nullable=False)
    e_grade = db.Column(db.Integer, nullable=True)

# Flask Login management
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Globally declare user
user = None

# Load user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Root directory
@app.route('/')
def index():
    return render_template('login.html')

# Student Dashboard
@app.route('/s_dashboard', methods=['GET', 'POST'])
@login_required
def s_dashboard():
    print('Rendering student dashboard..')

    # get student from student dashboard
    student = Student.query.filter_by(s_userId=current_user.u_userId).first()

    #get all classes available
    allClasses = Class.query.all()

    classesIn = Enrollment.query.filter_by(e_studentId=student.s_studentId)

    return render_template('s_dashboard.html', name=student.s_name, classes=allClasses, classesIn=classesIn)

# Teacher Dashboard
@app.route('/t_dashboard', methods=['GET', 'POST'])
@login_required
def t_dashboard():
    print('Rendering teacher dashboard..')

    # get student from student dashboard
    teacher = Teacher.query.filter_by(t_userId=current_user.u_userId).first()

    return render_template('t_dashboard.html', name=teacher.t_name)

# Login requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    logout_user()

    if request.method == 'POST':

        user = User.query.filter_by(u_userName=request.json['username']).first()

        if user == None:
            print('user not found')
            flash('User does not exist')
        elif not user.check_password(request.json['password']):
            print('Incorrect password')
            flash('Incorrect password')
        else:
            #check if user is student or teacher
            login_user(user)

            #check if user is teacher or student
            teacher = Teacher.query.filter_by(t_userId=user.u_userId).first()
            if teacher == None:
                print('student')
                return {"redirect": url_for('s_dashboard')}
            else:
                print('teacher')
                return {"redirect": url_for('t_dashboard')}

    return {"redirect": url_for('index')}

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return {"redirect": url_for('index')}

# Run app
if __name__ == '__main__':
    app.run(debug=True)