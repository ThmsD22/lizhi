from flask import Blueprint, jsonify
from backend.models.database_models import ProductionArea
from backend.extensions import db

production_area_bp = Blueprint('production_area_bp', __name__)

@production_area_bp.route('', methods=['GET'])
def get_production_areas():
    try:
        areas = ProductionArea.query.all()
        return jsonify([{
            'id': area.id,
            'name': area.name,
            'latitude': str(area.latitude), # Convert Decimal to string for JSON
            'longitude': str(area.longitude),
            'variety_id': area.variety_id,
            'variety_name': area.variety.name if area.variety else None # Include variety name
        } for area in areas])
    except Exception as e:
        print(f"Error fetching production areas: {e}") # Log error
        return jsonify({'error': 'Failed to fetch production areas.'}), 500

@production_area_bp.route('/variety/<int:variety_id>', methods=['GET'])
def get_production_areas_by_variety(variety_id):
    try:
        areas = ProductionArea.query.filter_by(variety_id=variety_id).all()
        if not areas:
            return jsonify({'message': 'No production areas found for this variety'}), 404
        return jsonify([{
            'id': area.id,
            'name': area.name,
            'latitude': str(area.latitude),
            'longitude': str(area.longitude),
            'variety_id': area.variety_id,
            'variety_name': area.variety.name if area.variety else None
        } for area in areas])
    except Exception as e:
        print(f"Error fetching production areas for variety {variety_id}: {e}") # Log error
        return jsonify({'error': 'Failed to fetch production areas for this variety.'}), 500

# Consider adding POST, PUT, DELETE for production areas if admin functionality is needed.
# Example POST:
# @production_area_bp.route('', methods=['POST'])
# def create_production_area():
#     data = request.get_json()
#     if not data or not data.get('name') or not data.get('latitude') or not data.get('longitude'):
#         return jsonify({'error': 'Missing required fields: name, latitude, longitude'}), 400
#     try:
#         new_area = ProductionArea(
#             name=data['name'],
#             latitude=data['latitude'], # Ensure validation for Decimal
#             longitude=data['longitude'], # Ensure validation for Decimal
#             variety_id=data.get('variety_id')
#         )
#         db.session.add(new_area)
#         db.session.commit()
#         return jsonify({'id': new_area.id, 'name': new_area.name}), 201
#     except Exception as e:
#         db.session.rollback()
#         print(f"Error creating production area: {e}") # Log error
#         return jsonify({'error': str(e)}), 500
