from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    color = request.args['color'] 
    # the request object stores information that was sent by the client to the server
    #args is a multidict (like a dictionart but can have multiple values for the smae key)
    #the information in args is visible in the url for the page being requested (ex. .../responce.html)
    if color == 'blue':
        reply = "Thats my favorite color too!"
    else:
        reply = "My favorite color is blue!"
    return render_template('response.html',response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
