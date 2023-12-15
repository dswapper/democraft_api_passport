from flask_sqlalchemy.extension import Model


def as_dict(model: Model):
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}