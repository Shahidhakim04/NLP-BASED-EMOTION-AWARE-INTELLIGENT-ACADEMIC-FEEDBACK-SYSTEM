"""
Topic Detector
Automatically detects the academic subject/topic of student answers
"""

from transformers import pipeline
import re

# Initialize zero-shot classifier
try:
    classifier = pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli"
    )
except:
    classifier = None

# Academic topics/subjects
ACADEMIC_TOPICS = [
    "Mathematics",
    "Physics", 
    "Chemistry",
    "Biology",
    "Computer Science",
    "Programming",
    "History",
    "Literature",
    "English Language",
    "Economics",
    "Psychology",
    "Philosophy",
    "Engineering",
    "Medicine",
    "Geography",
    "Political Science",
    "Sociology",
    "Business",
    "Statistics",
    "Data Science"
]

def detect_topic(text, use_ml=True):
    """
    Detect the academic topic/subject of the text
    
    Args:
        text: The answer text to analyze
        use_ml: Whether to use ML model (slower but more accurate)
        
    Returns:
        dict with primary_topic, confidence, and top topics
    """
    
    if use_ml and classifier:
        try:
            result = classifier(text, ACADEMIC_TOPICS, multi_label=False)
            
            return {
                'primary_topic': result['labels'][0],
                'confidence': round(result['scores'][0], 3),
                'all_topics': {
                    label: round(score, 3) 
                    for label, score in zip(result['labels'][:5], result['scores'][:5])
                }
            }
        except Exception as e:
            print(f"ML topic detection failed: {e}")
            return _detect_topic_keywords(text)
    else:
        return _detect_topic_keywords(text)

def _detect_topic_keywords(text):
    """
    Fallback method using keyword matching
    Fast but less accurate than ML approach
    """
    text_lower = text.lower()
    
    # Define keywords for each topic
    topic_keywords = {
        "Mathematics": ["equation", "theorem", "proof", "algebra", "calculus", "geometry", 
                       "derivative", "integral", "matrix", "vector", "logarithm", "function"],
        "Physics": ["force", "energy", "momentum", "velocity", "acceleration", "quantum",
                   "wave", "particle", "gravity", "thermodynamics", "mechanics", "relativity"],
        "Chemistry": ["molecule", "atom", "compound", "reaction", "element", "periodic",
                     "bond", "acid", "base", "oxidation", "reduction", "catalyst"],
        "Biology": ["cell", "organism", "dna", "gene", "protein", "evolution", "species",
                   "tissue", "organ", "photosynthesis", "mitosis", "ecosystem"],
        "Computer Science": ["algorithm", "data structure", "programming", "code", "function",
                            "variable", "loop", "array", "database", "software", "binary"],
        "Programming": ["python", "java", "javascript", "function", "class", "variable",
                       "loop", "array", "object", "method", "syntax", "debug"],
        "History": ["century", "war", "revolution", "ancient", "medieval", "empire",
                   "civilization", "dynasty", "treaty", "independence", "colonial"],
        "Literature": ["author", "novel", "poem", "character", "plot", "theme", "metaphor",
                      "symbolism", "narrative", "protagonist", "literary"],
        "Economics": ["market", "demand", "supply", "inflation", "gdp", "trade", "price",
                     "economy", "fiscal", "monetary", "investment", "consumer"],
        "Psychology": ["behavior", "cognitive", "emotion", "personality", "mental", "therapy",
                      "consciousness", "perception", "memory", "learning", "social"],
        "Philosophy": ["ethics", "moral", "logic", "metaphysics", "epistemology", "existence",
                      "consciousness", "truth", "argument", "reasoning", "virtue"],
        "Engineering": ["design", "system", "circuit", "mechanical", "electrical", "structure",
                       "material", "stress", "load", "analysis", "optimization"],
    }
    
    # Count keyword matches for each topic
    topic_scores = {}
    for topic, keywords in topic_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        if score > 0:
            topic_scores[topic] = score
    
    if not topic_scores:
        return {
            'primary_topic': 'General',
            'confidence': 0.5,
            'all_topics': {'General': 0.5}
        }
    
    # Sort by score
    sorted_topics = sorted(topic_scores.items(), key=lambda x: x[1], reverse=True)
    total_score = sum(topic_scores.values())
    
    return {
        'primary_topic': sorted_topics[0][0],
        'confidence': round(sorted_topics[0][1] / total_score, 3),
        'all_topics': {
            topic: round(score / total_score, 3) 
            for topic, score in sorted_topics[:5]
        }
    }

def get_topic_emoji(topic):
    """Get emoji representation for topic"""
    emoji_map = {
        "Mathematics": "🔢",
        "Physics": "⚛️",
        "Chemistry": "🧪",
        "Biology": "🧬",
        "Computer Science": "💻",
        "Programming": "👨‍💻",
        "History": "📜",
        "Literature": "📚",
        "Economics": "💰",
        "Psychology": "🧠",
        "Philosophy": "🤔",
        "Engineering": "⚙️",
        "Medicine": "⚕️",
        "Geography": "🌍",
        "General": "📖"
    }
    return emoji_map.get(topic, "📖")
