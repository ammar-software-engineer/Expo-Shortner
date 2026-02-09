from flask import render_template, request, redirect, url_for, flash
from . import db
from .models import URL
from flask import current_app as app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form.get('original_url')
        if not original_url:
            flash('Please enter a URL')
            return redirect(url_for('index'))

        existing_url = URL.query.filter_by(original_url=original_url).first()
        if existing_url:
            return render_template('shortened.html', short_url=f'{request.host_url}{existing_url.short_code}')

        new_url = URL(original_url=original_url)
        db.session.add(new_url)
        db.session.commit()
        return render_template('shortened.html', short_url=f'{request.host_url}{new_url.short_code}')

    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_original_url(short_code):
    url = URL.query.filter_by(short_code=short_code).first_or_404()
    return redirect(url.original_url)
