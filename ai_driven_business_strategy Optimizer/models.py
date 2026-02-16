import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class MarketTrendPredictor:
    def __init__(self, units=128, layers=3):
        self.model = self._build_model(units, layers)
    
    def _build_model(self, units, layers):
        model = Sequential()
        for i in range(layers):
            if i == 0:
                model.add(LSTM(units, return_sequences=True))
            else:
                model.add(LSTM(units, return_sequences=False))
        model.add(Dense(1))
        model.compile(loss='mean_squared_error', optimizer='adam')
        return model

    def train(self, data, epochs=50, batch_size=64):
        # Assuming data is preprocessed and normalized
        self.model.fit(data, epochs=epochs, batch_size=batch_size)

    def predict(self, data):
        # Reshape input for LSTM
        data = np.array(data).reshape((1, -1))
        return self.model.predict(data)[0][0]