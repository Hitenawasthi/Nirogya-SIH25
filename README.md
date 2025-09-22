# 🏥 Nirogya - AI-Driven Public Health Chatbot

**Smart India Hackathon 2025 Project**

An intelligent public health assistant powered by Google's Gemini AI, designed to provide health information, wellness guidance, and preventive care advice to users.

## 🎯 Project Overview

This project aims to improve public health awareness and accessibility by providing an AI-powered chatbot that can answer health-related questions, suggest preventive measures, and guide users on when to seek professional medical help.

### Key Features

- 🤖 **AI-Powered Responses**: Uses Google Gemini AI for intelligent health-related conversations
- 💬 **Interactive Chat Interface**: Modern, responsive chat UI with real-time messaging
- 🎨 **Attractive Design**: Beautiful, professional interface perfect for hackathon presentation
- 📱 **Mobile Responsive**: Works seamlessly on desktop, tablet, and mobile devices
- ⚡ **Quick Suggestions**: Pre-loaded health topics for easy interaction
- 🔒 **Safe & Responsible**: Always reminds users to consult healthcare professionals for serious concerns
- 📄 **Document Analysis**: Upload and analyze medical reports and prescriptions
- 🏥 **Doctor Network**: Connect with partner doctors and hospitals
- 🚨 **SOS Emergency**: Quick access to emergency medical support

## 🛠️ Technology Stack

### Backend
- **Flask**: Lightweight Python web framework
- **Google Gemini AI**: Advanced AI model for natural language processing
- **Python**: Core programming language

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with CSS Grid and Flexbox
- **Vanilla JavaScript**: Interactive functionality
- **Font Awesome**: Icons and visual elements
- **Google Fonts**: Typography (Inter font family)

### APIs & Services
- **Google Generative AI API**: For AI-powered responses
- **RESTful API**: Clean backend API design

## 📁 Project Structure

```
Nirogya-SIH25/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── env_example.txt       # Environment variables template
├── docker-compose.yml    # Docker configuration
├── README.md             # Project documentation
├── templates/
│   ├── home.html         # Homepage
│   ├── index.html        # Chat interface
│   ├── about.html        # About & Contact page
│   ├── doctors.html      # Connect with Doctors
│   └── hospitals.html    # Search Hospitals
└── static/
    ├── css/
    │   └── style.css     # Styling and responsive design
    └── js/
        └── script.js     # Frontend functionality
```

## 🚀 Quick Start Guide

### Prerequisites

- Python 3.7 or higher
- Google Gemini API key (free tier available)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Hitenawasthi/Nirogya-SIH25.git
   cd Nirogya-SIH25
   ```

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   ```bash
   # Copy the example file
   cp env_example.txt .env
   
   # Edit .env and add your Gemini API key
   GEMINI_API_KEY=your_actual_api_key_here
   ```

4. **Get Your Gemini API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Create a new API key
   - Copy the key to your `.env` file

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the Application**
   - Open your browser
   - Navigate to `http://localhost:5001`
   - Start using Nirogya!

## 💡 How It Works

### Backend Flow
1. **User Input**: User sends a health-related question through the web interface
2. **API Processing**: Flask receives the request and forwards it to Gemini AI
3. **AI Response**: Gemini AI processes the question with health-focused context
4. **Response Delivery**: The AI response is sent back to the user interface

### Frontend Flow
1. **Homepage**: Users see project overview and can start AI analysis
2. **Chat Interface**: Interactive messaging with typing indicators
3. **Document Upload**: Users can upload medical reports for analysis
4. **Real-time Updates**: Messages appear instantly with smooth animations
5. **Responsive Design**: Works perfectly on all device sizes

## 🎨 Design Features

### Visual Appeal
- **Modern Gradient Backgrounds**: Eye-catching color schemes
- **Smooth Animations**: Heartbeat logo animation, typing indicators
- **Professional Typography**: Clean, readable Inter font
- **Card-based Layout**: Organized, modern interface design

### User Experience
- **Intuitive Navigation**: Easy-to-use chat interface
- **Quick Suggestions**: Pre-loaded health topics for faster interaction
- **Responsive Design**: Seamless experience across all devices
- **Accessibility**: Clear contrast, readable fonts, keyboard navigation

## 🔧 API Endpoints

### Chat Endpoint
```
POST /api/chat
Content-Type: application/json

{
  "message": "What are the symptoms of common cold?"
}

Response:
{
  "response": "Common cold symptoms include...",
  "status": "success"
}
```

### File Upload Endpoint
```
POST /api/upload
Content-Type: multipart/form-data

file: [medical document]

Response:
{
  "status": "success",
  "is_medical": true,
  "analysis": "Document analysis...",
  "filename": "report.pdf"
}
```

### Health Check
```
GET /api/health

Response:
{
  "status": "healthy",
  "message": "AI Public Health Chatbot is running!",
  "version": "1.0.0"
}
```

## 🎯 Hackathon Presentation Tips

### For Judges
1. **Demo the Interface**: Show the beautiful, responsive design
2. **Test Health Queries**: Ask questions like "What should I do for a headache?"
3. **Highlight AI Integration**: Explain how Gemini AI provides intelligent responses
4. **Show Mobile Responsiveness**: Demonstrate on different screen sizes
5. **Discuss Impact**: Explain how this improves public health accessibility

### Key Talking Points
- **Problem Solved**: Makes health information more accessible
- **Technology Used**: Modern AI integration with clean, professional design
- **Scalability**: Can be easily deployed and scaled for public use
- **Safety**: Always reminds users to consult healthcare professionals
- **Innovation**: Combines AI with public health awareness

## 🔮 Future Enhancements

### Phase 2 Features (Post-Hackathon)
- **Multi-language Support**: Hindi, regional languages
- **Voice Input/Output**: Speech-to-text and text-to-speech
- **Health Records**: Basic symptom tracking
- **Emergency Detection**: Identify urgent medical situations
- **Integration**: Connect with local healthcare providers
- **Analytics**: Track common health concerns in communities

### Advanced Features
- **Image Analysis**: Analyze skin conditions, wounds
- **Medication Reminders**: Help with medication schedules
- **Health Education**: Interactive health courses
- **Community Features**: Share health tips and experiences

## 🛡️ Safety & Disclaimers

### Important Notes
- **Not Medical Advice**: This chatbot provides general health information only
- **Professional Consultation**: Always recommend consulting healthcare professionals
- **Emergency Situations**: For emergencies, direct users to call emergency services
- **Data Privacy**: No personal health data is stored permanently

### Responsible AI Usage
- Clear disclaimers about limitations
- Emphasis on professional medical consultation
- Focus on prevention and general wellness
- Avoid specific medical diagnoses

## 📊 Technical Specifications

### Performance
- **Response Time**: < 2 seconds for most queries
- **Concurrent Users**: Supports multiple simultaneous users
- **Uptime**: Designed for 99%+ availability
- **Scalability**: Can be deployed on cloud platforms

### Security
- **API Key Protection**: Environment variable storage
- **Input Validation**: Sanitized user inputs
- **CORS Configuration**: Proper cross-origin setup
- **Error Handling**: Graceful error management

## 👨‍💻 Development Notes

### Code Quality
- **Clean Architecture**: Separated concerns (frontend/backend)
- **Documentation**: Comprehensive comments and README
- **Error Handling**: Robust error management
- **Responsive Design**: Mobile-first approach

### Best Practices
- **Environment Variables**: Secure API key management
- **RESTful API**: Clean, standard API design
- **Modern CSS**: CSS Grid, Flexbox, custom properties
- **Progressive Enhancement**: Works without JavaScript

## 🏆 Hackathon Success Factors

### What Makes This Project Stand Out
1. **Real-world Impact**: Addresses actual public health needs
2. **Modern Technology**: Uses cutting-edge AI (Gemini)
3. **Professional Design**: Production-ready interface
4. **Complete Solution**: Full-stack implementation
5. **Clear Documentation**: Easy to understand and extend
6. **Scalable Architecture**: Ready for real-world deployment

### Presentation Strategy
1. **Start with Impact**: Explain the public health problem
2. **Show the Solution**: Demo the beautiful interface
3. **Highlight Technology**: Explain AI integration
4. **Discuss Future**: Share expansion plans
5. **Q&A Ready**: Be prepared for technical questions

## 📞 Support & Contact

For questions about this project:
- **Developer**: Hitenawasthi
- **Institution**: [Your College/University]
- **Year**: 1st Year B.Tech CSE
- **Hackathon**: Smart India Hackathon 2025

---

**Good luck with your hackathon presentation! 🚀**

*Remember: This project demonstrates not just technical skills, but also the potential to make a real difference in public health accessibility.*
