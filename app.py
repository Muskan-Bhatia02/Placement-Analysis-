from flask import Flask, render_template, url_for, request
import pandas as pd
# from sklearn import linear_model


app = Flask(__name__, static_url_path='/static')




df = pd.read_excel('static/PCET 2022.xlsx')



data = pd.read_excel('static/Regression.xlsx')
df1 = pd.DataFrame(data)



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/alumnisearch', methods=['GET', 'POST'])
def alumnisearch():
    # if request.method=='POST':
    #     alumni = request.form['alumni']
    #     todo = Todo(alumni= alumni)
    #     # db.session.add(todo)
    #     print(todo)

    return render_template("alumnisearch.html")


@app.route('/result', methods=['POST', 'GET'])
def result():
    context = {}
    if request.method=='POST':
        output = request.form['fname']
        print(output)
        name = output


        flag = 0
        for i in range(0, len(df)):
            if output == df.iat[i, 2]:
                flag=1
                break

        if flag == 1:
            # print(df.at[i,'Email Address'])
            # print(df.at[i, 'College Name'])
            # print(df.at[i, 'Branch / Specialization'])
            # print(df.at[i, 'Company Placed Final Offers'])

            context['email'] = df.at[i,'Email Address']
            context['college'] = df.at[i,'College Name']
            context['branch'] = df.at[i,'Branch / Specialization']
            context['offer'] = df.at[i,'Company Placed Final Offers']
        else:
            print("Not found!")

    return render_template("alumnisearch.html", name = context)



@app.route('/prediction')
def prediction():
    return render_template("prediction.html")

@app.route('/visualisation')
def visualisation():
    return render_template("visualisation.html")






# @app.route('/predict', methods=['POST', 'GET'])
# def predict():
#     # content = {}
#     if request.method=='POST':
#         ssc = request.form['ssc']
#         hsc = request.form['hsc']
#         engg = request.form['engg']
#         cocubes = request.form['cocubes']
#         cod = request.form['cod']

        
#         x = df1[['ssc_p','hsc_p','degree_p','etest_p','mba_p']]
#         y = df1['salary']

#         regr = linear_model.LinearRegression()
#         regr.fit(x,y)
#         predicted_salary = regr.predict([[ssc,hsc,engg,cocubes,cod]])

#     return render_template("prediction.html", name = predicted_salary)



if __name__ == "__main__":
    app.run(debug=True, port=8000)