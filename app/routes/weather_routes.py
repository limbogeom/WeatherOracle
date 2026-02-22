from flask import Blueprint, request, jsonify, render_template
from ..services.weather_service import WeatherService
from ..observers.weather_observer import WeatherLogger
from ..schemas.weather_schema import WeatherSchema
from datetime import datetime

weather_bp = Blueprint("weather", __name__, url_prefix="/api/weather")
service = WeatherService()
service.subscribe(WeatherLogger())

schema = WeatherSchema()

@weather_bp.post("/backend")
def create_weather_stamp():
    try:
        data = schema.load(request.get_json())
    except Exception as err:
        return {"error": str(err)}, 400
    
    weather = service.create(
        temperature=data["temperature"],
        humidity=data["humidity"],
        light=data["light"],
        stored_at=data["stored_at"]
    )
    return jsonify({"message": "success", "id": weather.id}), 201
    
@weather_bp.get("/frontend")
def frontend():
    return render_template("index.html")
    
@weather_bp.get("/backend")
def return_stamps():
    filters = {k: request.args.get(k) for k in request.args.keys()}
    limit = request.args.get("limit", default=100, type=int)
    results = service.get_all(filters=filters, limit=limit)
    return jsonify([w.to_dict() for w in results])
    
@weather_bp.get("/backend/<int:stamp_id>")
def get_stamp(stamp_id):
    stamp = service.get(stamp_id)
    
    return jsonify({
        "id": stamp.id,
        "temperature": stamp.temperature,
        "humidity": stamp.humidity,
        "light": stamp.light,
        "created_at": stamp.created_at.isoformat(),
        "stored_at": stamp.stored_at.isoformat()
    })
    
@weather_bp.delete("/backend/<int:stamp_id>")
def delete_stamp(stamp_id):
    service.delete(stamp_id)
    
    return jsonify({
        "message": "deleted"
    })
    
@weather_bp.delete("/backend")
def delete_all():
    service.delete_all()
    
    return jsonify({"message": "all deleted"})