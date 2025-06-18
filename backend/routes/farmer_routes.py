from flask import Blueprint, jsonify
from backend.models.database_models import Farmer
from backend.extensions import db

farmer_bp = Blueprint('farmer_bp', __name__)

@farmer_bp.route('', methods=['GET'])
def get_farmers():
    try:
        farmers = Farmer.query.all()
        return jsonify([{
            'id': farmer.id,
            'name': farmer.name,
            'brand_name': farmer.brand_name,
            'contact_info': farmer.contact_info,
            'image_url': farmer.image_url,
            'area_id': farmer.area_id,
            'area_name': farmer.production_area.name if farmer.production_area else None, # Include area name
            'variety_id': farmer.production_area.variety.id if farmer.production_area and farmer.production_area.variety else None, # Include variety id
            'variety_name': farmer.production_area.variety.name if farmer.production_area and farmer.production_area.variety else None # Include variety name
        } for farmer in farmers])
    except Exception as e:
        print(f"Error fetching farmers: {e}") # Log error
        return jsonify({'error': 'Failed to fetch farmers.'}), 500

@farmer_bp.route('/area/<int:area_id>', methods=['GET'])
def get_farmers_by_area(area_id):
    try:
        farmers = Farmer.query.filter_by(area_id=area_id).all()
        if not farmers:
            return jsonify({'message': 'No farmers found for this area'}), 404
        return jsonify([{
            'id': farmer.id,
            'name': farmer.name,
            'brand_name': farmer.brand_name,
            'contact_info': farmer.contact_info,
            'image_url': farmer.image_url,
            'area_id': farmer.area_id,
            'area_name': farmer.production_area.name if farmer.production_area else None,
            'variety_id': farmer.production_area.variety.id if farmer.production_area and farmer.production_area.variety else None,
            'variety_name': farmer.production_area.variety.name if farmer.production_area and farmer.production_area.variety else None
        } for farmer in farmers])
    except Exception as e:
        print(f"Error fetching farmers for area {area_id}: {e}") # Log error
        return jsonify({'error': 'Failed to fetch farmers for this area.'}), 500

# Consider adding POST, PUT, DELETE for farmers if admin functionality is needed.
# Example POST:
# @farmer_bp.route('', methods=['POST'])
# def create_farmer():
#     data = request.get_json()
#     if not data or not data.get('name'):
#         return jsonify({'error': 'Missing required field: name'}), 400
#     try:
#         new_farmer = Farmer(
#             name=data['name'],
#             brand_name=data.get('brand_name'),
#             contact_info=data.get('contact_info'),
#             image_url=data.get('image_url'),
#             area_id=data.get('area_id') # Ensure area_id exists
#         )
#         db.session.add(new_farmer)
#         db.session.commit()
#         return jsonify({'id': new_farmer.id, 'name': new_farmer.name}), 201
#     except Exception as e:
#         db.session.rollback()
#         print(f"Error creating farmer: {e}") # Log error
#         return jsonify({'error': str(e)}), 500
