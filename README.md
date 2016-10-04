# Cats_and_Dogs_Flask-app

Demo flask app that exposes random images from dogs and cats:

It exposes three endpoints:

"/" -> shows random gifs from dogs and cats 

"/dogs" -> shows random gifs from dogs 

"/cats" -> shows random gifs from cats

If you can download this project by docker image you can do this:

```
docker pull myolnir/flask-app
docker run -p 8888:5000 --name flask-app myolnir/flask-app
```

Enjoy!
