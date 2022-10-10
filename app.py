from flask import Flask,render_template,request
import mod2
app=Flask(__name__)

@app.route("/")
def sum_():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        # to_predict_list = request.form.get_data()
        print(to_predict_list)
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = to_predict_list 
        return render_template("result.html", prediction = mod2.get_input(*result))
if __name__=="__main__":
    app.run(debug=True)
