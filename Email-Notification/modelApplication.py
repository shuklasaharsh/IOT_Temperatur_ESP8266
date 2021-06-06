import turicreate as tc


def loadModel():
    model = tc.load_model('./Time-Model')
    return model


def getPrediction(sf, model):
    prediction = model.predict(sf)
    return prediction


def textPrediction(prediction):
    if prediction[0] > 165:
        return "Cooked"
    else:
        return "Not Cooked"
