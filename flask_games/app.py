from flask import Flask, render_template, request
from DFS import solve

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('base.html')

@app.route('/operation_result/', methods=['POST'])
def operation_result():
    A1 = request.form['A1']
    A2 = request.form['A2']
    A3 = request.form['A3']
    A4 = request.form['A4']
    B1 = request.form['B1']
    B2 = request.form['B2']
    B3 = request.form['B3']
    B4 = request.form['B4']
    C1 = request.form['C1']
    C2 = request.form['C2']
    C3 = request.form['C3']
    C4 = request.form['C4']
    D1 = request.form['D1']
    D2 = request.form['D2']
    D3 = request.form['D3']
    D4 = request.form['D4']
    
    # create Board

    board = [[A1, A2, A3, A4], [B1, B2, B3, B4], [C1, C2, C3, C4], [D1, D2, D3, D4]]

    result = [x for x in sorted(set(solve(board)), key=len, reverse=True)]
    return result

    # create static Trie (can be used across all games, using same set of words from dictionary.json)
    # first create Trie
    # then run dictionary through Trie so it is stored and doesn't have to be set up each time

    # DFS through actual board
