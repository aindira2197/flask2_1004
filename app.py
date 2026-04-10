from flask import Flask, render_template

app = Flask(__name__)

@app.route('/soz/<matn>/tahlil')
def soz_tahlil(matn):
    uzunlik = len(matn)
    teskari = matn[::-1]
    uper = matn.upper()
    return render_template("tahlil.html", u=uzunlik, t=teskari, up=uper)



if __name__ == "__main__":
    app.run(debug=True)
