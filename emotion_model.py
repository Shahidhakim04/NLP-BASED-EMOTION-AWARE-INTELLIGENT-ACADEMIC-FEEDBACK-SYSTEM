from transformers import pipeline

emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def detect_emotion(text):
    predictions = emotion_classifier(text)[0]
    predictions = sorted(predictions, key=lambda x: x["score"], reverse=True)
    return predictions
