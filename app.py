from flask import Flask, render_template, request, jsonify

from helper.board import generate, print_board

# defining global variables 
game_board = None
full_board = None
difficulty = None


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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game', methods=['POST', 'GET'])
def game():
    global game_board, full_board, difficulty

    if request.method == 'GET':
        # checking for difficulty level 
        levels = ['easy', 'medium', 'hard', 'extreme']
        difficulty = request.args.get('difficulty')
        difficulty_level = levels.index(difficulty)
        
        # generating the board 
        full_board, game_board = generate(difficulty_level)
        print_board(full_board)

    return render_template('game.html', board=game_board, difficulty=difficulty)

@app.route('/update-board', methods=['POST'])
def update_game_board():
    board = request.get_json()['current_state']
    if board == full_board:
        print('well done')
        
    
    return jsonify({'status': 'updated'})