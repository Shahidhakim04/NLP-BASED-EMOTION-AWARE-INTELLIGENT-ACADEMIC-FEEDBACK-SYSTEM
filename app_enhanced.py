"""
Enhanced Emotion-Aware Intelligent Academic Feedback System
With Advanced Quality Analysis, Topic Detection, and Progress Tracking
"""

from flask import Flask, render_template, request, session, jsonify
from datetime import datetime
import uuid

# Import original modules
from preprocess import preprocess_text
from emotion_model import detect_emotion

# Import new advanced modules
from advanced_quality_analyzer import AdvancedQualityAnalyzer
from topic_detector import detect_topic, get_topic_emoji
from enhanced_feedback_generator import generate_enhanced_feedback
from progress_tracker import ProgressTracker

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'  # Change this in production!

# Initialize advanced modules
quality_analyzer = AdvancedQualityAnalyzer()
progress_tracker = ProgressTracker()

@app.route("/", methods=["GET", "POST"])
def index():
    # Generate or retrieve session ID for progress tracking
    if 'student_id' not in session:
        session['student_id'] = str(uuid.uuid4())
    
    student_id = session['student_id']
    
    # Default values
    emotion = None
    confidence = None
    quality_metrics = None
    feedback = None
    topic_info = None
    all_emotions = None
    word_count = None
    
    if request.method == "POST":
        answer = request.form.get("answer", "")
        
        if answer.strip() != "":
            try:
                # Preprocess text
                clean = preprocess_text(answer)
                
                # Detect emotions
                emotions = detect_emotion(clean)
                top_emotion = emotions[0]["label"]
                confidence = round(emotions[0]["score"], 2)
                
                # Get all emotions for visualization
                all_emotions = [
                    {
                        'label': e['label'],
                        'score': round(e['score'] * 100, 1)
                    }
                    for e in emotions[:6]  # Top 6 emotions
                ]
                
                # Advanced quality analysis
                quality_metrics = quality_analyzer.analyze_quality(answer)
                word_count = quality_metrics['word_count']
                
                # Topic detection (using keyword method for speed)
                topic_info = detect_topic(answer, use_ml=False)
                topic_info['emoji'] = get_topic_emoji(topic_info['primary_topic'])
                
                # Generate enhanced feedback
                feedback = generate_enhanced_feedback(
                    top_emotion,
                    confidence,
                    quality_metrics,
                    topic_info,
                    word_count
                )
                
                emotion = top_emotion
                
                # Log submission for progress tracking
                submission_data = {
                    'answer': answer[:500],  # Store first 500 chars only
                    'emotion': top_emotion,
                    'confidence': confidence,
                    'quality_metrics': quality_metrics,
                    'topic': topic_info,
                    'word_count': word_count
                }
                progress_tracker.log_submission(student_id, submission_data)
                
            except Exception as e:
                print(f"Error during analysis: {e}")
                # Fallback to simple analysis
                emotion = "neutral"
                confidence = 0.5
                quality_metrics = {
                    'overall_score': 50,
                    'quality_level': 'average'
                }
                feedback = "An error occurred during analysis. Please try again."
    
    # Get progress data for display
    progress_summary = progress_tracker.get_progress_summary(student_id)
    
    template_name = "results.html" if request.method == "POST" and emotion else "index.html"
    
    return render_template(
        template_name,
        emotion=emotion,
        confidence=confidence,
        quality_metrics=quality_metrics,
        feedback=feedback,
        topic_info=topic_info,
        all_emotions=all_emotions,
        word_count=word_count,
        progress_summary=progress_summary
    )

@app.route("/progress")
def progress():
    """Progress dashboard page"""
    student_id = session.get('student_id', None)
    
    if not student_id:
        return render_template("progress.html", no_data=True)
    
    progress_summary = progress_tracker.get_progress_summary(student_id)
    
    return render_template(
        "progress.html",
        progress_summary=progress_summary,
        student_id=student_id
    )

@app.route("/api/progress", methods=["GET"])
def api_progress():
    """API endpoint for progress data (for AJAX requests)"""
    student_id = session.get('student_id', None)
    
    if not student_id:
        return jsonify({'error': 'No student ID found'}), 404
    
    progress_summary = progress_tracker.get_progress_summary(student_id)
    
    if not progress_summary:
        return jsonify({'error': 'No data available'}), 404
    
    return jsonify(progress_summary)

@app.route("/reset-progress", methods=["POST"])
def reset_progress():
    """Reset progress data for current session"""
    student_id = session.get('student_id', None)
    
    if student_id:
        progress_tracker.delete_student_data(student_id)
        session.pop('student_id', None)
    
    return jsonify({'success': True})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
