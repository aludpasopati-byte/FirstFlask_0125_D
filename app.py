from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    submitted_name = None

    if request.method == "POST":
        # Mengambil nilai input berdasarkan atribut name="nama_pengguna"
        submitted_name = request.form.get("nama_pengguna", "").strip()

    return render_template("index.html", submitted_name=submitted_name)


if __name__ == "__main__":
    app.run(debug=True)