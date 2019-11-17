from flask import redirect
import connexion

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir='swagger/')

# Read the swagger.yml file to configure the endpoints
app.add_api('api.yml')

@app.route('/')
@app.route('/api')
def display_api_doc():
    return redirect('/api/ui', code=302)


if __name__ == '__main__':
    app.run()
