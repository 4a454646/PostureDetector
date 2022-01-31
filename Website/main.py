from flask import Flask, render_template, request, Response
import cv2


def gen_frames():
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

camera = cv2.VideoCapture(0)


app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

@app.route('/')
def hello_world():
  return render_template("status.html")

@app.route('/', methods=['POST'])
def hello_world_post():
  first_name = request.form['fname']
  last_name = request.form['lname']
  return render_template("status.html", message = "You are a loser, " + first_name + " " + last_name)

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


app.run(host='0.0.0.0', port=8080)

