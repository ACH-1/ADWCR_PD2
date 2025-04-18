from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/decision", methods=["GET"])
def decision():
    try:
        age = int(request.args.get("age"))
        income = float(request.args.get("income"))

        if age < 25 and income < 3000:
            result = "Niska zdolność kredytowa"
        elif income > 10000:
            result = "Wysoka zdolność kredytowa"
        else:
            result = "Średnia zdolność kredytowa"

        return jsonify({"decision": result})
    except:
        return jsonify({"error": "Bad Request"}), 400

if __name__ == "__main__":
    app.run()