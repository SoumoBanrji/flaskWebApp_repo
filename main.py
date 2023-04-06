from website import create_app

app = create_app()

# intitializing if this file run then webserver will run
if __name__ == '__main__':
    app.run(debug=True)
