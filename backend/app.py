from flask import Flask,request,jsonify
from calculator import calculate


app = Flask(__name__)

@app.route('/api',methods=['GET','POST'])
def home():
    voice_input = str(request.args['text'])
    result = calculate(voice_input)
    return jsonify(result)

if __name__ == '__main__':

    app.run()
