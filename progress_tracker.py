"""
Progress Tracker
Tracks student submissions and progress over time
"""

import json
import os
from datetime import datetime

class ProgressTracker:
    def __init__(self, data_file='data/progress.json'):
        self.data_file = data_file
        self._ensure_data_directory()
        self.data = self._load_data()
    
    def _ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        data_dir = os.path.dirname(self.data_file)
        if data_dir and not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def _load_data(self):
        """Load progress data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _save_data(self):
        """Save progress data to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def log_submission(self, student_id, submission_data):
        """
        Log a new submission for a student
        
        Args:
            student_id: Unique identifier for student (can use session ID for demo)
            submission_data: Dict containing all analysis results
        """
        if student_id not in self.data:
            self.data[student_id] = {
                'submissions': [],
                'statistics': {
                    'total_submissions': 0,
                    'average_quality': 0,
                    'most_common_emotion': None,
                    'improvement_trend': []
                }
            }
        
        # Add timestamp to submission
        submission_data['timestamp'] = datetime.now().isoformat()
        submission_data['submission_id'] = len(self.data[student_id]['submissions']) + 1
        
        # Append submission
        self.data[student_id]['submissions'].append(submission_data)
        
        # Update statistics
        self._update_statistics(student_id)
        
        # Save to file
        self._save_data()
    
    def _update_statistics(self, student_id):
        """Update aggregated statistics for a student"""
        submissions = self.data[student_id]['submissions']
        
        if not submissions:
            return
        
        # Total submissions
        self.data[student_id]['statistics']['total_submissions'] = len(submissions)
        
        # Average quality score
        quality_scores = [s.get('quality_metrics', {}).get('overall_score', 0) 
                         for s in submissions]
        if quality_scores:
            avg_quality = sum(quality_scores) / len(quality_scores)
            self.data[student_id]['statistics']['average_quality'] = round(avg_quality, 2)
        
        # Most common emotion
        emotions = [s.get('emotion', '') for s in submissions]
        if emotions:
            most_common = max(set(emotions), key=emotions.count)
            self.data[student_id]['statistics']['most_common_emotion'] = most_common
        
        # Improvement trend (last 5 submissions)
        recent_scores = quality_scores[-5:] if len(quality_scores) >= 5 else quality_scores
        if len(recent_scores) > 1:
            trend = "improving" if recent_scores[-1] > recent_scores[0] else "declining"
            self.data[student_id]['statistics']['improvement_trend'] = trend
    
    def get_student_history(self, student_id, limit=None):
        """
        Get submission history for a student
        
        Args:
            student_id: Student identifier
            limit: Maximum number of submissions to return (most recent)
            
        Returns:
            List of submissions
        """
        if student_id not in self.data:
            return []
        
        submissions = self.data[student_id]['submissions']
        
        if limit:
            return submissions[-limit:]
        return submissions
    
    def get_student_statistics(self, student_id):
        """Get aggregated statistics for a student"""
        if student_id not in self.data:
            return None
        
        return self.data[student_id]['statistics']
    
    def get_progress_summary(self, student_id):
        """
        Get a comprehensive progress summary
        
        Returns:
            Dict with various progress metrics and visualizations data
        """
        if student_id not in self.data:
            return None
        
        submissions = self.data[student_id]['submissions']
        
        if not submissions:
            return None
        
        # Emotion distribution
        emotions = [s.get('emotion', '') for s in submissions]
        emotion_counts = {}
        for emotion in emotions:
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
        
        # Quality progression
        quality_progression = [
            {
                'submission_id': s.get('submission_id', i+1),
                'score': s.get('quality_metrics', {}).get('overall_score', 0),
                'date': s.get('timestamp', '')[:10]  # Just the date
            }
            for i, s in enumerate(submissions)
        ]
        
        # Topic distribution
        topics = [s.get('topic', {}).get('primary_topic', 'Unknown') for s in submissions]
        topic_counts = {}
        for topic in topics:
            topic_counts[topic] = topic_counts.get(topic, 0) + 1
        
        return {
            'total_submissions': len(submissions),
            'statistics': self.data[student_id]['statistics'],
            'emotion_distribution': emotion_counts,
            'quality_progression': quality_progression,
            'topic_distribution': topic_counts,
            'latest_submission': submissions[-1],
            'first_submission_date': submissions[0].get('timestamp', '')[:10],
            'latest_submission_date': submissions[-1].get('timestamp', '')[:10]
        }
    
    def delete_student_data(self, student_id):
        """Delete all data for a student"""
        if student_id in self.data:
            del self.data[student_id]
            self._save_data()
            return True
        return False
    
    def get_all_students(self):
        """Get list of all student IDs"""
        return list(self.data.keys())
