from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired


class RegistrationForm(FlaskForm):
    f_name = StringField("Имя: ", validators=[DataRequired(), Length(min=2, max=20)])
    l_name = StringField("Фамилия: ", validators=[DataRequired(), Length(min=2, max=20)])
    m_name = StringField("Отчество: ", validators=[DataRequired(), Length(min=2, max=20)])
    rf_id = StringField("RFID: ", validators=[DataRequired()])
    submit = SubmitField("Зарегестрировать")
