from flask import Flask
from views.views import views

app = Flask(__name__)
# TODO: replace key into env, create .env file (for Yuri)
app.secret_key = "23123145435667"
app.register_blueprint(views)

if __name__ == "__main__":
    app.run()
