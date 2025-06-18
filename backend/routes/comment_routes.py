from flask import Blueprint, jsonify, request
from backend.models.database_models import Comment, Variety
from backend.extensions import db
from datetime import datetime

comment_bp = Blueprint('comment_bp', __name__)

@comment_bp.route('/variety/<int:variety_id>', methods=['POST'])
def add_comment(variety_id):
    data = request.get_json()
    if not data or not data.get('user_name') or not data.get('comment_text'):
        return jsonify({'message': 'Missing user_name or comment_text in request body'}), 400

    # Check if the variety exists
    variety = Variety.query.get(variety_id)
    if not variety:
        return jsonify({'message': f'Variety with id {variety_id} not found'}), 404

    try:
        new_comment = Comment(
            user_name=data['user_name'],
            comment_text=data['comment_text'],
            variety_id=variety_id
            # created_at is handled by default in the model
        )
        db.session.add(new_comment)
        db.session.commit()
        return jsonify({
            'id': new_comment.id,
            'user_name': new_comment.user_name,
            'comment_text': new_comment.comment_text,
            'created_at': new_comment.created_at.isoformat() + 'Z', # ISO 8601 format with Z for UTC
            'variety_id': new_comment.variety_id
        }), 201
    except Exception as e:
        db.session.rollback()
        print(f"Error adding comment for variety {variety_id}: {e}") # Log error
        return jsonify({'error': 'Failed to add comment. Please try again later.'}), 500

@comment_bp.route('/variety/<int:variety_id>', methods=['GET'])
def get_comments(variety_id):
    try:
        # Check if the variety exists
        variety = Variety.query.get(variety_id)
        if not variety:
            return jsonify({'message': f'Variety with id {variety_id} not found'}), 404

        comments = Comment.query.filter_by(variety_id=variety_id).order_by(Comment.created_at.desc()).all()
        return jsonify([{
            'id': c.id,
            'user_name': c.user_name,
            'comment_text': c.comment_text,
            'created_at': c.created_at.isoformat() + 'Z', # ISO 8601 format with Z for UTC
            'variety_id': c.variety_id
        } for c in comments])
    except Exception as e:
        print(f"Error fetching comments for variety {variety_id}: {e}") # Log error
        return jsonify({'error': 'Failed to fetch comments. Please try again later.'}), 500
