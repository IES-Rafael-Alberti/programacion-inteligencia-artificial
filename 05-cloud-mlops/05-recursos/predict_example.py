import os
import numpy as np
import hopsworks
import joblib


class Predict(object):

    def __init__(self):
        """ Initializes the serving state, reads a trained model"""
        # Get feature store handle
        project = hopsworks.login()
        self.mr = project.get_model_registry()

        # Retrieve the feature view from the model
        retrieved_model = self.mr.get_model(
            name="fraud",
            version=1,
        )
        self.feature_view = retrieved_model.get_feature_view()

        # Load the trained model
        self.model = joblib.load(os.environ["MODEL_FILES_PATH"] + "/xgboost_model.pkl")
        print("Initialization Complete")

    def predict(self, inputs):
        """ Serves a prediction request usign a trained model"""
        feature_vector = self.feature_view.get_feature_vector({"cc_num": inputs[0][0]})
        feature_vector = feature_vector[:-2] + feature_vector[-1:]

        return self.model.predict(np.asarray(feature_vector).reshape(1, -1)).tolist() # Numpy Arrays are not JSON serializable
