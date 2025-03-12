from transformers import pipeline

generator = pipeline("text2text-generation", model="facebook/bart-large")

def generate_response(prompt):
    result = generator(prompt, max_length=150, num_return_sequences=1)
    return result[0]['generated_text']
