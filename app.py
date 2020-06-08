from flask import Flask, request, render_template

app = Flask("__name__")


@app.route("/", methods=["POST", "GET"])
def home():
    str1 = ''
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        str1 = username + ' ' + password
    return render_template("index.html", pl=str1)


if __name__ == "__main__":
    app.run()
