from flask import Blueprint, jsonify
import os
from dotenv import load_dotenv
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from flask_jwt_extended import get_jwt_identity, jwt_required
from api.models import Appointments

load_dotenv()
twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
twilio_api_key_sid = os.environ.get('TWILIO_API_KEY_SID')
twilio_api_key_secret = os.environ.get('TWILIO_API_KEY_SECRET')


video_bp = Blueprint('video_bp', __name__)

@video_bp.route('/generateAccessToken/<int:id>', methods=['POST', 'GET'], strict_slashes=False)
@jwt_required()
def generateAddVideoToken(id):
    """
    Create a token for joining video call

    Args:
        None - Nothing because the token will be verified by jwt required

    Return:
        string - token for joining the video call
    """
    # Take appointment id and create a room with it
    # Create a token with the room
    # return the room and token as json file

    appt = Appointments.query.get(id)
    
    # room_name = 'room_'.join(appt.id)
    if not appt:
        return jsonify({'status': 'room not found'}), 200
    
    # Add room id to appointments
    room_name = appt.room

    # Generate token
    token = AccessToken(twilio_account_sid, twilio_api_key_sid,
            twilio_api_key_secret, identity=get_jwt_identity().id)

    token.add_grant(VideoGrant(room=room_name))

    return jsonify({
        'token': token.to_jwt().decode(), 
        'room': room_number
        }), 200
