from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import RadioField, SelectField, StringField, SubmitField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure secret key

class RobotForm(FlaskForm):
    made_of_metal = RadioField('Are you made of metal?', choices=[('yes', 'Yes'), ('no', 'No')],
                               validators=[validators.InputRequired()])
    constructed_by = SelectField('Were you constructed by the Sirius Cybernetics Corporation?',
                                 choices=[('yes', 'Yes'), ('no', 'No')],
                                 validators=[validators.InputRequired()])
    dreams_of_being = StringField('Do you dream of being ED-209 when you grow up?',
                                  validators=[validators.InputRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RobotForm()

    if form.validate_on_submit():
        metal_answer = form.made_of_metal.data
        construction_answer = form.constructed_by.data
        dreams_answer = form.dreams_of_being.data.lower().strip()

        if metal_answer == 'yes' and construction_answer == 'yes' and 'ed-209' in dreams_answer:
            result = "You're a robot!"
        else:
            result = "Hello fellow human."

        return render_template('result.html', result=result)

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
