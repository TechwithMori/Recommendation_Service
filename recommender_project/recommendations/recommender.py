import numpy as np
from .models import UserPreference, Item

def get_recommendations(user_id):
    # Get all user preferences
    preferences = UserPreference.objects.filter(user_id=user_id)
    
    # Create a dictionary to hold item scores
    item_scores = {}

    # Calculate scores based on preferences
    for pref in preferences:
        item_scores[pref.item.id] = pref.preference_score

    # Sort items by score
    sorted_items = sorted(item_scores.items(), key=lambda x: x[1], reverse=True)

    # Get the top 5 recommended item IDs
    recommended_items = [item[0] for item in sorted_items[:5]]
    
    return recommended_items
