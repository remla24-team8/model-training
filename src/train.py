from model import create_model
from joblib import dump, load
import json
# Load or define necessary variables
#parameters load


char_index = load("output/char_index.joblib")

# Load the data from CSV files
x_train = load("output/x_train.joblib")
x_val = load("output/x_val.joblib")
x_test = load("output/x_test.joblib")

y_train = load("output/y_train.joblib")
y_val = load("output/y_val.joblib")
y_test = load("output/y_test.joblib")

#Clipping of the vocab size, something wrong with tokenizer
vocab_size = len(char_index.keys())
# x_train = np.clip(x_train, 0, vocab_size - 1)
# x_val = np.clip(x_val, 0, vocab_size - 1)
# x_test = np.clip(x_test, 0, vocab_size - 1)


# Create the model and return model parameters
model, params = create_model(char_index)
#training of the model
model.compile(loss=params['loss_function'], optimizer=params['optimizer'], metrics=params['metrics'])


hist = model.fit(x_train, y_train,
                batch_size=params['batch_train'],
                epochs=params['epoch'],
                shuffle=True,
                validation_data=(x_val, y_val)
                )

scores = model.evaluate(x_test, y_test, batch_size=params['batch_test'])

metrics = dict(zip(['loss', 'accuracy'], scores))

#Save the model
dump(model, 'output/model.joblib')


with open('output/metrics.json', 'w+') as json_file:
    json.dump(metrics, json_file, indent=4)

