from flask import Flask, Response
import json
import os

app = Flask(__name__)

@app.route('/api/v1.0/students',methods = ['GET'])
def students():
    students_list = [
        { #start opening

            'name':'Asabeneh',
            'country':'Finland',
            'city':'Helsinki',
            'skills':['HTML','CSS','JavaScript','Python']
        },

        {
            'name':'David',
            'country':'UK',
            'city':'London',
            'skills':['Python','MongoDB']
        },

        {
        'name':'John',
        'country':'Sweden',
        'city':'Stockholm',
        'skills':['Java','C#'] 
        }
    ]

    return Response(json.dumps(students_list), mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
