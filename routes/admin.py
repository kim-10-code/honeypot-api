from flask import Blueprint, jsonify, send_file
from models import Attack, db
import csv
import io

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def dashboard():
    attacks = Attack.query.order_by(Attack.timestamp.desc()).limit(100).all()
    return jsonify({"attacks": [a.to_dict() for a in attacks]})


@admin_bp.route('/admin/export/csv')
def export_csv():
    attacks = Attack.query.all()
    output = io.StringIO()
    writer = csv.DictWriter(
        output,
        fieldnames=['id', 'ip', 'user_agent', 'payload', 'geolocation', 'timestamp']
    )
    writer.writeheader()
    for a in attacks:
        writer.writerow(a.to_dict())
    output.seek(0)
    return send_file(
        output,
        mimetype='text/csv',
        as_attachment=True,
        download_name='honeypot_logs.csv'
    )