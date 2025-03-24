from transformers import pipeline

summarizer = pipeline("summarization", model="google/t5-small")
email_text = """Dear Team, I hope this email finds you well. I wanted to provide an update on our project..."""
summary = summarizer(email_text, max_length=50, min_length=10, do_sample=False)

print(summary[0]['summary_text'])
