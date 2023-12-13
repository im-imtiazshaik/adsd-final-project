# Importing necessary modules
from bottle import Bottle, run, template, request, redirect
import sqlite3

# Creating a Bottle app
app = Bottle()

# SQLite database initialization
db = sqlite3.connect('football.db')
cursor = db.cursor()

# Creating tables if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS national_team (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        jersey_number INTEGER,
        player_name TEXT,
        team_name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS club_team (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        jersey_number INTEGER,
        player_name TEXT,
        club_name TEXT
    )
''')

db.commit()

# CRUD operations for the national_team table
def create_national_player(jersey_number, player_name, team_name):
    cursor.execute('''
        INSERT INTO national_team (jersey_number, player_name, team_name)
        VALUES (?, ?, ?)
    ''', (jersey_number, player_name, team_name))
    db.commit()

def read_national_players():
    cursor.execute('SELECT * FROM national_team')
    return cursor.fetchall()

def update_national_player(player_id, jersey_number, player_name, team_name):
    cursor.execute('''
        UPDATE national_team
        SET jersey_number=?, player_name=?, team_name=?
        WHERE id=?
    ''', (jersey_number, player_name, team_name, player_id))
    db.commit()

def delete_national_player(player_id):
    cursor.execute('DELETE FROM national_team WHERE id=?', (player_id,))
    db.commit()

# CRUD operations for the club_team table
def create_club_player(jersey_number, player_name, club_name):
    cursor.execute('''
        INSERT INTO club_team (jersey_number, player_name, club_name)
        VALUES (?, ?, ?)
    ''', (jersey_number, player_name, club_name))
    db.commit()

def read_club_players():
    cursor.execute('SELECT * FROM club_team')
    return cursor.fetchall()

def update_club_player(player_id, jersey_number, player_name, club_name):
    cursor.execute('''
        UPDATE club_team
        SET jersey_number=?, player_name=?, club_name=?
        WHERE id=?
    ''', (jersey_number, player_name, club_name, player_id))
    db.commit()

def delete_club_player(player_id):
    cursor.execute('DELETE FROM club_team WHERE id=?', (player_id,))
    db.commit()

# Route for the home page
@app.route('/')
def index():
    national_players = read_national_players()
    club_players = read_club_players()
    return template('index', national_players=national_players, club_players=club_players)

# Routes for national players
@app.route('/national/add', method='GET')
def add_national_player():
    return template('add_national')

@app.route('/national/add', method='POST')
def do_add_national_player():
    jersey_number = request.forms.get('jersey_number')
    player_name = request.forms.get('player_name')
    team_name = request.forms.get('team_name')
    create_national_player(jersey_number, player_name, team_name)
    redirect('/')

@app.route('/national/edit/<player_id>', method='GET')
def edit_national_player(player_id):
    player = cursor.execute('SELECT * FROM national_team WHERE id=?', (player_id,)).fetchone()
    return template('edit_national', player=player)

@app.route('/national/edit/<player_id>', method='POST')
def do_edit_national_player(player_id):
    jersey_number = request.forms.get('jersey_number')
    player_name = request.forms.get('player_name')
    team_name = request.forms.get('team_name')
    update_national_player(player_id, jersey_number, player_name, team_name)
    redirect('/')

@app.route('/national/delete/<player_id>')
def do_delete_national_player(player_id):
    delete_national_player(player_id)
    redirect('/')

# Routes for club players
@app.route('/club/add', method='GET')
def add_club_player():
    return template('add_club')

@app.route('/club/add', method='POST')
def do_add_club_player():
    jersey_number = request.forms.get('jersey_number')
    player_name = request.forms.get('player_name')
    club_name = request.forms.get('club_name')
    create_club_player(jersey_number, player_name, club_name)
    redirect('/')

@app.route('/club/edit/<player_id>', method='GET')
def edit_club_player(player_id):
    player = cursor.execute('SELECT * FROM club_team WHERE id=?', (player_id,)).fetchone()
    return template('edit_club', player=player)

@app.route('/club/edit/<player_id>', method='POST')
def do_edit_club_player(player_id):
    jersey_number = request.forms.get('jersey_number')
    player_name = request.forms.get('player_name')
    club_name = request.forms.get('club_name')
    update_club_player(player_id, jersey_number, player_name, club_name)
    redirect('/')

@app.route('/club/delete/<player_id>')
def do_delete_club_player(player_id):
    delete_club_player(player_id)
    redirect('/')

# Running the application
if __name__ == '__main__':
    run(app, debug=True)
