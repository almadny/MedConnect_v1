"""
This file contains routes to
1. Create, Edit, View and Delete Diagnosis
2. Display medical records
"""
from api import db
from api.models import Diagnosis
from flask import Blueprint

records_bp = Blueprint('records_bp', __name__)

@records_bp.route('/diagnosis/<int:id>', methods=['GET'])
def get_diagnosis(id):
    """
    Get a single diagnosis with the id provided
    """
    diag = Diagnosis.query.get(id)
    if not diag:
        return jsonify({'error': 'Not found'})
    return jsonify({'diagnosis' : diag})

@records_bp.route('/diagnosis/<patient_id>', methods=['GET'])
def patient_diagnosis(patient_id):
    """
    get all diagnosis for a particular patient
    """
    diag = Diagnosis.query.filter_by(patient_id=patient_id).all()
    if not diag:
        return jsonify({'error': 'No records found'})
    return jsonify({'all_diagnosis' : diag})
