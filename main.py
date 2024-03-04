import pickle

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences

description = """
Teste Prático Ciências de Dados. 🚀
## Sentiment Analysis

Neste endpoint é realizada a classificação de um texto de tweet sobre Covid-19.
A classificação é realizada em 5 categorias de sentimentos:

* **Extremely Positive** (_Extremamente Positivo_).
* **Positive** (_Positivo_).
* **Neutral** (_Neutro_).
* **Negative** (_Negativo_).
* **Extremely Negative** (_Extremamente Negativo_).
"""


app = FastAPI(
    title="PredictAPI",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Jessica Cardoso",
        "url": "https://github.com/jessicacardoso/",
        "email": "jessicasousa.pc@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


class Tweet(BaseModel):
    text: str


with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

model = keras.models.load_model("tweets.keras")

sentiment_list = [
    "Extremely Negative",
    "Extremely Positive",
    "Negative",
    "Neutral",
    "Positive",
]


@app.post("/tweet_sentiment")
def predict_sentiment(tweet: Tweet):
    """Informe o tweet o qual deseja obter uma predição."""
    X = tokenizer.texts_to_sequences([tweet.text])
    X = pad_sequences(X, maxlen=60)
    y_pred = model.predict(X)
    return {"sentiment": sentiment_list[np.argmax(y_pred)]}
