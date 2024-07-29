def add_feedback(feedback_dict, sentiment, message):
    feedback_dict.setdefault(sentiment.lower(), []).append(message)
    print(f"Feedback added to '{sentiment}' category.")

def display_feedback_count(feedback_dict):
    for sentiment, messages in feedback_dict.items():
        print(f"{sentiment.title()}: {len(messages)} feedback(s)")

def show_feedback_for_sentiment(feedback_dict, sentiment):
    messages = feedback_dict.get(sentiment.lower(), [])
    if messages: 
        print(f"Feedback for '{sentiment}':")
        for message in messages:
            print(f"- {message}")
    else:
        print(f"No feedback available for '{sentiment}'.")


customer_feedback = {"positive": [], "negative": [], "neutral": []}

add_feedback(customer_feedback, "Positve", "Great product!")
add_feedback(customer_feedback, "Neutral", "It's okay, but it could be better.")
add_feedback(customer_feedback, "Positve", "Absolutely love this!")
display_feedback_count(customer_feedback)
show_feedback_for_sentiment(customer_feedback, "negative")