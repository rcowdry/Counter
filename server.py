from flask import Flask, redirect, render_template, session

app = Flask(__name__)
app.secret_key = "This is a secret key"
# session["counter"] = 1


@app.route("/<int:no>")
@app.route("/")
def session_counter(no=1):
    if "counter" in session:
        session["counter"] += no
    else:
        session["counter"] = no

    return render_template("index.html", counter=session["counter"])


@app.route("/destroy_session")
def destroy_session():
    session.clear()

    return redirect("/")


if (__name__) == "__main__":
    app.run(debug=True, threaded=True)
