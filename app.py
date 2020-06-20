from flask import Flask, render_template

from volume_module.SystemVolume import SystemVolume

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/vol-up')
def vol_up():
    system_vol = SystemVolume()
    system_vol.vol_up()
    resp = {
        "current_vol": system_vol.get_vol()
    }
    return resp, 200


@app.route('/vol-down')
def vol_down():
    system_vol = SystemVolume()
    system_vol.vol_down()
    resp = {
        "current_vol": system_vol.get_vol()
    }
    return resp, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
