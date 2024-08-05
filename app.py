
from flask import Flask, jsonify, request

app = Flask(__name__)

def suma_ops(op1,op2):
    calculo = op1 + op2
    return calculo

@app.route('/suma', methods = ['POST'])
def suma_temp():
    data = request.get_json()
    op1=data.get('op1')
    op2=data.get('op2') 
    result= suma_ops(op1,op2)   
    return jsonify({"Suma": result})
    
def resta_ops(op1,op2):
    calculo = op1 - op2
    return calculo

@app.route('/resta', methods = ['POST'])
def resta_temp():
    data = request.get_json()
    op1=data.get('op1')
    op2=data.get('op2') 
    result= resta_ops(op1,op2)   
    return jsonify({"Resta": result})    

def div_ops(op1,op2):
    calculo = op1 / op2
    return calculo

@app.route('/division', methods = ['POST'])
def div_temp():
    data = request.get_json()
    op1=data.get('op1')
    op2=data.get('op2') 
    result= div_ops(op1,op2)   
    return jsonify({"División": result})    

def mul_ops(op1,op2):
    calculo = op1 * op2
    return calculo

@app.route('/multiplicacion', methods = ['POST'])
def mul_temp():
    data = request.get_json()
    op1=data.get('op1')
    op2=data.get('op2') 
    result= mul_ops(op1,op2)   
    return jsonify({"Multiplicación": result})    

if __name__ == '__main__':
    app.run(debug=False)
