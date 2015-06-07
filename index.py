from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
