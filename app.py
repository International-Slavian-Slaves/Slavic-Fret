from flask import Flask, render_template
from flask_login import LoginManager

from views.admin_login import AdminLogin
from views.admin_view import admin
from views.views import views

app = Flask(__name__)
# TODO: replace key into env, create .env file (for Yuri)
app.secret_key = "23123145435667"
app.register_blueprint(views)
app.register_blueprint(admin)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return AdminLogin().get_data(user_id)


@app.errorhandler(404)
def handle404(error):
    return render_template("not_found.html")


@app.errorhandler(401)
def handle401(error):
    return render_template("unauthorized.html")


if __name__ == "__main__":
    app.run()
