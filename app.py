from flask import Flask, render_template, request, jsonify
import searchengine
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    result = searchengine.searchengine(user_input)
    return jsonify(result=result)

# Custom highlight filter
@app.template_filter('highlight')
def highlight(text, search_input):
    if search_input:
        return text.replace(search_input, f'<span class="highlight">{search_input}</span>')
    return text

if __name__ == '__main__':
    app.run(debug=True)
