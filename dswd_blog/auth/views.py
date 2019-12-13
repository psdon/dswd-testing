from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user
from .forms import SignInForm, SignUpForm, RecoverForm, ResetPasswordForm
from ..models import User
from ..extensions import db
from .utils import send_recover_account_email
from .tokens import verify_email_token

# Try :: url_prefix="/account"
bp = Blueprint("auth", __name__)


@bp.route("/sign-in/", methods=["GET", "POST"])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for("blog.home"))

    form = SignInForm()

    if form.validate_on_submit():
        user = form.username_or_email.data
        password = form.password.data
        user_obj = User.query.filter(
            (User.email == user) | (User.username == user)
        ).first()

        if user_obj and user_obj.check_password(password):
            login_user(user_obj)

        else:
            flash("Incorrect username or password", "warning")
            return render_template("auth/sign_in/index.html", form=form)

        # Be Careful, URL Redirect Vulnerability
        safe_redirect = None
        if request.args.get("next"):
            safe_redirect = f"{request.host_url}{request.args.get('next').strip('/')}"

        return redirect(safe_redirect or url_for("blog.home"))
    return render_template("auth/sign_in/index.html", form=form)


@bp.route("/sign-out/")
def sign_out():
    """Logout."""
    logout_user()
    flash("You have signed out successfully", category="success")
    return redirect(url_for("public.home"))


@bp.route("/sign-up/", methods=["GET", "POST"])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for("public.blog"))

    form = SignUpForm()

    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        db.session.add(new_user)
        try:
            db.session.commit()
            flash("You have signed up successfully. You can now sign-in", "success")
            return redirect(url_for("auth.sign_in"))
        except Exception:
            db.session.rollback()
            flash("Oops, an error occurred. Please try again later.", "warning")

    return render_template("auth/sign_up/index.html", form=form)


@bp.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):

    email = verify_email_token(token)
    if email is None:
        flash("The reset password link is invalid or has expired.", "warning")
        return redirect(url_for("auth.account_recover"))

    if current_user.is_authenticated:
        logout_user()

    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first()

        if user:
            user.set_password(form.password.data)
            try:
                db.session.commit()
                flash(
                    "You have successfully reset your password. You can now sign in.",
                    "success",
                )
                return redirect(url_for("auth.sign_in"))
            except Exception:
                flash("Oops, an error occurred. Please try again later.", "warning")
        else:
            flash("Oops, an error occurred. Please try again later.", "warning")

    return render_template("auth/recover/reset_password.html", form=form)


@bp.route("/recover/", methods=["GET", "POST"])
def account_recover():
    if current_user.is_authenticated:
        return redirect(url_for("blog.home"))

    form = RecoverForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_recover_account_email(email=user.email)
        flash("We have sent you an email. Please check your email inbox.", "success")

    return render_template("auth/recover/find_account.html", form=form)
