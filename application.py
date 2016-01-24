from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

@app.route("/application-form")
def show_application():
    """Show an application form."""

    return render_template("application-form.html")

@app.route("/application", methods=["POST", "GET"])
def submit_application():
    """Show a submitted application page."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    position = request.form.get("position")
    salary = request.form.get("salary")


    return render_template("application-response.html",
                            first_name = first_name,
                            last_name = last_name,
                            position = position,
                            salary = salary
                            )


if __name__ == "__main__":
    app.run(debug=True)
