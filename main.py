from flask import Flask, render_template, url_for, request
import requests
import re

URL = "https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=[topic]" #konstant som ikke skal endres på

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Function that checks if the request method is POST, and if this is true, it gets the topic the user has written and get the number of occurrences of the topic.

    Returns:
        Call on the render_template-method to render the index.html file in the browser.
    """

    nr_of_topic = 0
    if request.method == 'POST':
        topic = request.form['topic']
        nr_of_topic = get_number(topic)
    return render_template('index.html', nr_of_topic=nr_of_topic)

def get_number(topic):
    """
    Function that retrieve information from the URL and search through the information for finding the number of occurrences of the topic.

    Args:
        topic (String): The topic you want to retrieve information from.

    Returns:
        Int: the number of occurrences of the topic.
    """

    page = {'page':topic}
    http_respons = requests.get(url = URL, params = page)
    regex = "(" + topic + ")"
    nr_of_topic = len(re.findall(regex, http_respons.text))
    print("Number of the topic " + topic + " is " + str(nr_of_topic))
    return nr_of_topic

if __name__ == "__main__":
    app.run(debug=True)
