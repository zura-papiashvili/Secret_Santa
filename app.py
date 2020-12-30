from flask import Flask, render_template, session, redirect, url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, DateField,TextAreaField,SelectField,FileField
from wtforms.validators import DataRequired, Email, EqualTo
# from flask_mail import Mail, Message
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

app = Flask(__name__)


app.config['SECRET_KEY'] = 'mysecretkey'
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'papiashvil@gmail.com'
# app.config['MAIL_PASSWORD'] = 'fsdqudsdyqcvxrch'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True



class LetterForm(FlaskForm):
    file = FileField(validators=[DataRequired()])
    letter_text = StringField('საიდუმლო კოდი', validators=[DataRequired()],
                              render_kw={"placeholder": "M**"})
    submit = SubmitField('გაგზავნა')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = LetterForm()

    if form.validate_on_submit():
        session['filename'] = secure_filename(form.file.data.filename)
        form.file.data.save('static/uploads/' + session['filename'])

        session["letter_text"] = form.letter_text.data
        # msg = Message('Future me', sender='papiashvil@gmail.com', recipients=['papiashvil@gmail.com'])
        code = session["letter_text"]

        if code=='M16':
            flash('ნანიკო შენ სწორად გამოიცანი ნისლეულის სახელი')
            return redirect(url_for('report_2'))
        else:
            flash('პასუხი არასწორია')

    return render_template('home.html',form=form)


@app.route('/report',methods=['GET','POST'])
def report():

    return render_template('report.html')

@app.route('/report_2',methods=['GET','POST'])
def report_2():

    return render_template('report_2.html')

@app.route('/puzzle',methods=['GET','POST'])
def puzzle():

    return render_template('puzzle.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
