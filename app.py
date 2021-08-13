from flask import Flask, render_template, request

app = Flask(__name__)


import sqlite3 as sql

conn = sql.connect('database.db')



@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            name = request.form['nm']
            cmnt = request.form['cmnt']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("""INSERT INTO comments (name, comment)
                VALUES (?, ?)
                """, (name, cmnt))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:

            return render_template("comment.html", msg=msg)
            con.close()


@app.route('/posts')
def posts():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from comments")

    rows = cur.fetchall();
    return render_template("posts.html", rows=rows)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/memes")
def memes():
    return render_template('memes.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/enternew')
def new_comment():
   return render_template('comment.html')



@app.route("/HistoryMemes")
def HistoryMemes():
    return render_template('HistoryMemes.html')

@app.route("/WorldWar")
def WorldWar():
    return render_template('WorldWar.html')

@app.route("/Communist")
def Communist():
    return render_template('Communist.html')


@app.errorhandler(404)
def handler404(_):
    return render_template('404.html')


if __name__ == "__main__":
    app.run()