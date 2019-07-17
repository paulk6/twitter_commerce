from app import app
from flask import render_template, url_for, redirect
from app.forms import TitleForm, ContactForm, LoginForm, RegisterForm, PostForm


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
        pass

    return render_template('form.html', form=form, title='Login')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # TODO: setup code
        pass

    return render_template('form.html', form=form, title='Register')

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # TODO: setup code
        pass

    return render_template('form.html', form=form, title='Contact Us')

# temporary variable for testing, generally don't declare variables here
posts = [
    {
        'post_id': 1,
        'tweet': 'My favorite suit is zoot.',
        'date_posted': '6/22/2019'
    },
    {
        'post_id': 2,
        'tweet': 'My favorite suit is hearts.',
        'date_posted': '7/10/2019'
    },
    {
        'post_id': 3,
        'tweet': 'My favorite suit is Roe vs. Wade.',
        'date_posted': '7/17/2019'
    }
]

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    form = PostForm()

    if form.validate_on_submit():
        posts.append(
            {
            'post_id': len(posts) + 1,
            'tweet': form.tweet.data,
            'date_posted': '7/17/2019'
            }
        )

        return redirect(url_for('profile'))
    return render_template('profile.html', form=form, posts=posts, title='Profile' )
