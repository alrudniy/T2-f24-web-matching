from django.apps import AppConfig

class UserQuestionnaireConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_questionnaire'

# List of house features
features = [
    "Balcony",
    "Multiple floors",
    "Wheelchair access",
    "Pet friendly",
    "Large lot",
    "Low cost",
    "Close to shopping",
    "Close to police station",
    "Close to hospital",
    "Close to fire station",
    "Close to park",
    "Close to school",
    "Close to public transportation",
    "Neighborhood safety",
    "School district quality",
    "Parking availability",
    "Storage space"
]


# Separate area for number of bedrooms and bathrooms? Doesn't really make sense to put them here I feel.

# Store ratings
ratings = {}

@app.route('/')
def index():
    return render_template('index.html', features=features)

@app.route('/rate/<feature>', methods=['GET', 'POST'])
def rate_feature(feature):
    if request.method == 'POST':
        rating = request.form['rating']
        ratings[feature] = rating
        return redirect(url_for('index'))

    return render_template('rate.html', feature=feature)

@app.route('/results')
def results():
    return render_template('results.html', ratings=ratings)

if __name__ == '__main__':
    app.run(debug=True)
