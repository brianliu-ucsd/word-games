from flask import Flask, render_template, request
from DFS import solve

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('base.html')

@app.route('/operation_result/', methods=['POST'])
def operation_result():
    A1 = request.form['A1'].lower()
    A2 = request.form['A2'].lower()
    A3 = request.form['A3'].lower()
    A4 = request.form['A4'].lower()
    B1 = request.form['B1'].lower()
    B2 = request.form['B2'].lower()
    B3 = request.form['B3'].lower()
    B4 = request.form['B4'].lower()
    C1 = request.form['C1'].lower()
    C2 = request.form['C2'].lower()
    C3 = request.form['C3'].lower()
    C4 = request.form['C4'].lower()
    D1 = request.form['D1'].lower()
    D2 = request.form['D2'].lower()
    D3 = request.form['D3'].lower()
    D4 = request.form['D4'].lower()
    
    board = [[A1, A2, A3, A4], [B1, B2, B3, B4], [C1, C2, C3, C4], [D1, D2, D3, D4]]

    result = [x for x in sorted(set(solve(board)), key=len, reverse=True)]
    return render_template('result.html', result = result)