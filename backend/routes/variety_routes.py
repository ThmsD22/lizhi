from flask import Blueprint, jsonify, request
from backend.models.database_models import Variety
from backend.extensions import db

variety_bp = Blueprint('variety_bp', __name__)

@variety_bp.route('', methods=['GET'])
def get_varieties():
    try:
        varieties = Variety.query.all()
        return jsonify([{
            'id': var.id,
            'name': var.name,
            'description': var.description,
            'image_url': var.image_url,
            'video_url': var.video_url
        } for var in varieties])
    except Exception as e:
        # Log the exception e for debugging purposes
        print(f"Error fetching varieties: {e}")
        return jsonify({'error': 'Failed to fetch varieties. Please try again later.'}), 500

@variety_bp.route('/<int:id>', methods=['GET'])
def get_variety(id):
    try:
        variety = Variety.query.get(id)
        if variety:
            return jsonify({
                'id': variety.id,
                'name': variety.name,
                'description': variety.description,
                'image_url': variety.image_url,
                'video_url': variety.video_url
            })
        else:
            return jsonify({'message': 'Variety not found'}), 404
    except Exception as e:
        # Log the exception e for debugging purposes
        print(f"Error fetching variety with id {id}: {e}")
        return jsonify({'error': f'Failed to fetch variety with id {id}. Please try again later.'}), 500

# Future: Implement POST to create a new variety
# @variety_bp.route('', methods=['POST'])
# def create_variety():
#     data = request.get_json()
#     # Add validation and error handling
#     try:
#         new_variety = Variety(
#             name=data['name'],
#             description=data.get('description'),
#             image_url=data.get('image_url'),
#             video_url=data.get('video_url')
#         )
#         db.session.add(new_variety)
#         db.session.commit()
#         return jsonify({'id': new_variety.id, 'name': new_variety.name}), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500

# Future: Implement PUT to update a variety
# @variety_bp.route('/<int:id>', methods=['PUT'])
# def update_variety(id):
#     data = request.get_json()
#     variety = Variety.query.get(id)
#     if not variety:
#         return jsonify({'message': 'Variety not found'}), 404
#     try:
#         variety.name = data.get('name', variety.name)
#         variety.description = data.get('description', variety.description)
#         variety.image_url = data.get('image_url', variety.image_url)
#         variety.video_url = data.get('video_url', variety.video_url)
#         db.session.commit()
#         return jsonify({'message': 'Variety updated successfully'})
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500

# Future: Implement DELETE to remove a variety
# @variety_bp.route('/<int:id>', methods=['DELETE'])
# def delete_variety(id):
#     variety = Variety.query.get(id)
#     if not variety:
#         return jsonify({'message': 'Variety not found'}), 404
#     try:
#         # Add logic to handle related entities if necessary (e.g., comments, likes)
#         # For example, if there's a cascading delete or if they should be disassociated.
#         # Depending on your schema, SQLAlchemy might handle some of this automatically
#         # if `ondelete="CASCADE"` is set in your model relationships.
#         # If not, you might need to delete related ProductionArea, Comment, Like objects manually
#         # or set their foreign keys to null if the schema allows.
#         # Example:
#         # Comment.query.filter_by(variety_id=id).delete()
#         # Like.query.filter_by(variety_id=id).delete()
#         # ProductionArea.query.filter_by(variety_id=id).update({"variety_id": None}) # Or delete

#         db.session.delete(variety)
#         db.session.commit()
#         return jsonify({'message': 'Variety deleted successfully'})
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500
