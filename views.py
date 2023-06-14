from flask import Blueprint, render_template, request
import requests

views = Blueprint(__name__, "views")

@views.route("/", methods=["GET", "POST"])
def home():
    data_dict = None
    # if Convert Button is clicked
    if request.method == "POST":
        date = request.form.get("date_input")
        # check if the date is valid
        if date:
            url = f"https://www.hebcal.com/converter?cfg=json&date={date}&g2h=1&strict=1"
            response = requests.get(url)
            # check if we have a success response
            if response.status_code == 200:
                data = response.json()
                data_dict = {"gregorian_date": date, "heb_date": data["hebrew"], "heb_year": data["heDateParts"]["y"],
                             "heb_month": data["heDateParts"]["m"], "heb_day": data["heDateParts"]["d"]}
            else:
                response.raise_for_status()
    return render_template("index.html", data_dict=data_dict)
