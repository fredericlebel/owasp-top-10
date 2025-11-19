import os
from flask import Flask, send_file

app = Flask(__name__)

FILES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files")


@app.route("/download/<path:filename>")
def download(filename):
    app.logger.info(f"[REQUEST] User requested: {filename}")

    # Vulnérabilité CWE-22 : aucune canonicalisation du chemin d'accès
    file_path = os.path.join(FILES_DIR, filename)

    app.logger.info(f"[FILEPATH] Resolved path: {file_path}")

    return send_file(file_path)


if __name__ == "__main__":
    app.logger.setLevel("INFO")
    app.logger.info("URLs exploitables :")
    app.logger.info("  1) curl http://127.0.0.1:5000/download/.env")
    app.logger.info("  2) curl http://127.0.0.1:5000/download/%2e%2e/.env")
    app.logger.info(
        "  3) curl http://127.0.0.1:5000/download/%2e%2e/%2e%2e/%2e%2e/owasp-top-10-2025-labs.code-workspace"
    )
    app.logger.info("")
    app.logger.info("Serveur vulnérable démarré ➜ http://127.0.0.1:5000/")

    app.run(debug=True)
