from flask import Blueprint, render_template

blog_blueprint = Blueprint('blog', __name__, template_folder='templates')


@blog_blueprint.route('/blogs/')
def blogs():
    return render_template('blogs.html')


@blog_blueprint.route('/blogs/<string:id>')
def blog(id):
    return render_template('blog.html', id=id)


