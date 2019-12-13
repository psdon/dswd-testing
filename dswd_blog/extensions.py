from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from passlib.context import CryptContext
from flask_mail import Mail


csrf_protect = CSRFProtect()
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate(compare_type=True)
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
mail = Mail()
