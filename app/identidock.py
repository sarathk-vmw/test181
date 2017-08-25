from flask import Flask,Response,request 
import requests,hashlib,redis
app=Flask(__name__)

default_name = "srt"
salt = "UNIQUE SALT"

cache = redis.StrictRedis(host="redis", port=6379, db=0)

@app.route("/", methods=["GET", "POST"])
def mainpage():
    name = default_name
    if request.method == "POST":
        name = request.form["name"]

    salted_name = salt + name 
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest()

    header = '<html><head><title>Identidock</title></head>'
    body = '''<body>
                  <form method="POST"> 
                  Name: <input type="text" name="name" value={name} />
                      <input type="submit" value="GET AVATAR" />
                  </form>
                  <p>Your Avatar is:<br><br>
                  <img src="/monster/{name_hash}" /> </p>
           '''.format(name=name, name_hash=name_hash)
    footer = "</body></html>"
  
    
    return header + body + footer

@app.route("/monster/<name>")
def get_identicon(name):
    image = cache.get(name)
    if image is None:
        print "Cache miss"
        r = requests.get("http://dnmonster:8080/monster/" + name + "?size=80")
        image = r.content
        cache.set(name, image)
    return Response(image, mimetype="image/png")

if __name__ == "__main__":
     app.run(debug=True,host="0.0.0.0")
