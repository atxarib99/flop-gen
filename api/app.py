from connexion import FlaskApp

app = FlaskApp("flop-gen")

def post_greeting(name: str):
    return f"Hello {name}", 200

def get_filters():
    return {'name': 'texture', 'description': 'Flop texture', 'options': ['rainbow', 'two tone', 'monotone']}

def generate(generateRequest: str):
    return None

app.add_api("openapi.yaml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)
