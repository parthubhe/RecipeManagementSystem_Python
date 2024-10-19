from flask import Flask,request,render_template,url_for,redirect
from Recipe_List.Recipe_List import RecipeDLL
app = Flask(__name__)
recipe_list = RecipeDLL()

recipe_list.append(1, "Spaghetti", "Italian Pasta", "pancakes.jpg", 30, "pasta, tomatoes", "Boil pasta, make sauce.")
recipe_list.append(2, "Salad", "Greek Salad", "salad.jpeg", 15, "lettuce, tomatoes, cucumber", "Chop vegetables, mix.")
recipe_list.append(3, "Pancakes", "Breakfast Pancakes", "spaget.jpeg", 20, "flour, eggs, milk", "Mix ingredients, fry.")


@app.route('/')
def home_page():
    return render_template('index.html',recipes = recipe_list) #render html boiler plate here using render_template('index.html')
@app.route('/recipe/<int:id>')
def view_recipe(id):
    recipe = recipe_list.get_recipe_by_id(id) #when the button is clicked we view a seperate card using get_by_id()  method which renders the recipe_detail.html
    if not recipe:
        return "recipe not found"
    return render_template('recipe_detail.html',recipe = recipe)

@app.route('/add', methods = ['GET','POST'])
def add_recipe():
    if request.method == 'POST':
        id = len(list(recipe_list)) +1
        name = request.form['name'] #getting the attributes from user using the html form
        title = request.form['title']
        image_url = request.form['image_url']
        time_required = int(request.form['time_required'])
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']

        recipe_list.append(id, name, title, image_url, time_required, ingredients, instructions)
        return redirect(url_for('home_page'))
    return render_template('add_recipe.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_recipe(id):
    recipe = recipe_list.get_recipe_by_id(id)
    if not recipe:
        return "Recipe not found",404
    if request.method == 'POST':
        recipe.name = request.form['name']
        recipe.title = request.form['title']
        recipe.image_url = request.form['image_url']
        recipe.time_required = int(request.form['time_required'])
        recipe.ingredients = request.form['ingredients']
        recipe.instructions = request.form['instructions']

        return redirect(url_for('view_recipe', id = recipe.id))
    return  render_template('edit_recipe.html',recipe = recipe)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_recipe(id):
    recipe_list.delete_recipe(id)
    return redirect(url_for('home_page'))
if __name__ == "__main__":
    app.run(debug = True)

"""Notes:
 <!-- #the {%block content%} is a template(in Jinja2 of FLask) that is used to reference other html files body in the main tag in the base template -->
"""