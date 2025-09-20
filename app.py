# Importing flask function
from flask import Flask, render_template, request, redirect, url_for
# Importing all function from database.py
from database import init_db, add_item, get_all_items, get_item_by_id, update_item, delete_item
import subprocess

app = Flask(__name__)

init_db()

# This a home route or we called index route
@app.route('/')
def index():
    sort_by = request.args.get('sort_by')
    filter_category = request.args.get('filter_category')
    filter_genre = request.args.get('filter_genre')

    
    items = get_all_items(
        sort_by, 
        filter_category,
        filter_genre)
    return render_template(
        'index.html', 
        items=items, 
        sort_by=sort_by,
        filter_category=filter_category,
        filter_genre=filter_genre
        )

@app.route('/add', methods=['GET', 'POST'])
def add_item_route():
    if request.method == 'POST':
        title = request.form['title']
        item_type = request.form['category']
        genre = request.form['genre']
        rating = request.form['rating']
        status = request.form['status']

        
        add_item(title, item_type, genre, rating, status)

        return redirect(url_for('index'))
    return render_template('add_item.html')


@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item_route(item_id):
    item = get_item_by_id(item_id)

    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        genre = request.form['genre']
        rating = request.form['rating']
        status = request.form['status']

        update_item(item_id, title, category, genre, rating, status)
        return redirect(url_for('index'))
    
    return render_template('edit_item.html', item=item)
        

@app.route('/delete/<int:item_id>', methods=['GET'])
def delete_item_route(item_id):
    delete_item(item_id)
    return redirect(url_for('index'))

# Route for ask ai
@app.route('/ask_ai', methods=['GET','POST'])
def ask_ai():
    response = None
    if request.method == 'POST':
        user_query = request.form['query']
        response = query_ai(user_query)
    return render_template('ask_ai.html',response=response)



# To call the ai prompt
def query_ai(prompt):
    result = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True, text=True
    )
    return result.stdout.strip()

if __name__ == '__main__':
    app.run(debug=True)
