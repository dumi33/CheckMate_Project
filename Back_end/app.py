from flask import Flask
import students
import classes
import checks

app = Flask(__name__)
app.register_blueprint(students.blue_student)
app.register_blueprint(classes.blue_class)
app.register_blueprint(checks.blue_check)

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port = "8080")