from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/input',methods=['GET','POST'])
def input():
    if (request.method == "POST"):
        wt=request.form["weight"]
        ht=request.form["height"]
        at=request.form["age"]
        gt= str(request.form.get('gender'))
        print(gt)
        if "gender" in request.form:
            gt = request.form["gender"]
        else:
            gt = "m"
        print (gt)
        if "exercise" in request.form:
            activity = request.form["exercise"]
        else:
            activity = 0
        body_mass_index=bmi(wt,ht,at,gt)
        basal_metabolic_rate=bmr(wt,ht,at,gt)
        cal=calorie(basal_metabolic_rate,gt,activity)
        bodyFat=body_fat(body_mass_index[0],gt,int(at))
        ideal=ideal_wt(ht,gt)
        return render_template('output.html',IDEAL=ideal,BMI=body_mass_index[0],BMR=basal_metabolic_rate,SIZE=body_mass_index[1],CALORIE=cal,BODYFAT=bodyFat[0],OBESITY=bodyFat[1])
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
        bmr = round(66.5 + (13.75 * weight) + (5 * height) - (6.755 * age), 2)
    else:
        bmr = round(655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age), 2)

    #bmr = round(bmr)
    
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

def calorie(b_m_r,gender,act):
    cal=0
    if act==0:
        cal=b_m_r*1.2
    elif act==1:
        cal=b_m_r*1.375
    elif act==2:
        cal=b_m_r*1.549
    out=""
    #cal=2600
    if (gender=="m"):
        if (cal>3000 ):
            out=" number of calories required to maintain your weight seems high"
        elif(cal>2000 and cal<3000):
            out=" number of calories required to maintain your weight seems normal"
        else:
            out=" number of calories required to maintain your weight seems low"
    else: 
        if(cal>1600 and cal<2400):
            out=" number of calories required to maintain your weight seems normal"
        elif(cal>2400):
            out=" number of calories required to maintain your weight seems high"
        else:
            out=" number of calories required to maintain your weight seems low"

    return out

def body_fat(b_m_i,gender,age):
    out=[]
    b_m_i=float(b_m_i)
    age=float(age)
    if(gender=='m'):
        body_fat = round(1.20*b_m_i + 0.23*age - 16.2, 2)
        out.append("Your Body fat percentage is: "+str(abs(body_fat))+"%")
        if(body_fat>=20.0 and body_fat<=25.0):
             out="Your Body Fat is of required amount"
        else:
           out.append("You are obese")
    else:
        body_fat = round(1.20*b_m_i + 0.23*age - 5.4, 2)
        out.append("Your Body fat percentage is: "+str(abs(body_fat))+"%")
        if(body_fat>=8.0 and body_fat<=14.0):
            out.append("Your Body Fat is of required amount")
        else:
            out.append("You are obese")
    return out


def ideal_wt(ht, gt):
    height = int(ht)
    gender = gt

    def cm_to_inch(height):
        return height/2.54

    diff = cm_to_inch(height) - 60
    if(gender == "m"):
        ideal_wt = 52 + 1.9 * diff

    elif(gender == "f"):
        ideal_wt = 49 + 1.7 * diff

    return "Your ideal weight is "+ str(round(ideal_wt, 1)) + "kg"



if __name__=="__main__":
    app.run(debug=True)