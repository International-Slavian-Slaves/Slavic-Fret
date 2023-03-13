from flask import Flask, render_template, url_for, request, redirect, flash, get_flashed_messages
from views.views import views
from views.forms import RF_IDForm, AdminForm
from controllers.controllers import get_hours, check_admin
from flask_login import LoginManager, login_user, login_required
from views.admin_login import AdminLogin

app = Flask(__name__)
# TODO: replace key into env, create .env file (for Yuri)
app.secret_key = "23123145435667"
app.register_blueprint(views)

login_manager = LoginManager(app)


@app.errorhandler(404)
def handle404(error):
    return render_template("not_found.html")

@app.errorhandler(401)
def handle401(error):
    return render_template("unauthorized.html")

@login_manager.user_loader
def load_user(user_id):
    return AdminLogin().get_data(user_id)

@app.route("/login", methods=['GET', 'POST'])
def login_admin():
    if request.method == "POST":
        user = check_admin(request.form['rf_id'])
        print(user)
        if user and user[0] == "1111":
            userlogin = AdminLogin().create(user)
            login_user(userlogin)
            return redirect(url_for("views.index"))
        else:
            flash("Попытка входа не удалась, попробуйте снова")
    return render_template("login.html", form=AdminForm())


@app.route("/hours", methods=['GET', 'POST'])
@login_required
def get_month_time():
    response = ""
    if request.method == 'POST':
        dict = request.form.to_dict()
        response = get_hours(dict['rf_id'])
    return render_template("month_times.html", form=RF_IDForm(), response=response)


if __name__ == "__main__":
    app.run()
