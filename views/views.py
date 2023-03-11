from flask import Blueprint, render_template, request
from local_logging import logger
from views.forms import RegistrationForm, LimitForm
from controllers.controllers import register_user, get_recent_passes, get_fun, get_locations

views = Blueprint('views', __name__, template_folder='..templates')


@views.route("/", methods=['GET', 'POST'])  # theese funcs will be added to views later
@views.route("/index", methods=['GET', 'POST'])
def index():
    limit = 10
    if request.method == 'POST':
        logger.info(request.form)
        data = request.form.to_dict()
        limit = int(data['amount'])
    passes_data = get_recent_passes(limit)
    return render_template('index.html', passes_data=passes_data, form=LimitForm())


@views.route("/registration", methods=['GET', 'POST'])
def registration():
    logger.debug(request.method)
    if request.method == 'POST':
        request_data = request.form
        register_user(request_data)
        logger.info(request_data)
    return render_template('registration.html', form=RegistrationForm())


@views.route("/fun")
def kill_yourself():
    msg, result = get_fun()
    return render_template("easter_result.html", msg=msg, result=result)


@views.route("/locations")
def locate_users():
    location_data = get_locations()
    return render_template("locations.html", location_data=location_data)



