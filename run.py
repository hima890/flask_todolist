from projectFiles import create_app

app = create_app()

if __name__ == "__min__":
    app.run(debug=True)