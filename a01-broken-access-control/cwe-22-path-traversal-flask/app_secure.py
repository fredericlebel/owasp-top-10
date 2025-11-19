import os
from flask import Flask, send_file


def create_app(files_dir=None):

    app = Flask(__name__)

    if files_dir is None:
        files_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files")

    app.config["FILES_DIR"] = files_dir

    @app.route("/download/<path:filename>")
    def download(filename):
        base = app.config["FILES_DIR"]
        requested = os.path.join(base, filename)

        # Canonicalisation du chemin d'accès pour prévenir les attaques de type path traversal
        requested_realpath = os.path.realpath(requested)

        if not requested_realpath.startswith(base + os.sep):
            app.logger.warning(
                f"[SECURITY] Path traversal attempt detected: {filename} -> {requested_realpath}"
            )
            return "Access denied", 403

        file_path = requested_realpath

        if not os.path.isfile(file_path):
            app.logger.info(f"File not found: {file_path}")
            return "File not found", 404

        app.logger.info(f"[REQUEST] User requested: {filename}")
        app.logger.info(f"[FILEPATH] Resolved path: {file_path}")

        return send_file(file_path)

    return app


if __name__ == "__main__":
    app = create_app()

    app.logger.setLevel("INFO")
    app.logger.info("URLs exploitables :")
    app.logger.info("  1) curl http://127.0.0.1:5000/download/.env")
    app.logger.info("  2) curl http://127.0.0.1:5000/download/%2e%2e/.env")
    app.logger.info(
        "  3) curl http://127.0.0.1:5000/download/%2e%2e/%2e%2e/%2e%2e/owasp-top-10-2025-labs.code-workspace"
    )
    app.logger.info("")
    app.logger.info("Serveur sécurisé démarré ➜ http://127.0.0.1:5000/")

    app.run(debug=True)
