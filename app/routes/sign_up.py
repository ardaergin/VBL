from flask import Blueprint, render_template, request, redirect, url_for, flash
import csv
from app.utils import NAVIGATION

bp = Blueprint('sign_up', __name__)

@bp.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        if "@student.vu.nl" not in email:
            flash('Email must be a student email (@student.vu.nl)', 'danger')
            return redirect(url_for('sign_up'))

        with open('submissions.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([first_name, last_name, email])

        flash('You have successfully signed up!', 'success')
        return redirect(url_for('sign_up'))

    return render_template(
        'sign_up.html',
        title='Sign Up', 
        navigation=NAVIGATION, 
        breadcrumb_path=[{"name": "home", "display": "Home"}, {"name": "sign_up", "display": "Sign Up"}])
