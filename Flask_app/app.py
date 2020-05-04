from flask import Flask
from flask import render_template, redirect, flash, request, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
import psycopg2
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SECRET_KEY'] = '1234abcdef'
Bootstrap(app)
db = SQLAlchemy(app)

try:
    connection = psycopg2.connect(user="postgres",
                                  password="Jimma123!",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="member")
    cursor = connection.cursor()
# Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

# Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)


class LoginForm(FlaskForm):
    username = StringField('username', validators=[
                           InputRequired(), Length(min=4, max=10)])
    password = PasswordField('password', validators=[
                             InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    firstname = StringField('firstname', validators=[
                            InputRequired(), Length(min=4, max=15)])
    lastname = StringField('lastname', validators=[
                           InputRequired(), Length(min=4, max=15)])
    username = StringField('username', validators=[
                           InputRequired(), Length(min=4, max=15)])
    email = StringField('email', validators=[InputRequired(), Email(
        message='Not a valid email address'), Length(max=50)])
    password = PasswordField('password', validators=[
                             InputRequired(), Length(min=8, max=80)])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        #user = User(firstname=firstname,lastname=lastname,username=username,email=email,password=password)
        #print('x')
        db.session.add(self)
        db.session.commit()

        # create cursor
        #cursor = connection.cursor()
        # execute cursor
        #sql = "INSERT INTO users (firstname,lastname,username,email,password) VALUES (%s,%s,%s,%s,%s)"
        #val = ("John", "Doey", "JohnDoey", "johndoey@yahoo.com", "Jdoey@123")
        #cursor.execute(sql, val)
        # commit to DB
        #connection.commit()
        # close the connection
        #cursor.close()

        flash('You are now a registered user', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', title='SignUp', form=form)


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/logout')
def logout():
    return render_template('logout.html')


if __name__ == '__main__':
    app.run(debug=True)
