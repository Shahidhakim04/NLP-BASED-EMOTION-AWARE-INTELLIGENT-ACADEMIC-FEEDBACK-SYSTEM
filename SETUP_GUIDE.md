# 🚀 Complete Setup Guide

## Quick Start (5 Minutes)

### Option 1: Automatic Setup (Recommended)
```bash
# Run the setup script
python setup.py
```

### Option 2: Manual Setup

#### Step 1: Install Python Dependencies
```bash
pip install Flask==3.0.0
pip install transformers==4.35.0
pip install torch==2.1.0
pip install nltk==3.8.1
pip install textstat==0.7.3
pip install scikit-learn==1.3.2
pip install Werkzeug==3.0.1
```

#### Step 2: Download NLTK Data
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

#### Step 3: Download Transformer Model
```python
from transformers import pipeline
pipeline('text-classification', model='j-hartmann/emotion-english-distilroberta-base')
```

#### Step 4: Create Data Directory
```bash
mkdir -p data
```

#### Step 5: Run the Application
```bash
# Run enhanced version
python app_enhanced.py

# Or run standard version
python app.py
```

#### Step 6: Access the Application
Open browser and navigate to: `http://localhost:5000`

## 📋 Detailed Installation Instructions

### For Windows

1. **Install Python**
   - Download from https://python.org
   - Check "Add Python to PATH" during installation
   - Verify: `python --version`

2. **Install Dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Run Application**
   ```cmd
   python app_enhanced.py
   ```

### For macOS

1. **Install Python**
   ```bash
   brew install python3
   ```

2. **Install Dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Run Application**
   ```bash
   python3 app_enhanced.py
   ```

### For Linux (Ubuntu/Debian)

1. **Install Python and pip**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Install Dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Run Application**
   ```bash
   python3 app_enhanced.py
   ```

## 🔧 Configuration Options

### Change Port
```python
# In app_enhanced.py, modify:
app.run(debug=True, host='0.0.0.0', port=8080)  # Change port to 8080
```

### Enable/Disable Debug Mode
```python
# Production:
app.run(debug=False)

# Development:
app.run(debug=True)
```

### Change Data Storage Location
```python
# In app_enhanced.py:
progress_tracker = ProgressTracker('custom/path/progress.json')
```

## 🌐 Deployment

### Deploy on Local Network

1. Find your IP address:
   ```bash
   # Windows
   ipconfig
   
   # Mac/Linux
   ifconfig
   ```

2. Run with network access:
   ```python
   app.run(host='0.0.0.0', port=5000)
   ```

3. Access from other devices:
   ```
   http://YOUR_IP_ADDRESS:5000
   ```

### Deploy on Cloud (Heroku Example)

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: python app_enhanced.py
   ```
3. Deploy:
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

### Deploy with Docker

1. Create `Dockerfile`:
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["python", "app_enhanced.py"]
   ```

2. Build and run:
   ```bash
   docker build -t feedback-system .
   docker run -p 5000:5000 feedback-system
   ```

## 🧪 Testing

### Test Basic Functionality
```bash
# Run test script
python test_system.py
```

### Test Individual Components
```python
# Test emotion detection
from emotion_model import detect_emotion
result = detect_emotion("I love learning about AI!")
print(result)

# Test quality analyzer
from advanced_quality_analyzer import AdvancedQualityAnalyzer
analyzer = AdvancedQualityAnalyzer()
result = analyzer.analyze_quality("Your test answer here...")
print(result)
```

## ⚡ Performance Optimization

### 1. Use GPU for Faster Inference
```bash
# Install PyTorch with CUDA
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 2. Cache Model Loading
Models are automatically cached after first load.

### 3. Reduce Model Size
Use quantized models for faster inference:
```python
model = pipeline('text-classification', 
                model='j-hartmann/emotion-english-distilroberta-base',
                device=-1)  # Use CPU
```

## 🔒 Security Considerations

### Production Deployment

1. **Change Secret Key**
   ```python
   import secrets
   app.secret_key = secrets.token_hex(16)
   ```

2. **Disable Debug Mode**
   ```python
   app.run(debug=False)
   ```

3. **Use Environment Variables**
   ```python
   import os
   app.secret_key = os.environ.get('SECRET_KEY')
   ```

4. **Set Up HTTPS**
   Use reverse proxy (Nginx) with SSL certificate

## 📊 Database Setup (Optional)

For production, replace JSON storage with database:

### PostgreSQL Setup
```bash
pip install psycopg2-binary
```

```python
# Create database connection
import psycopg2
conn = psycopg2.connect(
    dbname="feedback_db",
    user="your_user",
    password="your_password",
    host="localhost"
)
```

## 🐛 Common Issues & Solutions

### Issue: "Module not found"
**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

### Issue: "Port already in use"
**Solution:**
```bash
# Kill process on port 5000
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:5000 | xargs kill -9
```

### Issue: "Model download timeout"
**Solution:**
```python
# Set longer timeout
from transformers import pipeline
pipeline('text-classification', 
        model='j-hartmann/emotion-english-distilroberta-base',
        use_fast=True,
        timeout=300)
```

### Issue: "Memory error"
**Solution:**
- Use smaller batch sizes
- Close other applications
- Use CPU instead of GPU

## 📞 Getting Help

If you encounter issues:

1. Check the [README.md](README.md)
2. Review error messages carefully
3. Search for similar issues online
4. Contact the development team

## ✅ Verification Checklist

- [ ] Python 3.8+ installed
- [ ] All dependencies installed
- [ ] Models downloaded successfully
- [ ] Data directory created
- [ ] Application runs without errors
- [ ] Can access at http://localhost:5000
- [ ] Emotion detection works
- [ ] Quality analysis works
- [ ] Progress tracking works
- [ ] Feedback generation works

## 🎉 You're Ready!

If all checks pass, your system is ready to use. Start analyzing academic responses and providing intelligent feedback!

---

**Need Help?** Open an issue or contact the development team.
