from . import app, db
from .models import Passport, Marriage

from flask import request, abort
from sqlalchemy.exc import IntegrityError
from random import randint
from typing import Tuple
from datetime import datetime


# TODO: change abort(400) to useful information

@app.route('/api/v1/passport', methods=['POST'])
def post_passport() -> str:
    """
    A function that create new passport in DB
    :param: json:
           nickname: "str(64)"
           discord_tag: "str(128)"
    :return: A str with unique 8-digit number of new passport ("mm rnd:06")
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
        nickname: str = request.json['nickname']
        discord_tag: str = request.json['discord_tag']
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

    return rp_number
