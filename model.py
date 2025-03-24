def predict_sentiment(text):
    if not text:
        return "neutral"
    text = text.lower()  # Transformation en minuscules pour éviter des erreurs de casse
    if "happy" in text or "good" in text:
        return "positif"  # Changement du retour de "positive" à "positif"
    if "sad" in text or "bad" in text:
        return "negative"
    return"neutral"