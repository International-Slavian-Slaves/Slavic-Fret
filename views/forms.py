from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField
from wtforms.validators import Length, DataRequired, NumberRange

import local_logging


class RegistrationForm(FlaskForm):
    f_name = StringField("Имя: ", validators=[DataRequired(), Length(min=2, max=20)])
    l_name = StringField("Фамилия: ", validators=[DataRequired(), Length(min=2, max=20)])
    m_name = StringField("Отчество: ", validators=[DataRequired(), Length(min=2, max=20)])
    rf_id = StringField("RFID: ", validators=[DataRequired()])
    submit = SubmitField("Зарегестрировать")


class LimitForm(FlaskForm):
    amount = IntegerField("Значение: ", validators=[DataRequired(), NumberRange(1, 100)], default=10)
    submit = SubmitField("Вывести")


class RF_IDForm(FlaskForm):
    rf_id = StringField("Значение: ", validators=[DataRequired(), Length(min=2, max=20)], default="")
    submit = SubmitField("Вывести")
