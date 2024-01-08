# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 18:20:27 2024

@author: James
"""

from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for, make_response, jsonify)
from os import listdir

bp = Blueprint('pages', __name__, url_prefix='/')

@bp.route("sharkfiles")
def sharkfiles_landing():
    cards_path = "/home/jdawson/repos/sharkweb/static/cards/"
    shark_cards = ["cards/"+f for f in listdir(cards_path)]
    shark_card_urls = [url_for("static", filename=i) for i in shark_cards]
    shark_cards_dict = {v: k for v, k in enumerate(shark_card_urls)}
    return render_template('sharkfiles.html', contents=shark_cards_dict)

@bp.route("map")
def map_landing():
    return render_template('map.html')


