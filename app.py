from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form['dish']

       
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={search_term}"
        response = requests.get(url).json()
        meals = response.get('meals', [])

        return render_template('select_meal.html', meals=meals, search_term=search_term)

    return render_template('index.html')


@app.route('/meal/<meal_id>')
def meal_detail(meal_id):
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
    response = requests.get(url).json()
    recipe = response['meals'][0]

    ingredients = []
    for i in range(1, 21):
        ing = recipe.get(f"strIngredient{i}")
        measure = recipe.get(f"strMeasure{i}")
        if ing and ing.strip() != "":
            nutri = get_nutrition(ing.strip())
            ingredients.append({
                "name": ing,
                "measure": measure,
                "nutrition": nutri
            })

    return render_template('results.html', recipe=recipe, ingredients=ingredients)



def get_nutrition(ingredient):
    try:
        search_url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={ingredient}&search_simple=1&action=process&json=1&page_size=1"
        res = requests.get(search_url).json()

        if res.get("products"):
            product = res["products"][0]
            nutriments = product.get("nutriments", {})
            return {
                "calories": nutriments.get("energy-kcal_100g"),
                "protein": nutriments.get("proteins_100g"),
                "fat": nutriments.get("fat_100g"),
                "carbs": nutriments.get("carbohydrates_100g"),
            }
        else:
            return {"calories": None, "protein": None, "fat": None, "carbs": None}
    except:
        return {"calories": None, "protein": None, "fat": None, "carbs": None}


if __name__ == "__main__":
    app.run(debug=True)
