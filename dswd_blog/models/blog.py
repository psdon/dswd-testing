from ..extensions import db
import datetime as dt


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer,
                          db.ForeignKey("user.id", ondelete='CASCADE'),
                          nullable=False)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __repr__(self):
        return f"<Blog '{self.title}'>"
