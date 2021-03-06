from flask import Flask
import students
import classes
import checks,oauths
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
CORS(app, resources={r'*': {'origins': '*'}})
app.register_blueprint(students.blue_student)
app.register_blueprint(classes.blue_class)
app.register_blueprint(checks.blue_check)
app.register_blueprint(oauths.blue_oauth)


if __name__ == "__main__" :
    app.run(host="0.0.0.0", port = "8080")