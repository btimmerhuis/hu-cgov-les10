from flask import render_template, request, current_app, url_for, redirect

from project import db
from project.models import todo_item

from . import cgov_blueprint


# ------
# Routes
# ------
@cgov_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        todo = todo_item(request.form['action'])
        db.session.add(todo)
        db.session.commit()

    todo_items = todo_item.query.all()
    current_app.logger.info(todo_items)

    return render_template('cgov/index.html', TODO_ITEMS=todo_items)


@cgov_blueprint.route('/delete/<id>', methods=['GET'])
def delete(id):
    print(todo_item.query.filter_by(id=id).all())
    todo_item.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('cgov.index'))
