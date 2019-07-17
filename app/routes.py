from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import TitleForm, ContactForm, LoginForm, RegisterForm, PostForm
from app.models import Post, Contact


@app.route('/')
@app.route('/index')
@app.route('/index/<header>', methods=['GET'])
def index(header=''):
    products = [
        {
            'id': 1001,
            'title': 'Soap',
            'price': '3.98',
            'desc': 'Very clean soapy soap. Has soapness.'
        },
        {
            'id': 1002,
            'title': 'Grapes',
            'price': '2.50',
            'desc': 'Very clean soapy grapes. Has grapeness. Cleans your insides!'
        },
        {
            'id': 1003,
            'title': 'A Video Game',
            'price': '60',
            'desc': 'Very clean video gamey video game. Has game.'
        },
        {
            'id': 1004,
            'title': 'Happiness',
            'price': '100',
            'desc': 'Very clean happy times. Has good feels.'
        },
    ]

    return render_template('index.html', products=products, title='Home', header=header)


@app.route('/checkout')
def checkout():
    return render_template('checkout.html', title='Checkout')


@app.route('/title', methods=['GET', 'POST'])
def title():
    # create an instance of the form
    form = TitleForm()

    # write a conditional that checks if form was submitted properly, then do something with the data
    if form.validate_on_submit():
        # print(f'{form.title.data}') # name of form . name of input . data

        return redirect(url_for('index', header=form.title.data))


    return render_template('form.html', form=form, title='Change Title')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # TODO: setup code
        flash('You are now logged in!')
        return redirect(url_for('profile'))

    return render_template('form.html', form=form, title='Login')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # TODO: setup code
        flash('Thanks for registering!')
        return redirect(url_for('login'))

    return render_template('form.html', form=form, title='Register')

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        contact = Contact(
            name = form.name.data,
            email = form.email.data,
            message = form.message.data
        )

        # step 2: add the record to the stage
        db.session.add(contact)

        # step 3: commit the stage to the db
        db.session.commit()

        flash('Thanks for contacting us, we will be in touch soon')

        return redirect(url_for('contact'))

    return render_template('form.html', form=form, title='Contact Us')

# temporary variable for testing, generally don't declare variables here
# posts = [
#     {
#         'post_id': 1,
#         'tweet': 'My favorite suit is zoot.',
#         'date_posted': '6/22/2019'
#     },
#     {
#         'post_id': 2,
#         'tweet': 'My favorite suit is hearts.',
#         'date_posted': '7/10/2019'
#     },
#     {
#         'post_id': 3,
#         'tweet': 'My favorite suit is Roe vs. Wade.',
#         'date_posted': '7/17/2019'
#     }
# ]f

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    form = PostForm()

    if form.validate_on_submit():
        # step 1: create an instance of the db model
        post = Post(
            tweet = form.tweet.data
        )

        # step 2: add the record to the stage
        db.session.add(post)

        # step 3: commit the stage to the db
        db.session.commit()

        return redirect(url_for('profile'))

    # retrieve all posts and pass in to view
    posts = Post.query.all()

    # only return certain posts
    # posts = Post.query.filter_by(post_id=1).first()

    return render_template('profile.html', form=form, title='Profile', posts=posts)
