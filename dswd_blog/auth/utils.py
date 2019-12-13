import threading

from flask import (
    copy_current_request_context,
    current_app, url_for, render_template
)
from flask_mail import Message

from ..extensions import mail
from .tokens import generate_email_token


def create_email_message(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=current_app.config["MAIL_DEFAULT_SENDER"],
    )
    return msg


def send_async_email(to, subject, template):
    msg = create_email_message(to, subject, template)

    if not current_app.config.get("TESTING"):
        @copy_current_request_context
        def send_message(message):
            mail.send(message)

        sender = threading.Thread(name="mail_sender", target=send_message, args=(msg,))
        sender.start()
    else:
        with mail.record_messages() as outbox:
            mail.send(msg)
            return outbox


def send_recover_account_email(email):
    token = generate_email_token(email, expires_sec=600)

    reset_url = url_for("auth.reset_password", token=token, _external=True)

    template = render_template("auth/recover/email_template.html", reset_url=reset_url)

    return send_async_email(to=email, subject="Account Recovery", template=template)