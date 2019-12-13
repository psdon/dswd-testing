from flask_mail import Message
from flask import current_app
from dswd_blog.extensions import mail

def run():
    template = """
    This an email
    """

    msg = Message(
            subject="New Email",
            recipients=['dswd.testing@gmail.com'],
            html=template,
            sender=current_app.config["MAIL_DEFAULT_SENDER"],
    )

    mail.send(msg)


# from scripts.send_mail import run
# run()