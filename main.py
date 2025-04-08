from flask import Flask, request, Response
import os,json

app = Flask(__name__)


@app.route("/")
def hello_world(): 
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    if ip and "," in ip:
        ip = ip.split(",")[0].strip()

    body = {
        "User-Agent": request.headers.get("User-Agent"),
        "remote_ip": ip,
        "Content-Type": request.headers.get("Content-Type"),
        "Body": "Hola mundo"
    }
    payload = json.dumps(body, ensure_ascii=False)
    return Response(
        response=payload,
        status=200,
        mimetype="application/json"
    )
    
@app.route("/health")
def health():
    return Response(
        status=200,
        mimetype="application/text"
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))