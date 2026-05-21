from flask import Flask, request, render_template_string
import pickle

app = Flask(__name__)

# load saved model
model = pickle.load(
    open("placement_model.pkl","rb")
)

html = """

<html>

<head>

<style>

body{
    background:linear-gradient(to right,#1e3c72,#2a5298);
    font-family:Arial;
}

.box{
    width:400px;
    background:white;
    padding:30px;
    margin:50px auto;
    border-radius:15px;
    text-align:center;
}

input{
    width:90%;
    padding:10px;
    margin:8px;
}

button{
    width:95%;
    padding:10px;
    background:#1e3c72;
    color:white;
    border:none;
    border-radius:5px;
}

h2{
color:#1e3c72;
}

</style>

</head>

<body>

<div class="box">

<h2>Placement Prediction System</h2>

<form method="POST">
Age:<br>
<input name="age"><br>
Gender:<br>
<select name="gender">
<option>Male</option>
<option>Female</option>
</select><br><br>

Degree:<br>
<select name="degree">
<option>B.Tech</option>
<option>BCA</option>
<option>MCA</option>
<option>B.Sc</option>
</select><br><br>

Branch:<br>
<select name="branch">
<option>IT</option>
<option>ECE</option>
<option>ME</option>
<option>Civil</option>
</select><br><br>

CGPA:<br>
<input name="cgpa"><br>

Internships:<br>
<input name="internships"><br>

Projects:<br>
<input name="projects"><br>

Coding Skills:<br>
<input name="coding"><br>

Communication Skills:<br>
<input name="communication"><br>

Backlogs:<br>
<input name="backlogs"><br>

Aptitude Score:<br>
<input type="number" name="aptitude"><br>

Soft Skills:<br>
<input type="number" name="soft"><br>

Certifications:<br>
<input type="number" name="cert"><br><br>

<button type="submit">
Predict
</button>

</form>

<h2>{{result}}</h2>

</div>

</body>
</html>

"""
@app.route("/",methods=["GET","POST"])
def home():

    result=""

    if request.method=="POST":
        age=int(request.form["age"])
        gender=request.form["gender"]
        degree=request.form["degree"]
        branch=request.form["branch"]

        cgpa=float(request.form["cgpa"])
        internships=int(
            request.form["internships"]
        )

        projects=int(
            request.form["projects"]
        )

        coding=int(
            request.form["coding"]
        )

        communication=int(
            request.form["communication"]
        )

        backlogs=int(
            request.form["backlogs"]
        )
        aptitude=int(request.form["aptitude"])

        soft=int(request.form["soft"])

        cert=int(request.form["cert"])

        student=[[
        age,
        cgpa,
        internships,
        projects,
        coding,
        communication,
        aptitude,
        soft,
        cert,
        backlogs,

        1 if gender=="Male" else 0,
        1 if degree=="B.Tech" else 0,
        1 if degree=="BCA" else 0,
        1 if degree=="MCA" else 0,
        1 if branch=="Civil" else 0,
        1 if branch=="ECE" else 0,
        1 if branch=="IT" else 0,
        1 if branch=="ME" else 0

        ]]

        prediction=model.predict(student)

        if prediction[0]==1:
            result="Placed"

        else:
            result="Not Placed"

    return render_template_string(
        html,
        result=result
    )

app.run(debug=True)
