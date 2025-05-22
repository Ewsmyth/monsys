from flask import Blueprint, request

api = Blueprint('api', __name__)

@api.route('/api/metrics', methods=['POST'])
def collect_metrics():
    data = request.get_json()
    # Validate & save data to DB
