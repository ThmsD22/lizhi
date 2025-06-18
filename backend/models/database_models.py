from backend.extensions import db
from datetime import datetime

class Variety(db.Model):
    __tablename__ = 'varieties'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    video_url = db.Column(db.String(255))

    # Relationships
    production_areas = db.relationship('ProductionArea', backref='variety', lazy=True)
    comments = db.relationship('Comment', backref='variety', lazy=True)
    likes = db.relationship('Like', backref='variety', lazy=True)

    def __repr__(self):
        return f'<Variety {self.name}>'

class ProductionArea(db.Model):
    __tablename__ = 'production_areas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Numeric(10, 8), nullable=False)
    longitude = db.Column(db.Numeric(11, 8), nullable=False)
    variety_id = db.Column(db.Integer, db.ForeignKey('varieties.id'))

    # Relationships
    farmers = db.relationship('Farmer', backref='production_area', lazy=True)

    def __repr__(self):
        return f'<ProductionArea {self.name}>'

class Farmer(db.Model):
    __tablename__ = 'farmers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    brand_name = db.Column(db.String(255))
    contact_info = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    area_id = db.Column(db.Integer, db.ForeignKey('production_areas.id'))

    def __repr__(self):
        return f'<Farmer {self.name}>'

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), nullable=False)
    comment_text = db.Column(db.Text, nullable=False)
    variety_id = db.Column(db.Integer, db.ForeignKey('varieties.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<Comment {self.user_name} on Variety {self.variety_id}>'

class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    variety_id = db.Column(db.Integer, db.ForeignKey('varieties.id'), nullable=False)
    user_identifier = db.Column(db.String(255), nullable=False)

    __table_args__ = (db.UniqueConstraint('variety_id', 'user_identifier', name='uq_variety_user_identifier'),)

    def __repr__(self):
        return f'<Like by {self.user_identifier} on Variety {self.variety_id}>'
