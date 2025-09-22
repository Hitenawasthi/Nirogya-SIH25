"""
AI-Driven Public Health Chatbot
Smart India Hackathon 2025

This is a simple Flask backend that integrates with Google's Gemini AI
to provide health-related information and guidance to users.

Author: [Your Name]
Year: 1st Year B.Tech CSE
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
from werkzeug.utils import secure_filename
import base64

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Upload configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Configure Gemini AI
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY not found. Please set it in your .env file")
else:
    print(f"✅ GEMINI_API_KEY loaded: {GEMINI_API_KEY[:10]}...")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Health-focused system prompt
HEALTH_SYSTEM_PROMPT = """
You are an AI-powered Public Health Assistant designed to help with health-related questions and concerns.

RESPONSE FORMAT - ALWAYS USE THIS STRUCTURE:

**🔍 Quick Assessment:**
[Brief 1-2 sentence summary of the issue]

**📋 Key Points:**
• [Point 1]
• [Point 2] 
• [Point 3]

**💡 Recommendations:**
• [Action 1]
• [Action 2]
• [Action 3]

**⚠️ When to Seek Help:**
[Specific conditions that require medical attention]

**📝 Note:** [Brief medical disclaimer]

RESPONSE GUIDELINES:
- Keep each section concise (2-4 bullet points max)
- Use clear, simple language
- Support multiple languages - respond in user's language
- For non-health questions: "I'm a health assistant and can only help with health-related questions. Please ask me about symptoms, medications, treatments, or general health concerns."
- For serious symptoms, emphasize immediate medical attention
- Use emojis and formatting for better readability

LANGUAGE SUPPORT:
- Respond in the user's language when possible
- For medical terms, provide both local language and English when helpful

Remember: Structured, concise, and helpful responses only.
"""

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_medical_document(content, filename):
    """
    Use AI to determine if the uploaded document is medical-related
    """
    try:
        # Create a more comprehensive prompt for medical document detection
        medical_analysis_prompt = f"""
        You are a medical document classifier. Analyze the following document to determine if it's medical-related.
        
        Filename: {filename}
        Content: {content[:3000]}  # Increased content limit
        
        Medical documents include (but not limited to):
        - Prescriptions and medication lists
        - Lab reports and test results
        - Medical certificates and health records
        - Doctor's notes and consultation reports
        - Medical imaging reports (X-ray, MRI, CT scan reports)
        - Health insurance documents
        - Vaccination records
        - Discharge summaries
        - Medical bills and invoices
        - Health checkup reports
        - Emergency medical records
        - Any document containing medical terminology, patient information, or health data
        
        IMPORTANT: Be liberal in your assessment. If there's ANY medical content, health information, or medical terminology, classify it as medical.
        
        Respond with ONLY "YES" if this is a medical document.
        Respond with ONLY "NO" if this is clearly not a medical document.
        
        Consider documents in any language - medical terms are often similar across languages.
        """
        
        response = model.generate_content(medical_analysis_prompt)
        result = response.text.strip().upper()
        
        # More flexible matching
        return "YES" in result or result == "YES"
        
    except Exception as e:
        print(f"Error in medical document analysis: {str(e)}")
        return False

def analyze_medical_document(content, filename):
    """
    Analyze medical document content using AI with structured analysis
    """
    try:
        analysis_prompt = f"""
        You are an expert medical AI assistant. Analyze this medical document and provide a structured summary.
        
        Filename: {filename}
        Document Content: {content[:4000]}
        
        RESPONSE FORMAT - ALWAYS USE THIS STRUCTURE:
        
        **📄 Document Type:**
        [Type of medical document - prescription, lab report, etc.]
        
        **👤 Patient Information:**
        • [Patient details if mentioned]
        • [Date of document]
        • [Doctor/Facility name]
        
        **🔬 Key Findings:**
        • [Finding 1]
        • [Finding 2]
        • [Finding 3]
        
        **💊 Medications/Treatments:**
        • [Medication 1 with dosage]
        • [Medication 2 with dosage]
        • [Treatment recommendations]
        
        **📅 Follow-up Instructions:**
        • [Next appointment]
        • [Follow-up tests]
        • [Important reminders]
        
        **⚠️ Important Notes:**
        [Any urgent matters or warnings]
        
        **📝 Disclaimer:**
        This analysis is for informational purposes only. Please consult your healthcare provider for medical advice.
        
        GUIDELINES:
        - Keep each section concise (2-4 bullet points max)
        - Use clear, simple language
        - Highlight any concerning findings
        - If document is in another language, provide analysis in that language
        - If you cannot read certain parts, mention what you can and cannot analyze
        """
        
        response = model.generate_content(analysis_prompt)
        return response.text if response.text else "Unable to analyze the document. Please ensure the document is clear and readable."
        
    except Exception as e:
        print(f"Error in document analysis: {str(e)}")
        return "Error analyzing the document. Please try again or ensure the file is properly formatted."

@app.route('/')
def home():
    """Serve the home page with project information"""
    return render_template('home.html')

@app.route('/chat')
def chat_interface():
    """Serve the main chat interface"""
    return render_template('index.html')

@app.route('/about')
def about():
    """Serve the about us page"""
    return render_template('about.html')

@app.route('/doctors')
def doctors():
    """Serve the doctors page"""
    return render_template('doctors.html')

@app.route('/hospitals')
def hospitals():
    """Serve the hospitals page"""
    return render_template('hospitals.html')


@app.route('/api/upload', methods=['POST'])
def upload_file():
    """
    Handle file uploads and analyze medical documents
    """
    try:
        # Check if file is present
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided', 'status': 'error'}), 400
        
        file = request.files['file']
        
        # Check if file is selected
        if file.filename == '':
            return jsonify({'error': 'No file selected', 'status': 'error'}), 400
        
        # Check file extension
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Please upload PDF, JPG, PNG, or DOC files.', 'status': 'error'}), 400
        
        # Secure filename and save file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        print(f"File uploaded: {filename}")
        
        # Extract content from the uploaded file
        file_extension = filename.rsplit('.', 1)[1].lower()
        document_content = ""
        
        try:
            if file_extension == 'pdf':
                # For PDFs, we'll read the file and create a basic content representation
                # In a full implementation, you'd use PyPDF2, pdfplumber, or similar
                with open(filepath, 'rb') as file:
                    file_data = file.read()
                    # Create a content representation for AI analysis
                    document_content = f"PDF Document: {filename}\nFile size: {len(file_data)} bytes\n[PDF content would be extracted here in full implementation]"
            elif file_extension in ['jpg', 'jpeg', 'png']:
                # For images, we'll create a representation
                # In a full implementation, you'd use OCR (tesseract) to extract text
                with open(filepath, 'rb') as file:
                    file_data = file.read()
                    document_content = f"Image Document: {filename}\nFile size: {len(file_data)} bytes\n[Image content would be analyzed with OCR in full implementation]"
            elif file_extension in ['doc', 'docx']:
                # For Word documents
                # In a full implementation, you'd use python-docx
                with open(filepath, 'rb') as file:
                    file_data = file.read()
                    document_content = f"Word Document: {filename}\nFile size: {len(file_data)} bytes\n[Word document content would be extracted here in full implementation]"
            else:
                document_content = f"Document: {filename}\nFile type: {file_extension}"
                
        except Exception as e:
            print(f"Error reading file content: {str(e)}")
            document_content = f"Document: {filename}\n[Error reading file content]"
        
        # Check if it's a medical document
        is_medical = is_medical_document(document_content, filename)
        
        if is_medical:
            # Analyze the medical document
            analysis = analyze_medical_document(document_content, filename)
            
            # Clean up uploaded file
            try:
                os.remove(filepath)
            except:
                pass
            
            return jsonify({
                'status': 'success',
                'is_medical': True,
                'analysis': analysis,
                'filename': filename
            })
        else:
            # Clean up uploaded file
            try:
                os.remove(filepath)
            except:
                pass
            
            return jsonify({
                'status': 'success',
                'is_medical': False,
                'message': 'This document does not appear to be medical-related.'
            })
            
    except Exception as e:
        print(f"Upload error: {str(e)}")
        return jsonify({
            'error': f'Upload failed: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/api/chat', methods=['POST'])
def chat_api():
    """
    Handle chat messages from the frontend
    Processes health-related queries using Gemini AI
    """
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        
        # Create the full prompt with system context
        full_prompt = f"{HEALTH_SYSTEM_PROMPT}\n\nUser Question: {user_message}"
        
        # Generate response using Gemini
        response = model.generate_content(full_prompt)
        
        # Extract the response text
        bot_response = response.text if response.text else "I'm sorry, I couldn't generate a response. Please try again."
        
        return jsonify({
            'response': bot_response,
            'status': 'success'
        })
        
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        print(f"Error type: {type(e)}")
        return jsonify({
            'error': f'Sorry, there was an error processing your request: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'AI Public Health Chatbot is running!',
        'version': '1.0.0'
    })

@app.route('/api/suggestions', methods=['GET'])
def get_suggestions():
    """Get common health topics for quick suggestions"""
    suggestions = [
        "What are the symptoms of common cold?",
        "How to prevent seasonal flu?",
        "What should I do for a headache?",
        "How to maintain good mental health?",
        "What are the benefits of regular exercise?",
        "How to improve sleep quality?",
        "What foods boost immunity?",
        "How to manage stress effectively?"
    ]
    return jsonify({'suggestions': suggestions})

if __name__ == '__main__':
    print("🏥 AI-Driven Public Health Chatbot Starting...")
    print("📱 Access the chatbot at: http://localhost:5001")
    print("🔧 Make sure to set your GEMINI_API_KEY in .env file")
    app.run(debug=True, host='0.0.0.0', port=5001)
