from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    def NewText():
        characters = 0
        someRandom = ["something","great","boy","live","a","thousand","indian","years","that","is","why","we","live","in","the","better","way"]
        wordList = []
        while characters<2000:
            word = random.choice(someRandom)
            characters+=len(list(word))
            wordList.append(word)
        return wordList

    return render_template("index.html",text=NewText(), index="0")

if __name__ == "__main__":
    app.run(debug=True)
