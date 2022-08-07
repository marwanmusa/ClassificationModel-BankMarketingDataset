from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# open model
def open_model(model_path):
    """
    helper function for loading model
    """
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

model_marketing = open_model("pipe_project.pkl") # pandas dataframe

# Fungsi untuk inference iris
def inference_data(data, model):
    """
    input : list with lenght : 14 --> [1, admin./blue-collar/entrepreneur/housemaid/management/retired/self-employed/services/student/technician/unemployed, 
                                       divorced/married/single, illiterate/basic.4y/basic.6y/basic.9y/high.school/university.degree/professional.course, 
                                       yes/no, yes/no, cellular/telephone, mar/apr/may/jun/jul/aug/sep/oct/nov/dec, mon/tue/wed/thu/fri, 2, 3, 0-7, 
                                       nonexistent/failure/success, 4]
    output : predicted class (idx, label)
    """
    LABEL = ["Not Deposit", "Will Deposit"]
    columns = ['age', 'job', 'marital', 'education', 'housing', 'loan',
       'contact', 'month', 'day_of_week', 'duration', 'campaign',
       'previous', 'poutcome', 'cons.price.idx']
    data = pd.DataFrame([data], columns=columns)
    res = model.predict(data)
    return res[0], LABEL[res[0]]
    

# halaman home
@app.route("/")
def homepage():
    return "<h1> Deployment Model Backend!</h1>"
  
    
@app.route("/subscribe_prediction", methods=['POST'])
def titanic_predict():
    """
      content = 
    {
        'age': xx,
        'job': admin./blue-collar/entrepreneur/housemaid/management/retired/self-employed/services/student/technician/unemployed,
        'marital': divorced/married/single,
        'education': illiterate/basic.4y/basic.6y/basic.9y/high.school/university.degree/professional.course,
        'housing': yes/no,
        'loan': yes/no,
        'contact': cellular/telephone,
        'month': mar/apr/may/jun/jul/aug/sep/oct/nov/dec,
        'day_of_week': mon/tue/wed/thu/fri,
        'duration': xy,
        'campaign': xz,
        'previous': yy,
        'poutcome': nonexistent/failure/success,
        'cons.price.idx': yz        
    }
    """
    content = request.json
    newdata = [content['age'], 
               content['job'],
               content['marital'],
               content['education'],
               content['housing'],
               content['loan'], 
               content['contact'],
               content['month'],
               content['day_of_week'],
               content['duration'],
               content['campaign'],
               content['previous'],
               content['poutcome'],
               content['cons.price.idx']]
    res_idx, res_label = inference_data(newdata, model_marketing)
    result = {
        'label_idx' : str(res_idx),
        'label_name' : res_label
    }
    response = jsonify(success=True, result=result)
    return response, 200
    
# run app di local
# Jika deploy heroku komen baris dibawah
# app.run(debug=True) 