from flask import Blueprint, render_template as render, redirect, url_for
from flask_login import current_user, login_required, logout_user

main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/', methods=['GET'])
@login_required
def dashboard():
    return render(
        'dashboard.jinja2',
        title='Dashboard',
        template='dashboard-template',
        current_user=current_user,
        body = 'Logged in'
    )


@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))

    