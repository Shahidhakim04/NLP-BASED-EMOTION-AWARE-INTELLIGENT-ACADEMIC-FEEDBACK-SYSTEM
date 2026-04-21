"""
Advanced Quality Analyzer
Provides multi-dimensional quality analysis of academic answers
"""

import re
from textstat import textstat

class AdvancedQualityAnalyzer:
    def __init__(self):
        self.weights = {
            'length': 0.2,
            'complexity': 0.25,
            'vocabulary': 0.25,
            'readability': 0.15,
            'structure': 0.15
        }
    
    def analyze_quality(self, answer):
        """
        Perform comprehensive quality analysis
        Returns detailed metrics and overall score
        """
        metrics = {
            'length_score': self._analyze_length(answer),
            'complexity_score': self._analyze_complexity(answer),
            'vocabulary_score': self._analyze_vocabulary(answer),
            'readability_score': self._analyze_readability(answer),
            'structure_score': self._analyze_structure(answer),
        }
        
        # Calculate overall score (0-100)
        overall = sum(metrics[key] * self.weights[key.replace('_score', '')] 
                      for key in metrics.keys())
        
        metrics['overall_score'] = round(overall, 2)
        metrics['quality_level'] = self._get_quality_level(overall)
        metrics['word_count'] = len(answer.split())
        metrics['sentence_count'] = len(self._get_sentences(answer))
        
        return metrics
    
    def _analyze_length(self, text):
        """Score based on answer length (words)"""
        words = len(text.split())
        
        if words < 20:
            return 20  # Too short
        elif words < 50:
            return 50  # Below average
        elif words < 100:
            return 75  # Good
        elif words < 200:
            return 90  # Very good
        else:
            return 100  # Excellent
    
    def _analyze_complexity(self, text):
        """Analyze sentence complexity and structure"""
        sentences = self._get_sentences(text)
        
        if not sentences:
            return 0
        
        # Average words per sentence
        words = text.split()
        avg_sentence_length = len(words) / len(sentences)
        
        # Score based on complexity
        if avg_sentence_length < 8:
            complexity = 40  # Too simple
        elif avg_sentence_length < 15:
            complexity = 70  # Good
        elif avg_sentence_length < 25:
            complexity = 90  # Very good
        else:
            complexity = 75  # Maybe too complex
        
        return complexity
    
    def _analyze_vocabulary(self, text):
        """Analyze vocabulary richness (unique words ratio)"""
        words = text.lower().split()
        
        if len(words) == 0:
            return 0
        
        # Calculate lexical diversity
        unique_words = len(set(words))
        total_words = len(words)
        diversity_ratio = unique_words / total_words
        
        # Score: higher diversity = better vocabulary
        score = min(100, diversity_ratio * 120)  # Scale appropriately
        
        return round(score, 2)
    
    def _analyze_readability(self, text):
        """Analyze text readability using Flesch Reading Ease"""
        try:
            # Flesch Reading Ease (0-100, higher is easier)
            flesch_score = textstat.flesch_reading_ease(text)
            
            # Convert to 0-100 quality score
            # Target: 60-70 (standard/fairly easy) is ideal for academic writing
            if flesch_score < 30:
                score = 50  # Very difficult
            elif flesch_score < 50:
                score = 70  # Difficult but acceptable
            elif flesch_score < 70:
                score = 90  # Good academic level
            elif flesch_score < 80:
                score = 85  # Fairly easy
            else:
                score = 70  # Too simple for academic
            
            return score
        except:
            return 50  # Default if calculation fails
    
    def _analyze_structure(self, text):
        """Analyze answer structure and organization"""
        score = 0
        
        # Check for paragraphs (multiple line breaks)
        paragraphs = len(text.split('\n\n'))
        if paragraphs > 1:
            score += 30
        
        # Check for proper capitalization
        sentences = self._get_sentences(text)
        capitalized = sum(1 for s in sentences if s and s[0].isupper())
        if sentences and (capitalized / len(sentences)) > 0.7:
            score += 25
        
        # Check for punctuation usage
        punctuation_count = sum(1 for char in text if char in '.!?,;:')
        if punctuation_count > 2:
            score += 25
        
        # Check for transitional words/phrases
        transitions = ['however', 'therefore', 'furthermore', 'moreover', 
                      'consequently', 'additionally', 'for example', 'in conclusion']
        if any(trans in text.lower() for trans in transitions):
            score += 20
        
        return min(100, score)
    
    def _get_sentences(self, text):
        """Split text into sentences"""
        # Simple sentence splitter
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def _get_quality_level(self, score):
        """Convert numeric score to quality level"""
        if score < 40:
            return 'poor'
        elif score < 60:
            return 'below_average'
        elif score < 75:
            return 'average'
        elif score < 85:
            return 'good'
        else:
            return 'excellent'

# Backward compatibility function
def analyze_quality(answer):
    """Simple function that returns just the quality level (for existing code)"""
    analyzer = AdvancedQualityAnalyzer()
    result = analyzer.analyze_quality(answer)
    return result['quality_level']
