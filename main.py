from flask import *
from SQL_Parser import format_query

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def interface():
    if request.method == "POST":
        query = request.form["query"]
        output = format_query(query)
        return render_template('frontend.html', output_dictionary = output)
    else:
       return render_template('frontend.html')

if __name__ == '__main__':
   app.run(debug=True)