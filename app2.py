from flask import Flask,jsonify,request 
from classifier2 import get_pred

app=Flask(__name__)
@app.route("/predict-digit",methods=["POST"])

def pred_digit():
    img=request.files.get("digit")
    pred=get_pred(img)
    return jsonify({
        "pred":pred
    }),200

if(__name__=="__main__"):
    app.run(debug=True)
    
