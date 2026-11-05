import os
import glob
import hashlib
from flask import Flask, request, jsonify, send_file, send_from_directory
import yt_dlp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(BASE_DIR, "yt_cache")
os.makedirs(CACHE_DIR, exist_ok=True)

app = Flask(__name__, static_folder=BASE_DIR)

@app.after_request
def add_cors(resp):
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return resp

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/api/ping")
def ping():
    return jsonify({"ok": True})

@app.route("/api/youtube")
def youtube_audio():
    url = request.args.get("url", "").strip()
    if not url:
        return jsonify({"error": "Informe um link do YouTube."}), 400

    key = hashlib.md5(url.encode("utf-8")).hexdigest()[:12]
    out_tmpl = os.path.join(CACHE_DIR, f"{key}.%(ext)s")
    info_file = os.path.join(CACHE_DIR, f"{key}.title.txt")

    existing = [f for f in glob.glob(os.path.join(CACHE_DIR, f"{key}.*")) if not f.endswith(".txt") and not f.endswith(".part")]
    if existing and os.path.exists(info_file):
        with open(info_file, "r", encoding="utf-8") as fh:
            title = fh.read().strip()
        return jsonify({"audioUrl": f"/api/cache/{os.path.basename(existing[0])}", "title": title})

    ydl_opts = {
        "format": "bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio/best",
        "outtmpl": out_tmpl,
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get("title") or "Música do YouTube"
            with open(info_file, "w", encoding="utf-8") as fh:
                fh.write(title)
        files = [f for f in glob.glob(os.path.join(CACHE_DIR, f"{key}.*")) if not f.endswith(".txt") and not f.endswith(".part")]
        if not files:
            return jsonify({"error": "Falha ao salvar áudio do YouTube."}), 500
        return jsonify({"audioUrl": f"/api/cache/{os.path.basename(files[0])}", "title": title})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/cache/<path:filename>")
def serve_cache(filename):
    return send_from_directory(CACHE_DIR, filename)

if __name__ == "__main__":
    print("====================================================")
    print(" 🎸 RIFF RUSH - Servidor pronto em http://localhost:5000")
    print("====================================================")
    app.run(host="127.0.0.1", port=5000, debug=False)
