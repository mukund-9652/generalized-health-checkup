from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return ('home.html')

@app.route('/input',methods=['GET','POST'])
def input():
    if (request.method == "POST"):
        return 0
    else:
        return 0
        

@app.route('/output')
def output():
    return render_template('output.html',,)



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
    
    return str(bmr)+"clories/day"

def bmr(wt,ht,at,gt):
    weight = float(wt)
    height = float(ht)
    age = int(at)
    gender=str(gt)
    bmi=((weight)/(height**2))*1000
    print(str(bmi)[:4])
    bmi=bmi*10
    if(bmi<16):
        print("Severe Thinness")
    elif(bmi>=16 and  bmi<17):
        print("Moderate Thinness")
    elif(bmi>=17 and  bmi<18.5):
        print("Mild Thinness")
    elif(bmi>=18.5 and bmi<25):
        print("Normal")
    elif(bmi>=25 and bmi<30): 
        print("Overweight")
    elif(bmi>=30 and bmi<35):
        print("Obese Class I")
    elif(bmi>=35 and bmi<40):
        print("Obese Class II")
    elif(bmi>40):
        print("Obese Class III")

def eye_patch():
    return 0


if __name__=="__main__":
    app.run(debug=True)