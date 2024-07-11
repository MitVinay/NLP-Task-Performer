from flask_wtf import FlaskForm
import pandas as pd
from wtforms import (
    SubmitField,
    TextAreaField
)

from wtforms.validators import DataRequired

class InputForm(FlaskForm):

    airline = TextAreaField(
        label = "Named Entity Recoginition",
        validators=[DataRequired()]
    )

    submit = SubmitField(label="Predict")