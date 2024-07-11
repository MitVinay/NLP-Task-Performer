from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    TextAreaField,
    StringField
)
from wtforms.validators import DataRequired

class InputForm(FlaskForm):

    ner = TextAreaField(
        label = "Named Entity Recoginition",
        validators=[DataRequired()]
    )

    submit = SubmitField(label="Predict")
    