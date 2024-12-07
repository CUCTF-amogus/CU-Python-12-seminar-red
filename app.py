from flask import Flask


from src.route.index_route import index_page


app = Flask(__name__, template_folder="src/templates", static_folder="src/static")
app.register_blueprint(index_page)


if __name__ == "__main__":
    app.run(debug=True)
