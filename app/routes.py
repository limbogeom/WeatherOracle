from flask import Blueprint, request, jsonify, render_template
from .extensions import db
from .models import Weather
from datetime import datetime

weather_bp = Blueprint("weather", __name__, url_prefix="/api/weather")

@weather_bp.post("")
def create_weather_stamp():
    data = request.get_json()
    
    weather = Weather(
        temperature=data["temperature"],
        humidity=data["humidity"],
        light=data["light"],
        stored_at=datetime.fromisoformat(data["stored_at"])
    )
    
    db.session.add(weather)
    db.session.commit()
    
    return jsonify({
        "message": "success"
    }), 201
    
@weather_bp.get("/frontend")
def frontend():
    return render_template("index.html")
    
@weather_bp.get("/backend")
def return_stamps():
    q = db.session.query(Weather)
    
    temp_gt = request.args.get("temp_gt", type=float)
    temp_lt = request.args.get("temp_lt", type=float)
    hum_gt = request.args.get("hum_gt", type=float)
    hum_lt = request.args.get("hum_lt", type=float)
    lux_gt = request.args.get("lux_gt", type=float)
    lux_lt = request.args.get("lux_lt", type=float)
    method = request.args.get("method", type=str)
    from_dt = request.args.get("from")
    to_dt = request.args.get("to")
    
    if temp_gt is not None:
        q = q.filter(Weather.temperature > temp_gt)
    if temp_lt is not None:
        q = q.filter(Weather.temperature < temp_lt)
    if hum_gt is not None:
        q = q.filter(Weather.humidity > hum_gt)
    if hum_lt is not None:
        q = q.filter(Weather.humidity < hum_lt)
    if lux_gt is not None:
        q = q.filter(Weather.light["lux"].as_float() > lux_gt)
    if lux_lt is not None:
        q = q.filter(Weather.light["lux"].as_float() < lux_lt)
    if method:
        q = q.filter(Weather.light["method"].as_text() == method)
    if from_dt:
        q = q.filter(Weather.stored_at >= from_dt)
    if to_dt:
        q = q.filter(Weather.stored_at <= to_dt)
        
    q = q.order_by(Weather.stored_at.desc())
    limit = min(request.args.get("limit", default=100, type=int), 1000)
    results = q.limit(limit).all()
    
    return jsonify([{
        "id": w.id,
        "temperature": w.temperature,
        "humidity": w.humidity,
        "light": w.light,
        "created_at": w.created_at.isoformat(),
        "stored_at": w.stored_at.isoformat()
    }
    for w in results
    ])
    
@weather_bp.get("/<int:stamp_id>")
def get_stamp(stamp_id):
    stamp = Weather.query.get_or_404(stamp_id)
    
    return jsonify({
        "id": stamp.id,
        "temperature": stamp.temperature,
        "humidity": stamp.humidity,
        "light": stamp.light,
        "created_at": stamp.created_at.isoformat(),
        "stored_at": stamp.stored_at.isoformat()
    })
    
@weather_bp.delete("/<int:stamp_id>")
def delete_stamp(stamp_id):
    stamp = Weather.query.get_or_404(stamp_id)
    
    db.session.delete(stamp)
    db.session.commit()
    
    return jsonify({
        "message": "deleted"
    })