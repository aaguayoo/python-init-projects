"""Signal processing functionalities."""
import librosa
import numpy as np


def extract_signal(filename: str) -> np.ndarray:
    signal, _ = librosa.load(filename)
    return signal
