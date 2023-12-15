from . import app, db
from .models import Passport, Marriage
from .utils import as_dict

from flask import request, abort, jsonify, Response
from sqlalchemy.exc import IntegrityError
from random import randint
from typing import Tuple
from datetime import datetime


# TODO: change abort(400) to useful information
# TODO: response json

@app.route('/api/v1/passport', methods=['POST'])
def post_passport() -> Response:
    """
    A function that create new passport in DB
    :param: json:
           nickname: "str(64)"
           discord_tag: "str(128)"
    :return: A Response(JSON) with unique 8-digit number of new passport ("mm rnd:06")
    """
    nickname: str = ''
    discord_tag: str = ''

    if not request.json:
        abort(400)

    month_now_str: str = datetime.now().strftime('%m')

    # generate uuid
    passport_id = randint(0, 999999)
    while db.session.query(Passport).\
            filter(Passport.rp_number == month_now_str
                   + f'{passport_id:06d}').\
            limit(1).first() is not None:

        passport_id = randint(0, 999999)

    try:
        nickname = request.json['nickname']
        discord_tag = request.json['discord_tag']
    except KeyError:
        abort(400)

    rp_number = month_now_str + f'{passport_id:06d}'
    issue_date: datetime = datetime.now()

    passport = Passport(nickname=nickname,
                        discord_tag=discord_tag,
                        rp_number=rp_number,
                        issue_date=issue_date)

    db.session.add(passport)
    db.session.commit()

    return jsonify(rp_number=rp_number)


@app.route('/api/v1/passport/by_number/<string:rp_number>', methods=['GET'])
def get_passport_by_number(rp_number: str) -> Response:
    passport: Passport = db.session.query(Passport).\
        filter_by(rp_number=rp_number).\
        limit(1).first()

    if passport is None:
        abort(400)

    return jsonify(as_dict(passport))


@app.route('/api/v1/passport/by_nickname/<string:nickname>', methods=['GET'])
def get_passport_by_nickname(nickname: str) -> Response:
    passports: list[Passport] = db.session.query(Passport).\
        filter_by(nickname=nickname).order_by(Passport.issue_date).all()

    return jsonify(list(map(as_dict, passports)))
