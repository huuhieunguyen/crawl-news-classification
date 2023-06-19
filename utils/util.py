import re
import underthesea

# Save model
# import joblib
# joblib.dump(vectorizer, 'vectorizer.joblib')
# joblib.dump(model, 'model.joblib')

# # Load model
# import joblib
# vectorizer = joblib.load('vectorizer.joblib')
# model = joblib.load('model.joblib')

def preprocess(txt, lower=True):
    txt = re.sub(r'[^\w\s]', '', txt)
    txt = re.sub(r'[\d]', '', txt)
    txt = re.sub('\s+', ' ', txt)
    txt = txt.strip()
    if lower:
        txt = txt.lower()
    txt = underthesea.word_tokenize(txt, format='text')
    return txt