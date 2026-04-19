from flask import Flask, render_template, redirect

from helper.board import full_board, game_board, generate_game_board, print_board


# configuring app
app = Flask(__name__)
# secret key for flask flash notifications 
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.after_request
def after_request(response):
    # Ensure responses aren't cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=['POST', 'GET'])
def index():
    # game_board = generate_game_board(full_board, 3)
    return render_template('index.html')