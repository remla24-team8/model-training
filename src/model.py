"""
Defines the model architecture for the text classification task.
"""


from keras.models import Sequential
from keras.layers import Embedding, Conv1D, MaxPooling1D, Flatten, Dense, Dropout


# model definition
def create_model(char_index):
    """
    Create a convolutional neural network model for text classification.

    Args:
        char_index (dict): A dictionary mapping characters to their corresponding indices.

    Returns:
        model (Sequential): The created Keras Sequential model.
        params (dict): A dictionary containing the model parameters.
    """
    # Parameters
    params = {
        "loss_function": "binary_crossentropy",
        "optimizer": "adam",
        "sequence_length": 200,
        "batch_train": 5000,
        "batch_test": 5000,
        "categories": ["phishing", "legitimate"],
        "char_index": char_index,
        "epoch": 20,
        "embedding_dimension": 50,
        "dataset_dir": "../dataset/small_dataset/",
        "metrics": ["accuracy"],
    }

    embedding_dimension = params["embedding_dimension"]

    model = Sequential()

    voc_size = len(char_index.keys())
    print(f"voc_size: {voc_size}")
    model.add(
        Embedding(
            input_dim=voc_size + 1,
            output_dim=embedding_dimension,
            input_length=params["sequence_length"],
        )
    )

    model.add(Conv1D(128, 3, activation="tanh"))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 7, activation="tanh", padding="same"))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 5, activation="tanh", padding="same"))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 3, activation="tanh", padding="same"))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 5, activation="tanh", padding="same"))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 3, activation="tanh", padding="same"))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 3, activation="tanh", padding="same"))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Flatten())

    model.add(Dense(1, activation="sigmoid"))
    return model, params
