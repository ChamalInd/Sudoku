from flask import Flask, render_template, request, jsonify, redirect

from helper.board import generate

# defining global variables 
levels = ['easy', 'medium', 'hard', 'extreme']
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
    global game_board, full_board, difficulty, levels

    if request.method == 'GET':
        # checking for difficulty level 
        difficulty_level = request.args.get('difficulty')
        difficulty = levels.index(difficulty_level)
        
        # generating the board 
        full_board, game_board = generate(difficulty)
    
    if request.method == 'POST':
        if request.form.get('action') == 'home':
            return redirect('/')
        if request.form.get('action') == 'replay':
            return redirect(f'/game?difficulty={levels[difficulty]}')

    return render_template('game.html', board=game_board, difficulty=difficulty_level)


@app.route('/syncServer', methods=['POST'])
def sync_with_frontend():
    # keep track on board 
    if request.get_json()['status'] == 'Update-Board':
        board = request.get_json()['board']
        current = request.get_json()['active']
        
        server_message = 'incorrect'
        if board[current[0]][current[1]][current[2]] == full_board[current[0]][current[1]][current[2]]:
            server_message = 'done'

        if board == full_board:
            server_message = 'done'

        return jsonify(
            {
                'status': 'updated',
                'server_message': server_message
            }
        )

    # calculating score
    if request.get_json()['status'] == 'Calculate-Score':
        # gathering data 
        time = request.get_json()['totalTime']
        mistakes = request.get_json()['totalMistakes']

        # base score
        base_score = [1000, 4000, 7000, 10000]

        # time bonus 
        time_bonus = [180, 480, 900, 1800]
        time_bonus_score = time_bonus[difficulty] - time

        # calculating the score 
        score = (base_score[difficulty] + time_bonus_score) * (0.9 ** mistakes)

        return jsonify(
            {
                'status': 'recived',
                'score': round(score, 0),
                'base_score': base_score[difficulty],
                'time_bonus': time_bonus_score
            }
        )
