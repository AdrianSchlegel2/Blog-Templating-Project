from flask import Flask, render_template
import requests


app = Flask(__name__)
post_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = post_response.json()



@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/blog/<int:num>")
def post(num):
    return render_template("post.html", num=num, posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
