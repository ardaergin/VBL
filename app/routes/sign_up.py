from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.utils import NAVIGATION
from app.utils import register_user

bp = Blueprint('sign_up', __name__)

@bp.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        user_id = request.form['vu_id']
        email = request.form['email']
        if "@student.vu.nl" not in email and "@vu.nl" not in email:
            flash('Email must be a VU email (@vu.nl or @student.vu.nl)', 'danger')
            return redirect(url_for('sign_up.sign_up'))

        # Call the registration function directly
        try:
            register_user(first_name, last_name, user_id, email)
            return redirect(url_for('sign_up.sign_up_result', success=True))
        except Exception as e:
            error_message = str(e)
            if "User ID you have entered is already in use" in error_message:
                flash('It seems that you are already registered in VBL SONA. If you think this is a mistake, please contact vbl@vu.nl.', 'danger')
            else:
                flash(f'An error occurred: {error_message}', 'danger')
            return redirect(url_for('sign_up.sign_up'))

    return render_template(
        'sign_up.html',
        title='Sign Up',
        navigation=NAVIGATION,
        breadcrumb_path=[{"name": "home", "display": "Home"}, {"name": "sign_up", "display": "Sign Up"}])

@bp.route('/sign-up-result')
def sign_up_result():
    success = request.args.get('success', 'false').lower() == 'true'
    error_message = request.args.get('error_message', "")
    return render_template('sign_up_results.html', title='Registration Results', navigation=NAVIGATION, success=success, error_message=error_message)
