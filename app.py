from flask import Flask, jsonify

from volume_module.sound import Sound

app = Flask(__name__)

@app.route('/vol-up')
def vol_up():
  # Sound.volume_up()
  Sound.volume_set(50)
  resp = {
    "current_vol": Sound.current_volume()
  }

  return resp, 200

@app.route('/vol-down')
def vol_down():
  Sound.volume_down()
  return "Hello World", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
