from app import create_app, db

app = create_app()

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="127.0.0.1", port=5001)