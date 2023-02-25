from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Guitar

main = Blueprint('main', __name__)


@main.route('/')
def index():
    guitars = Guitar.query.all()
    return render_template('index.html', guitars=guitars)
