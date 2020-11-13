from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Calc(Resource):
    '''
    Array containing 2 or more matrices and calculate the product of those matrices.
    '''
    def post(self):
        #Get posted data:
        postedData = request.get_json()

        #Read Matrices from txt file
        with open('xmat.txt', 'r') as fx:
            x = [[int(num) for num in line.split(',')] for line in fx]
        with open('ymat.txt', 'r') as fy:
            y = [[int(num) for num in line.split(',')] for line in fy]
        
        #for loop approach
        '''
        for i in range(len(x)):
        # iterate through columns of Y
             for j in range(len(y[0])):
        # iterate through rows of Y
                 for k in range(len(y)):
                     result[i][j] += x[i][k] * y[k][j]
        '''
        #List comprehension approach
        result = [[ sum(m * n for m , n in zip(x_row,y_col)) for y_col in zip(*y)] for x_row in x ]
        retMap = {
            'Message': result,
            'Status Code': 200
        }
        return jsonify(retMap)

api.add_resource(Calc, "/calc")

@app.route('/')
def matrix_product():
    return "Matrix Product Calculation!"

if __name__=="__main__":
    app.run(debug=True)
