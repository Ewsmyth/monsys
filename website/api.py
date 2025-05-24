from flask import Blueprint, request, jsonify
import psutil
import platform
import datetime

api = Blueprint('api', __name__)

def get_system_metrics():
    metrics = {
        "timestamp": datetime.datetime.now().isoformat(),
        "hostname": platform.node(),
        "os": platform.platform(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": {
            "total": psutil.virtual_memory().total,
            "used": psutil.virtual_memory().used,
            "percent": psutil.virtual_memory().percent
        },
        "disk": {
            "total": psutil.disk_usage('/').total,
            "used": psutil.disk_usage('/').used,
            "percent": psutil.disk_usage('/').percent
        },
        "load_average": psutil.getloadavg(),
        "temperatures": {}
    }

    temps = psutil.sensors_temperatures()
    for name, entries in temps.items():
        metrics["temperatures"][name] = [
            {"label": e.label or name, "temp": e.current} for e in entries
        ]

    return metrics

@api.route('/api/metrics', methods=['POST'])
def collect_metrics():
    metrics = get_system_metrics()

    # For now, just print the metrics to the console
    print("=== System Metrics ===")
    for key, value in metrics.items():
        print(f"{key}: {value}")

    # Respond to the POST request
    return jsonify({"status": "success", "metrics": metrics})
