from marshmallow import Schema, fields, validates, ValidationError

class WeatherSchema(Schema):
    temperature = fields.Float(required=True)
    humidity = fields.Float(required=True)
    light = fields.Dict(required=True)
    stored_at = fields.DateTime(required=True)
    
    @validates("temperature")
    def validate_temperature(self, value, **kwargs):
        if not (-100 <= value <= 100):
            raise ValidationError("Temperature must be between -100 and 100")
        
    @validates("humidity")
    def validate_humidity(self, value, **kwargs):
        if not (0 <= value <= 100):
            raise ValidationError("Humidity must be between 0 and 100")