from app import db

class User (db.Model):
    """Data model for user accounts."""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    firstname = db.Column(db.String(10), nullable=False)
    lastname = db.Column(db.String(10), nullable=False)
    username = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)

    """Adding users"""

    def add_users(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<User {}>'.format(self.username)
