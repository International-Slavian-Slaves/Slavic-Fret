from flask import Flask, render_template, request
from local_logging import logger
from views.form import RegistrationForm
from controllers.controller import register_user

app = Flask(__name__)
# TODO: replace key into env, create .env file (for Yuri)
app.secret_key = "23123145435667"

users = [{"first_name": "Иван", "second_name": "Иванов", "status": "inside"},
         {"first_name": "Зиновий", "second_name": "Иванов", "status": "outside"}]  # array created to try jinja


@app.route("/")  # theese funcs will be added to views later
@app.route("/index")
def index():
    return render_template('index.html', users=users)


@app.route("/registration", methods=['GET', 'POST'])
def registartion():
    logger.debug(request.method)
    if request.method == 'POST':
        logger.debug(request.form)
        register_user(request.form)
        logger.info(request.form)
    return render_template('registration.html', form=RegistrationForm())


if __name__ == "__main__":
    app.run()
