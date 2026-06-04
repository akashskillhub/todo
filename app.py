from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return {"message":"app running"}

@app.route("/todo/create", methods=["POST"])
def createTodo():
    return {"message":"todo create success"}

@app.route("/todos", methods=["GET"])
def readTodo():
    return {"message":"todo read success"}

@app.route("/todo/modify", methods=["PATCH"])
def udpateTodo():
    return {"message":"todo update success"}

@app.route("/todo/remove", methods=["DELETE"])
def deleteTodo():
    return {"message":"todo delete success"}


if __name__ == "__main__":
    app.run(debug=True)