from flask import Flask, render_template
from game_backend import *
from backend.enemies import *
from backend.player import *

app = Flask(__name__)
our_player = Player()

@app.route('/game')
def game():
  global our_player
  if our_player is None:
    our_player = Player()
  return render_template('game.html', player = our_player)

@app.route('/battle')
def battle():
  global current_enemy, our_player
  return render_template('battlescreen.html', enemy = current_enemy, player = our_player)

@app.route('/startbattle')
def startbattle():
  global current_enemy, our_player
  current_enemy = Pillow() 
  return render_template('battlescreen.html', enemy = current_enemy, player = our_player)

@app.route('/battle/skills')
def battle_skills():
  skills_list = ['Scratch', 'Water Gun', 'Screech', 'Surf']
  return render_template('skillslist.html', skills = skills_list, name = """Horn
    Flask""")

@app.route('/battle/items')
def battle_items():
  items_list = ['Boots', 'Dagger', 'HP Pots', 'Deathfire Grasp']
  return render_template('itemslist.html', items = items_list, name = """Horn
    Flask""")

@app.route('/battle/attack')
def battle_attack():
  global current_enemy, our_player
  current_enemy.health -= our_player.damage
  if current_enemy.is_alive():
    our_player.health -= current_enemy.damage
  return render_template('battleattack.html', enemy = current_enemy, player = our_player)

@app.route('/game/init')
def init():
  global health
  global mana
  health = 10
  mana = 10
  return 'Game initiated.'

@app.route('/game/printstats')
def printstats():
  global health
  global mana
  return 'Health ' + str(health) + ', ' + 'Mana ' + str(mana)

@app.route('/game/changestats')
def changestats():
  global health
  global mana
  health += 2
  mana -= 1
  return 'Health ' + str(health) + ', ' + 'Mana ' + str(mana)
  

@app.route('/post/<int:post_id>')
def show_post(post_id):
  # show the post with the given id, the id is an integer
  return 'Post ' + str(post_id)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/faq")
def view_faq():
  return render_template('faq.html')

@app.route("/index.py")
def something():
  return "asdf";

@app.route("/printstring/<string>")
def printstring(string):
  return string

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
