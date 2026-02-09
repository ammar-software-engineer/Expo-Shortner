from . import db
import string
import random

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, original_url):
        self.original_url = original_url
        self.short_code = self.generate_short_code()

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        while True:
            short_code = ''.join(random.choice(characters) for _ in range(6))
            if not URL.query.filter_by(short_code=short_code).first():
                return short_code

    def __repr__(self):
        return f'<URL {self.short_code}>'
