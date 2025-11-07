from flask import Blueprint, request, jsonify
from utils.logger import log_attack
from models import db

login_bp = Blueprint('login', __name__)

DUMMY_JWT = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ."
    "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5Q"
)

@login_bp.route('/api/v1/login', methods=['POST'])
def fake_login():
    payload = request.get_json(silent=True) or {}
    log_attack(request, db, payload)
    return jsonify({"message": "Login successful", "token": DUMMY_JWT}), 200