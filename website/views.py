from flask import Flask, render_template, request, Blueprint
from flask_login import login_required, current_user

view = Blueprint('view', __name__)


@view.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@view.route('/contact-us', methods=['GET'])
def contact():
    return render_template('contact.html', name=current_user.name)

@view.route('/thank-you', methods=['GET'])
def thank():
    return render_template('thankU.html', name=current_user.name)

@view.route('/404', methods=['GET'])
def error():
    return render_template('404.html', name=current_user.name)

@view.route('/team', methods=['GET'])
def team():
    return render_template('team.html', name=current_user.name)

@view.route('/profile')
@login_required
def profile():
    return "Kaam Chal Raha hai bhai thoda ruko"


@view.route('/blog', methods=['GET'])
def blog():
    return render_template('blog.html', name=current_user.name)


@view.route('/blog/Melanoma', methods=['GET'])
def blog_melanoma():
    return render_template('Melanoma.html', name=current_user.name)


@view.route('/blog/Dermatitis', methods=['GET'])
def blog_dermatitis():
    return render_template('Dermatitis.html', name=current_user.name)


@view.route('/blog/Eczema', methods=['GET'])
def blog_Eczema():
    return render_template('Eczema.html', name=current_user.name)


@view.route('/blog/Psoriasis', methods=['GET'])
def blog_Psoriasis():
    return render_template('Psoriasis.html', name=current_user.name)
