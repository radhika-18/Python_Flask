from flask import Flask, render_template, request
from DbConnection import setdbconnection
from StudentData import Student
from StudentDao import StudentDao

studentapp = Flask(__name__)


@studentapp.route('/')
def mainpage():
    return render_template("home.html")


@studentapp.route('/enternew')
def addstudentform():
    return render_template("student.html")


@studentapp.route('/addrec', methods=['POST', 'GET'])
def addrecords():
    if request.method == 'POST':
        student = Student(request.form)
        studentdao = StudentDao(setdbconnection())
        return render_template("result.html", msg=studentdao.addrecord(student))


@studentapp.route('/list')
def listrecords():
    studentdao=StudentDao(setdbconnection())
    return render_template("list.html",rows=studentdao.showrecords())

if __name__ == "__main__":
    studentapp.run(debug=True)
