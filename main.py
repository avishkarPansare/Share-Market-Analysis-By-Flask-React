from flask_stock_analysis_backend import init_app

app = init_app()


if __name__ == '__main__':
    app.run("0.0.0.0", port=5003, debug=True)
