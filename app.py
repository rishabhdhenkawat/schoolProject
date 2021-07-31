from flask import Flask, render_template, request, url_for, redirect, session
from flask import Flask, request, url_for,Response, render_template_string
import pandas as pd
app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')


@app.route("/", methods=['post', 'get'])
def index():
    return render_template('part1.html')
@app.route("/part1", methods=['post', 'get'])
def part1():
    return render_template('part1.html')

@app.route("/page2", methods=['post', 'get'])
def page2():
    return render_template('page2.html')

@app.route("/page7", methods=['post', 'get'])
def page7():
    return render_template('page7.html')


@app.route("/student", methods=['post', 'get'])
def student():
    return render_template('student.html')

@app.route("/facultyLogin", methods=['post', 'get'])
def facultyLogin():
    return render_template('facultyLogin.html')


@app.route("/logout", methods=['post', 'get'])
def logout():
    return render_template('logout.html')

@app.route("/page3", methods=['post', 'get'])
def page3():
    data=pd.read_csv("complaint.csv")
    myData = list(data.values)
    return render_template('page3.html',myData=myData)

@app.route("/page4", methods=['post', 'get'])
def page4():
    data=pd.read_csv("complaintRecord.csv")
    myData = list(data.values)
    return render_template('page4.html',myData=myData)


@app.route("/page5", methods=['post', 'get'])
def page5():
    data=pd.read_csv("studentVolunteer.csv")
    headings=[]
    for col in data.columns:
        headings.append(col)
    myData = list(data.values)
    return render_template('page5.html',myData=myData,headings=headings)

@app.route("/page5Submit", methods=['post', 'get'])
def page5Submit():
    if request.method == "POST":
        name=request.form.get("name")
        id_=request.form.get("id")
        email=request.form.get("email")
        department=request.form.get("dept")
        phone=request.form.get("Phone")
        data=pd.read_csv("studentVolunteer.csv")
        print(data.loc[0])
        l=[id_, name,department,email,phone," "," "] 
        print(l)
        print(data)
        data.loc[len(data.index)] = l
        data.to_csv("studentVolunteer.csv",index=False)
        data=pd.read_csv("studentVolunteer.csv")
        headings=[]
        for col in data.columns:
            headings.append(col)
        myData = list(data.values)
        return render_template('page5.html',myData=myData,headings=headings)


@app.route("/faculty", methods=['post', 'get'])
def faculty():
    data=pd.read_csv("faculty.csv")
    headings=[]
    for col in data.columns:
        headings.append(col)
    myData = list(data.values)
    return render_template('faculty.html',myData=myData,headings=headings)


@app.route("/facultySubmit", methods=['post', 'get'])
def facultySubmit():
    if request.method == "POST":
        name=request.form.get("name")
        id_=request.form.get("id")
        email=request.form.get("email")
        department=request.form.get("dept")
        phone=request.form.get("Phone")
        data=pd.read_csv("faculty.csv")
        print(data.loc[0])
        l=[id_, name,department,email,phone," "," "] 
        print(l)
        print(data)
        data.loc[len(data.index)] = l
        data.to_csv("faculty.csv",index=False)
        data=pd.read_csv("faculty.csv")
        headings=[]
        for col in data.columns:
            headings.append(col)
        myData = list(data.values)
        return render_template('faculty.html',myData=myData,headings=headings)
@app.route("/report", methods=['post', 'get'])
def report():
    data=pd.read_csv("report.csv")
    headings=[]
    for col in data.columns:
        headings.append(col)
    myData = list(data.values)
    return render_template('report.html',myData=myData,headings=headings)


@app.route("/reportSubmit", methods=['post', 'get'])
def reportSubmit():
    if request.method == "POST":
        name=request.form.get("name")
        id_=request.form.get("id")
        email=request.form.get("email")
        department=request.form.get("dept")
        phone=request.form.get("Phone")
        data=pd.read_csv("faculty.csv")
        print(data.loc[0])
        l=[id_, name,department,email,phone," "," "] 
        print(l)
        print(data)
        data.loc[len(data.index)] = l
        data.to_csv("report.csv",index=False)
        data=pd.read_csv("report.csv")
        headings=[]
        for col in data.columns:
            headings.append(col)
        myData = list(data.values)
        return render_template('report.html',myData=myData,headings=headings)





@app.route("/complaintLogin", methods=['post', 'get'])
def complaintLogin():
    if request.method == "POST":
        username=request.form.get("name")
        password=request.form.get("password")
        data=pd.read_csv("studentVolunteer.csv")
        return render_template('complaintPage.html')




if __name__ == "__main__":
    app.run(host='0.0.0.0', port="8888",debug=True, threaded=True)
