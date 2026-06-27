from flask import Flask, request, render_template_string
import base64

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>BMI Calculator</title>

<style>
body{
    font-family:Arial;
    background:#f2f2f2;
}

.container{
    width:350px;
    margin:50px auto;
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0 0 10px gray;
}

input{
    width:95%;
    padding:8px;
    margin-top:5px;
}

button{
    margin-top:15px;
    padding:10px;
    width:100%;
    font-size:16px;
}

.error{
    color:red;
    font-size:14px;
    margin-bottom:10px;
}

.result{
    margin-top:20px;
    font-size:18px;
    color:blue;
}
</style>

<script>

function validateWeight(){

    let weight=document.getElementById("weight").value;
    let error=document.getElementById("weightError");

    if(weight=="" || weight<=0){
        error.innerHTML="Please enter a valid weight.";
        return false;
    }

    error.innerHTML="";
    return true;
}

function validateHeight(){

    let height=document.getElementById("height").value;
    let error=document.getElementById("heightError");

    if(height=="" || height<=0){
        error.innerHTML="Please enter a valid height.";
        return false;
    }

    error.innerHTML="";
    return true;
}

function validateForm(){

    let w=validateWeight();
    let h=validateHeight();

    return w && h;
}

</script>

</head>

<body>

<div class="container">

<h2>BMI Calculator</h2>

<form method="POST" onsubmit="return validateForm()">

<label>Weight (kg)</label><br>
<input type="number" step="0.1" id="weight" name="weight"
oninput="validateWeight()">
<div id="weightError" class="error"></div>

<label>Height (m)</label><br>
<input type="number" step="0.01" id="height" name="height"
oninput="validateHeight()">
<div id="heightError" class="error"></div>

<button type="submit">Calculate BMI</button>

</form>

{% if bmi %}

<div class="result">
BMI : {{bmi}}<br><br>
Category : <b>{{category}}</b>
</div>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():

    bmi=None
    category=""

    if request.method=="POST":

        weight=float(request.form["weight"])
        height=float(request.form["height"])

        bmi=round(weight/(height*height),2)

        if bmi<18.5:
            category="Underweight"
        elif bmi<25:
            category="Normal Weight"
        elif bmi<30:
            category="Overweight"
        else:
            category="Obese"

    return render_template_string(HTML,bmi=bmi,category=category)

if __name__=="__main__":
    app.run(debug=True)