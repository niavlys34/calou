import json
import os
from datetime import datetime
from pathlib import Path
from flask import Blueprint, render_template

bp = Blueprint("meteo", __name__)

METEO_JSON_PATH = os.environ.get(
    "METEO_JSON_PATH",
    Path(__file__).parent.parent / "debug" / "meteo.json",
)

@bp.route("/")
def index():
    with open(METEO_JSON_PATH, encoding="utf-8") as f:
        data = json.load(f)

    updated_at = data.pop("updated_at")

    modules = []
    for name, infos in data.items():
        modules.append({
            "name": name,
            "temp": infos["temp"],
            "min_temp": infos["min_temp"],
            "min_temp_time": datetime.fromtimestamp(infos["date_min_temp"]).strftime("%Hh%M"),
            "max_temp": infos["max_temp"],
            "max_temp_time": datetime.fromtimestamp(infos["date_max_temp"]).strftime("%Hh%M"),
            "reachable": infos["reachable"],
            })

    return render_template(
        "meteo.html",
        modules=modules,
        updated_at=datetime.fromtimestamp(updated_at).strftime("%d/%m/%Y à %Hh%M"),
    )
