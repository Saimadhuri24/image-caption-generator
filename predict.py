import numpy as np
import pickle

from tensorflow.keras.models import load_model, Model
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model once
print("Loading model...")
model = load_model("caption_model.keras")

print("INPUT SHAPE:", model.input_shape)
print("OUTPUT SHAPE:", model.output_shape)
print("NUMBER OF INPUTS:", len(model.inputs))

model.summary()

# Load tokenizer once
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

max_length = 33

# VGG16 Feature Extractor
base_model = VGG16(weights="imagenet")

vgg_model = Model(
    inputs=base_model.inputs,
    outputs=base_model.layers[-2].output
)


def extract_features(image_path):

    image = load_img(
        image_path,
        target_size=(224, 224)
    )

    image = img_to_array(image)

    image = np.expand_dims(
        image,
        axis=0
    )

    image = preprocess_input(image)

    feature = vgg_model.predict(
        image,
        verbose=0
    )

    return feature


def idx_to_word(integer, tokenizer):

    return tokenizer.index_word.get(integer)


def predict_caption(model, image_feature, tokenizer, max_length):

    in_text = "<start>"
    used_words = []

    for _ in range(max_length):

        sequence = tokenizer.texts_to_sequences([in_text])[0]

        sequence = pad_sequences(
            [sequence],
            maxlen=max_length
        )

        yhat = model.predict(
            [image_feature, sequence],
            verbose=0
        )

        yhat = np.argmax(yhat[0])

        word = idx_to_word(yhat, tokenizer)

        if word is None:
            break

        if word == "<end>":
            break

        # stop if word appears too many times
        if used_words.count(word) >= 2:
            break

        used_words.append(word)

        in_text += " " + word

    return in_text


def generate_caption(image_path):

    feature = extract_features(
        image_path
    )

    caption = predict_caption(
        model,
        feature,
        tokenizer,
        max_length
    )

    caption = caption.replace(
        "<start>",
        ""
    )

    caption = caption.replace(
        "<end>",
        ""
    )

    caption = caption.strip()

    bad_endings = [
        "and",
        "with",
        "of",
        "the",
        "in",
        "on",
        "is"
    ]

    words = caption.split()

    while words and words[-1].lower() in bad_endings:
        words.pop()

    caption = " ".join(words)

    return caption.strip()