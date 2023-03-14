from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Length, DataRequired, NumberRange


class RegistrationForm(FlaskForm):
    f_name = StringField("Имя: ", validators=[DataRequired(), Length(min=2, max=20)])
    l_name = StringField("Фамилия: ", validators=[DataRequired(), Length(min=2, max=20)])
    m_name = StringField("Отчество: ", validators=[DataRequired(), Length(min=2, max=20)])
    rf_id = StringField("RFID: ", validators=[DataRequired()])
    submit = SubmitField("Зарегестрировать")


class LimitForm(FlaskForm):
    amount = IntegerField("Количество последних проходов: ", validators=[DataRequired(),
                                                                         NumberRange(1, 100)], default=10)
    submit = SubmitField("Вывести")


class RF_IDForm(FlaskForm):
    rf_id = StringField("RF_ID сотрудника: ", validators=[DataRequired(), Length(min=2, max=20)], default="")
    submit = SubmitField("Вывести количество рабочих часов за месяц")


class AdminForm(FlaskForm):
    rf_id = StringField("Введите RF_ID администратора: ", validators=[DataRequired(),
                                                                      Length(min=2, max=20)], default="")
    submit = SubmitField("Войти")
