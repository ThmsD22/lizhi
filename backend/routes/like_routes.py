from flask import Blueprint, jsonify, request
from backend.models.database_models import Like, Variety
from backend.extensions import db

like_bp = Blueprint('like_bp', __name__)

@like_bp.route('/variety/<int:variety_id>', methods=['POST'])
def add_like(variety_id):
    data = request.get_json()
    if not data or not data.get('user_identifier'):
        return jsonify({'message': 'Missing user_identifier in request body'}), 400

    user_identifier = data['user_identifier']

    # Check if the variety exists
    variety = Variety.query.get(variety_id)
    if not variety:
        return jsonify({'message': f'Variety with id {variety_id} not found'}), 404

    try:
        # Check if this user has already liked this variety
        existing_like = Like.query.filter_by(variety_id=variety_id, user_identifier=user_identifier).first()
        if existing_like:
            # User has already liked, return current like status or a specific message
            # Returning 200 OK as the state is already achieved, or 409 Conflict if it's an issue.
            # For simplicity, let's return 200 with a message.
            return jsonify({
                'message': 'User has already liked this variety',
                'like_id': existing_like.id
            }), 200

        new_like = Like(
            variety_id=variety_id,
            user_identifier=user_identifier
        )
        db.session.add(new_like)
        db.session.commit()
        return jsonify({
            'message': 'Like added successfully',
            'like_id': new_like.id
        }), 201
    except Exception as e:
        db.session.rollback()
        print(f"Error adding like for variety {variety_id} by user {user_identifier}: {e}") # Log error
        return jsonify({'error': 'Failed to add like. Please try again later.'}), 500

@like_bp.route('/variety/<int:variety_id>', methods=['GET'])
def get_likes_summary(variety_id): # Renamed for clarity, can also get list of likers if needed
    try:
        # Check if the variety exists
        variety = Variety.query.get(variety_id)
        if not variety:
            return jsonify({'message': f'Variety with id {variety_id} not found'}), 404

        # Get the count of likes
        likes_count = Like.query.filter_by(variety_id=variety_id).count()

        # Optionally, get a list of user_identifiers who liked (if privacy allows and it's useful)
        # likers = [like.user_identifier for like in Like.query.filter_by(variety_id=variety_id).all()]

        return jsonify({
            'variety_id': variety_id,
            'variety_name': variety.name, # Added for context
            'likes_count': likes_count
            # 'users_who_liked': likers # If you decide to return this
        })
    except Exception as e:
        print(f"Error fetching likes for variety {variety_id}: {e}") # Log error
        return jsonify({'error': 'Failed to fetch likes information. Please try again later.'}), 500
