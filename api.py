from flask import Blueprint, jsonify
from database import get_winners_by_country, get_random_winners

# Create Blueprint for API endpoints
api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/winners-by-country', methods=['GET'])
def winners_by_country():
    """API endpoint to get Nobel Prize winners grouped by country"""
    data = get_winners_by_country()
    return jsonify(data)

@api_bp.route('/random-winners', methods=['GET'])
def random_winners():
    """API endpoint to get random Nobel Prize winners"""
    winners = get_random_winners(5)
    return jsonify(winners)
