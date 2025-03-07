from rq_dashboard import RQDashboard
from flask import Flask

app = Flask(__name__)
app.config["RQ_DASHBOARD_REDIS_URL"] = "redis://<your-redis-url>:6379/0"
RQDashboard(app, url_prefix="/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
