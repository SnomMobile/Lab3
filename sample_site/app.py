from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():

    # Load current count
    f = open("count.txt", "r")
    message = (f.read())
    f.close()

    # Render HTML with count variable
    return render_template("index.html", message=message)

app.route("/", methods=["POST"])
def getvalue():
    message=request.form["message"]
    
    f = open("count.txt", "w")
    f.write(str(message))
    f.close()
    
if __name__ == "__main__":
    app.run()
