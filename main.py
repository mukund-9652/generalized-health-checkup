from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/input',methods=['GET','POST'])
def input():
    if (request.method == "POST"):
        wt=request.form["weight"]
        ht=request.form["height"]
        at=request.form["age"]
        gt= str(request.form.get('gender'))
        if "gender" in request.form:
            gt = request.form["gender"]
        else:
            gt = 1
        body_mass_index=bmi(wt,ht,at,gt)
        basal_metabolic_rate=bmr(wt,ht,at,gt)
        return render_template('output.html',BMI=body_mass_index[0],BMR=basal_metabolic_rate,SIZE=body_mass_index[1])
    else:
        return render_template("input.html")
        

@app.route('/output')
def output():
    if (request.method == "POST"):
        return render_template('home.html')
    else:
        return("output.html")
    



def bmr(wt,ht,at,gt):
    weight = float(wt)
    height = float(ht)
    age = int(at)
    gender=str(gt)
    if gender=='m':
        bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
    else:
        bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

    bmr = round(bmr)
    
    return bmr

def bmi(wt,ht,at,gt):
    weight = float(wt)
    height = float(ht)
    age = int(at)
    gender=str(gt)
    out=[]
    bmi=((weight)/(height**2))*1000
    out.append(str(bmi)[:4])
    bmi=bmi*10
    if(bmi<16):
        out.append("Severe Thinness")
    elif(bmi>=16 and  bmi<17):
        out.append("Moderate Thinness")
    elif(bmi>=17 and  bmi<18.5):
        out.append("Mild Thinness")
    elif(bmi>=18.5 and bmi<25):
        out.append("Normal")
    elif(bmi>=25 and bmi<30): 
        out.append("Overweight")
    elif(bmi>=30 and bmi<35):
        out.append("Obese Class I")
    elif(bmi>=35 and bmi<40):
        out.append("Obese Class II")
    elif(bmi>40):
        out.append("Obese Class III")
    return out

def eye_patch():
    return 0


if __name__=="__main__":
    app.run(debug=True)