from flask import Flask, render_template
from redis import Redis, RedisError

import os
import socket

redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    try:
        visites = redis.incr("compteur")
    except RedisError:
        visites = "Error connexion Redis"

    return render_template('index.html', nom=os.getenv("NOM", "Docker"), hostname=socket.gethostname(), visites=visites)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
