from flask import Flask, jsonify
from flask_cors import CORS

from config import Config
from traffic_simulator import TrafficSimulator

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/api/*": {"origins": "*"}})

simulator = TrafficSimulator(
    capacity_mbps=Config.NETWORK_CAPACITY_MBPS,
    seed=Config.SIMULATION_SEED,
)


@app.get("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "VirtuNet backend",
        "stage": "stage-1-and-stage-2",
    })


@app.get("/api/traffic")
def traffic():
    return jsonify(simulator.generate_record("normal"))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=Config.PORT,
        debug=Config.DEBUG,
    )
