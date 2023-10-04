from flask import Blueprint, request
from services.nlp_service import cleansing, find_keywords
text_route = Blueprint('text_route', __name__)

@text_route.route('/v1/nlp/cleansing', methods=['POST'])
def text_cleansing():
    data = request.get_json()
    return cleansing(data)

@text_route.route('/v1/nlp/keywords', methods=['POST'])
def text_keywords():
    data = request.get_json()
    return find_keywords(data)