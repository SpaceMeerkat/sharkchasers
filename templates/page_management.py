# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 18:20:27 2024

@author: James
"""

from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for, make_response, jsonify)
from os import listdir

bp = Blueprint('pages', __name__, url_prefix='/')

@bp.route("about")
def about_landing():
    return render_template('about.html')

@bp.route("sharkfiles")
def sharkfiles_landing():
    cards_path = "/home/jdawson/repos/sharkweb/static/cards/"
    #shark_cards = ["cards/"+f for f in listdir(cards_path)]
    shark_cards = listdir(cards_path)
    print(shark_cards)
    #shark_card_names = [shark_cards[k].split("/")[1].split(".")[0] for k in range(len((shark_cards)))]
    shark_card_names = [shark_cards[k].split(".")[0] for k in range(len((shark_cards)))]
    #shark_card_urls = [url_for("static", filename=i) for i in shark_cards]
    shark_card_urls = shark_cards
    shark_card_status = ["unobserved"] * len(shark_card_names)
    
    shark_cards_dict = {"names":shark_card_names,
                        "urls":shark_card_urls,
                        "status":shark_card_status}
    
    return render_template('sharkfiles.html', contents=shark_cards_dict)

@bp.route("map")
def map_landing():
    return render_template('map.html')


