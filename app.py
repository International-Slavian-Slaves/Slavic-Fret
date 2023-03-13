from flask import Flask, render_template, url_for
from views.views import views

app = Flask(__name__)
# TODO: replace key into env, create .env file (for Yuri)
app.secret_key = "23123145435667"
app.register_blueprint(views)


@app.errorhandler(404)
def handle404(error):
    return render_template("not_found.html")

@app.route("")
def get_month_time():
    return render_template("month_times.html")

if __name__ == "__main__":
    app.run()
