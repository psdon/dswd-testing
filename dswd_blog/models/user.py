from ..extensions import db, pwd_context, login_manager
import datetime as dt
from sqlalchemy import UniqueConstraint


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.query.get(int(user_id))


login_manager.login_view = "auth.sign_in"
login_manager.login_message = "Please sign in to access this page"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    __table_args__ = (
        UniqueConstraint('username', name='unique_username'),
        UniqueConstraint('email', name='unique_email'),
    )

    blogs = db.relationship("Blog",
                            backref="author",
                            cascade="all, delete-orphan")

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = pwd_context.hash(self.password)

    def set_password(self, password):
        """Set password."""
        self.password = pwd_context.hash(password)

    def check_password(self, value):
        """Check password."""
        return pwd_context.verify(value, self.password)

    @property
    def is_active(self):
        return True if self.active else False

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
