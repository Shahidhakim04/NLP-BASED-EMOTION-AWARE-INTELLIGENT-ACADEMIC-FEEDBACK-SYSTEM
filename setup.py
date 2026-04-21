"""
Automated Setup Script for Enhanced Emotion-Aware Feedback System
Run this script to automatically set up the entire system
"""

import os
import sys
import subprocess

def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"⏳ {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✅ {description} - Success!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Failed!")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {version.major}.{version.minor}")
        sys.exit(1)
    print(f"✅ Python {version.major}.{version.minor} detected")

def create_directories():
    """Create necessary directories"""
    directories = ['data', 'logs']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Created directory: {directory}")
        else:
            print(f"ℹ️  Directory already exists: {directory}")

def install_dependencies():
    """Install Python dependencies"""
    print_header("Installing Python Dependencies")
    
    packages = [
        "Flask==3.0.0",
        "transformers==4.35.0",
        "torch==2.1.0",
        "nltk==3.8.1",
        "textstat==0.7.3",
        "scikit-learn==1.3.2",
        "Werkzeug==3.0.1"
    ]
    
    for package in packages:
        run_command(f"pip install {package}", f"Installing {package}")

def download_nltk_data():
    """Download required NLTK data"""
    print_header("Downloading NLTK Data")
    
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        print("✅ NLTK data downloaded successfully")
    except Exception as e:
        print(f"❌ Failed to download NLTK data: {e}")

def download_models():
    """Download transformer models"""
    print_header("Downloading AI Models")
    
    print("⏳ Downloading emotion detection model (this may take a few minutes)...")
    try:
        from transformers import pipeline
        pipeline('text-classification', 
                model='j-hartmann/emotion-english-distilroberta-base')
        print("✅ Emotion detection model downloaded successfully")
    except Exception as e:
        print(f"❌ Failed to download model: {e}")
        print("You can try downloading manually later.")

def test_imports():
    """Test if all required modules can be imported"""
    print_header("Testing Module Imports")
    
    modules = [
        'flask',
        'transformers',
        'torch',
        'nltk',
        'textstat',
        'sklearn'
    ]
    
    all_success = True
    for module in modules:
        try:
            __import__(module)
            print(f"✅ {module} - OK")
        except ImportError:
            print(f"❌ {module} - Failed to import")
            all_success = False
    
    return all_success

def create_test_file():
    """Create a simple test script"""
    test_script = """
# Quick Test Script
from emotion_model import detect_emotion
from advanced_quality_analyzer import AdvancedQualityAnalyzer

print("Testing emotion detection...")
result = detect_emotion("I love learning about artificial intelligence!")
print(f"Emotion detected: {result[0]['label']}")

print("\\nTesting quality analyzer...")
analyzer = AdvancedQualityAnalyzer()
result = analyzer.analyze_quality("This is a test answer with sufficient length and structure.")
print(f"Quality score: {result['overall_score']}")

print("\\n✅ All tests passed!")
"""
    
    with open('test_system.py', 'w') as f:
        f.write(test_script)
    
    print("✅ Created test script: test_system.py")

def main():
    """Main setup function"""
    print_header("Enhanced Emotion-Aware Feedback System Setup")
    
    # Step 1: Check Python version
    print_header("Step 1: Checking Python Version")
    check_python_version()
    
    # Step 2: Create directories
    print_header("Step 2: Creating Directories")
    create_directories()
    
    # Step 3: Install dependencies
    install_dependencies()
    
    # Step 4: Download NLTK data
    download_nltk_data()
    
    # Step 5: Download models
    download_models()
    
    # Step 6: Test imports
    if not test_imports():
        print("\n⚠️  Some modules failed to import. Please check the errors above.")
        print("You may need to reinstall dependencies manually.")
    
    # Step 7: Create test file
    print_header("Creating Test Files")
    create_test_file()
    
    # Final message
    print_header("Setup Complete!")
    print("""
✅ Setup completed successfully!

Next steps:
1. Run the application:
   python app_enhanced.py

2. Open your browser and navigate to:
   http://localhost:5000

3. (Optional) Run tests:
   python test_system.py

For more information, see:
- README.md - Project documentation
- SETUP_GUIDE.md - Detailed setup instructions

Need help? Contact the development team.
    """)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Setup failed with error: {e}")
        sys.exit(1)
