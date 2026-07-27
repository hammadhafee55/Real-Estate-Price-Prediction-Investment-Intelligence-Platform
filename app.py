

from flask import Flask, request, jsonify, render_template

from flask_cors import CORS

import pandas as pd

import numpy as np

import joblib

import json

import os


app = Flask(__name__)

CORS(app)


# Load Models

price_model = joblib.load(

    "models/price_model.pkl"

)


investment_model = joblib.load(

    "models/investment_model.pkl"

)


rating_model = joblib.load(

    "models/rating_model.pkl"

)


# Load Features

with open(

    "models/model_features.json",

    "r"

) as file:

    features = json.load(file)


@app.route("/")

def home():

    return render_template(

        "index.html"

    )


@app.route("/api/health")

def health():

    return jsonify({

        "status": "online",

        "message": "Real Estate AI API is running"

    })


@app.route(

    "/api/predict",

    methods=["POST"]

)

def predict():

    try:

        data = request.get_json()


        # Price Input

        price_input = pd.DataFrame([

            {

                feature: data.get(feature)

                for feature in features[

                    "price_features"

                ]

            }

        ])


        # Investment Input

        investment_input = pd.DataFrame([

            {

                feature: data.get(feature)

                for feature in features[

                    "investment_features"

                ]

            }

        ])


        # Rating Input

        rating_input = pd.DataFrame([

            {

                feature: data.get(feature)

                for feature in features[

                    "rating_features"

                ]

            }

        ])


        # Predictions

        predicted_price = price_model.predict(

            price_input

        )[0]


        predicted_score = investment_model.predict(

            investment_input

        )[0]


        predicted_score = np.clip(

            predicted_score,

            0,

            100

        )


        predicted_rating = rating_model.predict(

            rating_input

        )[0]


        # Strategy

        if predicted_score >= 75:

            strategy = "Buy & Rent / Strong Investment"

        elif predicted_score >= 60:

            strategy = "Buy for Appreciation"

        elif predicted_score >= 40:

            strategy = "Evaluate Carefully"

        else:

            strategy = "Avoid / High Risk"


        return jsonify({

            "success": True,

            "predicted_price": round(

                float(predicted_price),

                2

            ),

            "investment_score": round(

                float(predicted_score),

                2

            ),

            "investment_rating": str(

                predicted_rating

            ),

            "recommended_strategy": strategy

        })


    except Exception as error:

        return jsonify({

            "success": False,

            "error": str(error)

        }), 500


if __name__ == "__main__":

    port = int(

        os.environ.get(

            "PORT",

            5000

        )

    )


    app.run(

        host="0.0.0.0",

        port=port,

        debug=False

    )

