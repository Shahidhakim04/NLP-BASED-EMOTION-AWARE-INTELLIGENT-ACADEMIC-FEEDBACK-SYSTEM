"""
Enhanced Feedback Generator
Generates more sophisticated, context-aware feedback
"""

def generate_enhanced_feedback(emotion, confidence, quality_metrics, topic_info, word_count):
    """
    Generate comprehensive, personalized feedback
    
    Args:
        emotion: Primary detected emotion
        confidence: Emotion detection confidence
        quality_metrics: Dict with quality scores
        topic_info: Dict with topic detection results
        word_count: Number of words in answer
    """
    feedback_parts = []
    
    # 1. Opening based on emotion
    opening = _generate_emotion_opening(emotion, confidence)
    feedback_parts.append(opening)
    
    # 2. Topic acknowledgment
    if topic_info and topic_info.get('primary_topic'):
        topic_text = _generate_topic_comment(topic_info)
        feedback_parts.append(topic_text)
    
    # 3. Quality analysis
    quality_text = _generate_quality_feedback(quality_metrics, word_count)
    feedback_parts.append(quality_text)
    
    # 4. Specific improvements
    improvements = _generate_improvement_suggestions(quality_metrics, emotion)
    if improvements:
        feedback_parts.append(improvements)
    
    # 5. Encouraging conclusion
    conclusion = _generate_conclusion(emotion, quality_metrics.get('overall_score', 0))
    feedback_parts.append(conclusion)
    
    return " ".join(feedback_parts)

def _generate_emotion_opening(emotion, confidence):
    """Generate opening based on detected emotion"""
    high_confidence = confidence > 0.8
    
    emotion_openings = {
        "joy": {
            "high": "Your response radiates enthusiasm and positive engagement with the topic! This positive mindset is excellent for learning.",
            "low": "Your answer shows some positive engagement with the material, which is great for effective learning."
        },
        "sadness": {
            "high": "I notice some uncertainty in your response. Remember, feeling challenged is a natural part of the learning process.",
            "low": "Your answer suggests you may be finding some aspects challenging. This is completely normal when learning complex concepts."
        },
        "fear": {
            "high": "I sense some anxiety in your response. It's important to know that feeling nervous during academic work is completely normal.",
            "low": "There seems to be some hesitation in your answer. Remember, making mistakes is how we learn and grow."
        },
        "anger": {
            "high": "Your response suggests some frustration. This often happens when concepts are particularly challenging.",
            "low": "I detect a bit of frustration, which is understandable when dealing with difficult material."
        },
        "surprise": {
            "high": "Your answer reflects genuine curiosity and discovery! This engaged mindset is perfect for deep learning.",
            "low": "Your response shows interest in the topic, which is a great foundation for understanding."
        },
        "neutral": {
            "high": "Your response is measured and focused, showing a professional approach to the topic.",
            "low": "Your answer maintains a balanced perspective on the subject matter."
        },
        "disgust": {
            "high": "I notice strong feelings about this topic. Let's channel that energy into constructive analysis.",
            "low": "Your response shows you have strong opinions. Academic discussion benefits from all perspectives."
        }
    }
    
    confidence_level = "high" if high_confidence else "low"
    return emotion_openings.get(emotion, emotion_openings["neutral"])[confidence_level]

def _generate_topic_comment(topic_info):
    """Generate comment about the detected topic"""
    topic = topic_info.get('primary_topic', 'General')
    confidence = topic_info.get('confidence', 0)
    
    if confidence > 0.7:
        return f"I can clearly see you're working on {topic}-related content."
    elif confidence > 0.4:
        return f"Your answer appears to focus on {topic}."
    else:
        return "Your response covers an interesting academic topic."

def _generate_quality_feedback(quality_metrics, word_count):
    """Generate detailed quality feedback"""
    overall = quality_metrics.get('overall_score', 0)
    length_score = quality_metrics.get('length_score', 0)
    complexity_score = quality_metrics.get('complexity_score', 0)
    vocabulary_score = quality_metrics.get('vocabulary_score', 0)
    readability_score = quality_metrics.get('readability_score', 0)
    structure_score = quality_metrics.get('structure_score', 0)
    
    feedback = []
    
    # Overall quality
    if overall >= 85:
        feedback.append("Your answer demonstrates excellent quality overall.")
    elif overall >= 75:
        feedback.append("Your answer shows good quality with room for minor enhancements.")
    elif overall >= 60:
        feedback.append("Your answer is satisfactory but has clear areas for improvement.")
    else:
        feedback.append("Your answer needs significant development to meet academic standards.")
    
    # Length feedback
    if length_score < 50:
        feedback.append(f"At {word_count} words, your answer is too brief. Aim for at least 50 words to adequately address the topic.")
    elif length_score < 75 and word_count < 100:
        feedback.append(f"Your answer length ({word_count} words) is acceptable, but more elaboration would strengthen your response.")
    
    # Complexity feedback
    if complexity_score < 60:
        feedback.append("Try using more varied sentence structures to add depth to your analysis.")
    elif complexity_score > 90:
        feedback.append("Your sentences are well-structured. Ensure clarity isn't sacrificed for complexity.")
    
    # Vocabulary feedback
    if vocabulary_score < 60:
        feedback.append("Consider using a wider range of vocabulary to express your ideas more precisely.")
    elif vocabulary_score > 85:
        feedback.append("Your vocabulary usage demonstrates strong command of the subject matter.")
    
    # Readability feedback
    if readability_score < 60:
        feedback.append("The text could be more readable. Consider breaking down complex ideas into clearer explanations.")
    
    # Structure feedback
    if structure_score < 60:
        feedback.append("Improve your answer's organization with clear paragraphs and transitional phrases.")
    elif structure_score > 80:
        feedback.append("Your answer is well-organized and easy to follow.")
    
    return " ".join(feedback)

def _generate_improvement_suggestions(quality_metrics, emotion):
    """Generate specific, actionable improvement suggestions"""
    suggestions = []
    overall = quality_metrics.get('overall_score', 0)
    
    # Based on quality level
    if overall < 60:
        suggestions.append("Focus on expanding your explanation with specific examples and detailed reasoning.")
    
    if quality_metrics.get('structure_score', 0) < 70:
        suggestions.append("Use transitional words like 'however,' 'therefore,' and 'for example' to improve flow.")
    
    if quality_metrics.get('vocabulary_score', 0) < 70:
        suggestions.append("Incorporate subject-specific terminology to demonstrate deeper understanding.")
    
    # Based on emotion
    if emotion in ['fear', 'sadness']:
        suggestions.append("Take your time and break down complex problems into smaller, manageable parts.")
    elif emotion == 'anger':
        suggestions.append("Step back and approach the topic from different angles to find clarity.")
    
    if suggestions:
        return "Key improvements: " + " ".join(suggestions)
    return ""

def _generate_conclusion(emotion, overall_score):
    """Generate encouraging conclusion"""
    if overall_score >= 80:
        conclusions = [
            "Keep up the excellent work! Your understanding is clearly strong.",
            "Outstanding effort! Continue this level of engagement.",
            "You're demonstrating mastery of the material. Well done!"
        ]
    elif overall_score >= 60:
        conclusions = [
            "You're on the right track. Keep refining your approach!",
            "Good progress! Focus on the suggested improvements to reach the next level.",
            "Solid foundation. With some refinement, you'll excel!"
        ]
    else:
        conclusions = [
            "Keep practicing! Every attempt helps you improve.",
            "Don't be discouraged. Focus on small improvements each time.",
            "Remember, learning is a journey. Each step forward matters!"
        ]
    
    # Add emotion-specific encouragement
    if emotion in ['sadness', 'fear']:
        return conclusions[0] + " Remember, challenges are opportunities for growth."
    elif emotion == 'joy':
        return conclusions[0] + " Your positive attitude will carry you far!"
    else:
        return conclusions[0]

# Backward compatibility - simple feedback generator
def generate_feedback(emotion, confidence, quality):
    """
    Simple feedback generator for backward compatibility
    Maps old quality levels to scores
    """
    quality_map = {
        'poor': 30,
        'below_average': 50,
        'average': 65,
        'good': 80,
        'excellent': 95
    }
    
    score = quality_map.get(quality, 50)
    
    # Create simplified metrics
    quality_metrics = {
        'overall_score': score,
        'length_score': score,
        'complexity_score': score,
        'vocabulary_score': score,
        'readability_score': score,
        'structure_score': score
    }
    
    topic_info = {'primary_topic': 'General', 'confidence': 0.5}
    word_count = 50 if quality == 'poor' else 100
    
    return generate_enhanced_feedback(emotion, confidence, quality_metrics, topic_info, word_count)
