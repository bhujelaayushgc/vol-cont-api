from flask import Flask, request

from volume_module.SystemVolume import SystemVolume

app = Flask(__name__)


system_vol = SystemVolume()

@app.route('/')
def home():
    # system_vol = SystemVolume()
    system_vol.vol_up()
    resp = {
        "current_vol": system_vol.get_vol()
    }
    return resp, 200


@app.route('/vol-up', methods=['POST'])
def vol_up():
    # system_vol = SystemVolume()
    system_vol.vol_up()
    resp = {
        "current_vol": system_vol.get_vol()
    }
    return resp, 200


@app.route('/vol-down', methods=['POST'])
def vol_down():
    # system_vol = SystemVolume()
    system_vol.vol_down()
    resp = {
        "current_vol": system_vol.get_vol()
    }
    return resp, 200

@app.route('/mute', methods=['POST'])
def mute():
    # system_vol = SystemVolume()
    system_vol.mute()
    resp = {
        "current_vol": system_vol.get_vol(),
        "isMute": system_vol.volume.GetMute() == 1
    }
    return resp, 200

@app.route('/unmute', methods=['POST'])
def unmute():
    # system_vol = SystemVolume()
    system_vol.unmute()
    resp = {
        "current_vol": system_vol.get_vol(),
        "isMute": system_vol.volume.GetMute() == 1
    }
    return resp, 200

@app.route('/vol', methods=['POST', 'GET'])
def set_get_vol():
    if request.method == 'POST':
        vol = request.get_json()['volLevel']
        # system_vol = SystemVolume()
        system_vol.set_vol(vol)
        resp = {
            "current_vol": system_vol.get_vol()
        }
        return resp, 200
    else:
        # system_vol = SystemVolume()
        resp = {
            "current_vol": system_vol.get_vol()
        }
        return resp, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
