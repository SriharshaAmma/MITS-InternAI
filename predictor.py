# predictor.py

def predict_success(features):
    """
    Predicts student success score based on CGPA, projects, internships, and participation.
    Args:
        features (dict): Dictionary with keys: 'cgpa', 'projects', 'internships', 'participation'.
    Returns:
        str: Prediction result string.
    """
    # Weighted scoring system
    score = (
        features['cgpa'] * 0.4 +
        features['projects'] * 0.2 +
        features['internships'] * 0.2 +
        features['participation'] * 0.2
    )

    # Simple prediction logic
    if score >= 7.5:
        return "High chance of success 🎯"
    elif score >= 5.0:
        return "Moderate chance of success ⚠️"
    else:
        return "Low chance of success 😕"
