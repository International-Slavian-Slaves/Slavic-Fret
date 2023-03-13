from flask import Flask, render_template, url_for, request
from views.views import views
from views.forms import RF_IDForm
from controllers.controllers import get_hours

app = Flask(__name__)
# TODO: replace key into env, create .env file (for Yuri)
app.secret_key = "23123145435667"
app.register_blueprint(views)


@app.errorhandler(404)
def handle404(error):
    return render_template("not_found.html")


@app.route("/hours", methods=['GET', 'POST'])
def get_month_time():
    response = ""
    if request.method == 'POST':
        app = request.form.to_dict()
        response = get_hours(app['rf_id'])
    return render_template("month_times.html", form=RF_IDForm(), response=response)


if __name__ == "__main__":
    app.run()
