# 🎓 Advanced Emotion-Aware Academic Feedback System

## Overview
An intelligent academic feedback system that analyzes student responses using Natural Language Processing (NLP), emotion detection, and multi-dimensional quality assessment to provide personalized, constructive feedback.

## ✨ Key Features

### Core Features
- **Emotion Detection**: Identifies emotions (joy, sadness, fear, anger, etc.) in student responses
- **Multi-Dimensional Quality Analysis**: 
  - Length assessment
  - Complexity evaluation
  - Vocabulary richness
  - Readability scoring
  - Structure analysis
- **Topic Detection**: Automatically identifies the academic subject
- **Enhanced Feedback**: Context-aware, personalized feedback generation
- **Progress Tracking**: Stores submission history and tracks improvement over time

### Advanced Features
- **Multi-Emotion Visualization**: Shows distribution of all detected emotions
- **Quality Breakdown**: Detailed metrics across 5 dimensions
- **Progress Dashboard**: Visual analytics with charts and graphs
- **Session-Based Tracking**: Tracks individual student progress
- **Real-Time Character/Word Counter**: Helps students meet length requirements

## 🛠️ Technology Stack

### Backend
- **Flask**: Web framework
- **Transformers (Hugging Face)**: Emotion detection models
- **TextStat**: Readability analysis
- **NLTK**: Natural language processing
- **scikit-learn**: Machine learning utilities

### Frontend
- **HTML5/CSS3**: Modern, responsive design
- **JavaScript**: Interactive features
- **Chart.js**: Data visualization
- **Google Fonts (Poppins)**: Clean typography

### AI/ML Models
- **j-hartmann/emotion-english-distilroberta-base**: Emotion classification
- **Custom quality analyzer**: Multi-dimensional assessment
- **Keyword-based topic detection**: Fast academic subject identification

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd proj-2
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Download Required Models
```bash
python -c "from transformers import pipeline; pipeline('text-classification', model='j-hartmann/emotion-english-distilroberta-base')"
```

## 🚀 Running the Application

### Standard Version
```bash
python app.py
```

### Enhanced Version (Recommended)
```bash
python app_enhanced.py
```

The application will be available at: `http://localhost:5000`

## 📖 Usage Guide

### For Students

1. **Submit an Answer**
   - Navigate to the homepage
   - Type or paste your academic response in the text area
   - Click "Generate Intelligent Analysis"

2. **View Analysis Results**
   - Primary emotion detected
   - Confidence score
   - Detected academic topic
   - Overall quality score (0-100)
   - Detailed quality breakdown
   - Emotion distribution
   - Personalized feedback

3. **Track Progress**
   - Click "View Detailed Progress Dashboard"
   - See quality progression over time
   - View emotion distribution
   - Analyze topics covered

### For Developers

#### Project Structure
```
proj-2/
├── app.py                          # Original Flask app
├── app_enhanced.py                 # Enhanced version with all features
├── emotion_model.py                # Emotion detection
├── preprocess.py                   # Text preprocessing
├── quality_analyzer.py             # Simple quality analyzer
├── advanced_quality_analyzer.py    # Multi-dimensional quality analyzer
├── topic_detector.py               # Topic/subject detection
├── feedback_generator.py           # Basic feedback generation
├── enhanced_feedback_generator.py  # Advanced feedback generation
├── progress_tracker.py             # Progress tracking system
├── requirements.txt                # Python dependencies
├── templates/
│   ├── index.html                  # Original template
│   ├── index_enhanced.html         # Enhanced template
│   └── progress.html               # Progress dashboard
└── data/
    └── progress.json               # Stored progress data
```

#### Adding Custom Features

**Custom Emotion Responses**:
Edit `enhanced_feedback_generator.py`:
```python
emotion_openings = {
    "custom_emotion": {
        "high": "Your custom high-confidence message",
        "low": "Your custom low-confidence message"
    }
}
```

**Custom Topics**:
Edit `topic_detector.py`:
```python
ACADEMIC_TOPICS = [
    "Your Custom Topic",
    # Add more topics...
]
```

## 📊 Quality Metrics Explained

- **Length Score**: Based on word count (optimal: 50-200 words)
- **Complexity Score**: Sentence structure and variety
- **Vocabulary Score**: Lexical diversity (unique words ratio)
- **Readability Score**: Flesch Reading Ease score
- **Structure Score**: Organization, capitalization, punctuation

## 🎯 API Endpoints

### Main Routes
- `GET/POST /` - Main analysis page
- `GET /progress` - Progress dashboard
- `GET /api/progress` - JSON progress data
- `POST /reset-progress` - Clear progress data

## 🔧 Configuration

### Session Management
Edit `app_enhanced.py`:
```python
app.secret_key = 'your-secret-key-here'  # Change in production
```

### Data Storage
Progress data is stored in: `data/progress.json`

To change location:
```python
progress_tracker = ProgressTracker('custom/path/data.json')
```

## 🎨 Customization

### Themes & Styling
Edit CSS in template files:
- Primary colors: `#667eea`, `#764ba2`
- Change gradient backgrounds
- Modify card styles

### Feedback Messages
Customize feedback in `enhanced_feedback_generator.py`:
- Emotion-based openings
- Quality-based suggestions
- Encouraging conclusions

## 📈 Future Enhancements

Planned features:
- [ ] User authentication
- [ ] Database integration (PostgreSQL)
- [ ] Real-time collaborative features
- [ ] Export reports as PDF
- [ ] Teacher dashboard
- [ ] Comparative analysis with model answers
- [ ] Speech-to-text input
- [ ] Multi-language support
- [ ] Gamification (badges, points)
- [ ] Mobile app version

## 🐛 Troubleshooting

### Common Issues

**Issue**: Model download fails
```bash
# Solution: Manually download models
python -c "from transformers import pipeline; pipeline('text-classification', model='j-hartmann/emotion-english-distilroberta-base', revision='main')"
```

**Issue**: Import errors
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt --upgrade
```

**Issue**: Port already in use
```bash
# Solution: Use different port
python app_enhanced.py --port 5001
```

## 📝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is part of a Final Year B.Tech project.

## 👥 Authors

**Final Year B.Tech Students**
- Project: NLP & GenAI Based Intelligent Feedback System

## 🙏 Acknowledgments

- Hugging Face for transformer models
- Chart.js for visualization library
- Flask community
- All open-source contributors

## 📧 Contact

For questions or support, please open an issue in the repository.

---

**Project Status**: Active Development
**Version**: 2.0 (Enhanced)
**Last Updated**: February 2026
