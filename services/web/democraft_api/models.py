from . import db
from sqlalchemy.orm import relationship


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer(), primary_key = True)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)


class Passport(BaseModel):
    __tablename__ = 'passports'

    rp_number = db.Column(db.String(8), unique=True, nullable=False)
    nickname = db.Column(db.String(64), index=True, nullable=False)
    discord_tag = db.Column(db.String(128), nullable=False)
    issue_date = db.Column(db.DateTime(), nullable=False)


class Marriage(BaseModel):
    __tablename__ = 'mariages'

    first_partner_id = db.Column(db.Integer, db.ForeignKey('passports.id'), nullable=False)
    second_partner_id = db.Column(db.Integer, db.ForeignKey('passports.id'), nullable=False)
    mariage_date = db.Column(db.DateTime(), nullable=False)
    divorce_date = db.Column(db.DateTime())
