import requests
from user_agents import parse
import json

def extract_ip(request):
    return request.remote_addr

def parse_user_agent(request):
    user_agent_str = request.headers.get('User-Agent', 'Unknown')
    return str(parse(user_agent_str))

def get_geolocation(ip):
    try:
        r = requests.get(f'http://ip-api.com/json/{ip}', timeout=3)
        data = r.json()
        return f'{data.get('city', 'Unknown')}, {data.get('country', 'Unknown')}'
    except Exception:
        return 'Unknown'
    
def log_attack(request, db, payload):
    from models import Attack
    ip = extract_ip(request)
    user_agent = parse_user_agent(request)
    geo = get_geolocation(ip)

    attack = Attack(
        ip=ip,
        user_agent=user_agent,
        payload=json.dumps(payload),
        geolocation=geo
    )

    db.session.add(attack)
    db.session.commit()
    print(f"[+] Logged: {ip} - {geo} - {ua}")