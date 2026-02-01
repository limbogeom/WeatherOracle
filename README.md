### POST /api/weather
curl -X POST https://<your-url>/api/weather \
-H "Content-Type: application/json" \
-d '{
  "temperature": 23.5,
  "humidity": 45.2,
  "light": {"absolute": 1024,"lux":3.5,"method":"LDR_GL55xx_generic"},
  "stored_at": "2026-02-01T22:14:05"
}'

### GET /api/weather/backend
curl https://<your-url>/api/weather/backend
