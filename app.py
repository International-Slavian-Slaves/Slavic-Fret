from flask import Flask, render_template, request
from local_logging import logger
from views.form import RegistrationForm
from controllers.controllers import register_user, get_recent_passes, get_fun, get_locations

app = Flask(__name__)
# TODO: replace key into env, create .env file (for Yuri)
app.secret_key = "23123145435667"


@app.route("/")  # theese funcs will be added to views later
@app.route("/index")
def index():
    passes_data = get_recent_passes()
    return render_template('index.html', passes_data=passes_data)


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    logger.debug(request.method)
    if request.method == 'POST':
        request_data = request.form
        register_user(request_data)
        logger.info(request_data)
    return render_template('registration.html', form=RegistrationForm())


@app.route("/fun")
def kill_yourself():
    msg, result = get_fun()
    return render_template("easter_result.html", msg=msg, result=result)


@app.route("/locations")
def locate_users():
    location_data = get_locations()
    return render_template("locations.html", location_data=location_data)


if __name__ == "__main__":
    app.run()
