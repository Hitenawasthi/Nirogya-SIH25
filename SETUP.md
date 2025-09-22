# 🚀 Quick Setup Guide - AI Public Health Chatbot

## 📋 Prerequisites Checklist

Before you start, make sure you have:

- [ ] Python 3.7 or higher installed
- [ ] Internet connection
- [ ] Google account (for Gemini API)
- [ ] Text editor or IDE (VS Code recommended)

## ⚡ 5-Minute Setup

### Step 1: Install Dependencies
```bash
# Navigate to your project folder
cd hackathon2.0

# Install required packages
pip install -r requirements.txt
```

### Step 2: Get Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key

### Step 3: Configure Environment
```bash
# Create .env file
cp env_example.txt .env

# Edit .env file and add your API key
# Replace 'your_gemini_api_key_here' with your actual key
GEMINI_API_KEY=your_actual_api_key_here
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Open in Browser
- Go to `http://localhost:5000`
- Start chatting with your AI health assistant!

## 🔧 Troubleshooting

### Common Issues

**Issue**: "GEMINI_API_KEY not found"
- **Solution**: Make sure you created the `.env` file and added your API key

**Issue**: "Module not found" errors
- **Solution**: Run `pip install -r requirements.txt` again

**Issue**: Port 5000 already in use
- **Solution**: Change the port in `app.py` (line 95) to a different number like 5001

**Issue**: API key not working
- **Solution**: 
  1. Check if you copied the key correctly
  2. Make sure there are no extra spaces
  3. Verify the key is active in Google AI Studio

### Testing the Setup

1. **Check Backend**: Visit `http://localhost:5000/api/health`
   - Should return: `{"status": "healthy", "message": "AI Public Health Chatbot is running!"}`

2. **Test Chat**: Try asking "What are the symptoms of common cold?"
   - Should get an AI response about cold symptoms

3. **Check Mobile**: Open on your phone's browser
   - Should look great on mobile too!

## 🎯 Ready for Demo!

Once everything is working:
- ✅ Beautiful interface loads
- ✅ Can send messages
- ✅ AI responds with health information
- ✅ Works on mobile
- ✅ Quick suggestions work

**You're ready to impress the judges! 🏆**

## 📱 Demo Tips

### What to Show Judges
1. **Welcome Screen**: Beautiful design with quick suggestions
2. **Chat Functionality**: Ask health questions and get AI responses
3. **Mobile Responsiveness**: Show it works on phone
4. **Professional Look**: Clean, modern interface
5. **Real-time Interaction**: Typing indicators, smooth animations

### Sample Questions to Demo
- "What should I do for a headache?"
- "How can I prevent seasonal flu?"
- "What are the benefits of regular exercise?"
- "How to improve sleep quality?"

## 🆘 Need Help?

If you run into any issues:
1. Check the console for error messages
2. Verify your API key is correct
3. Make sure all dependencies are installed
4. Try restarting the application

**Good luck with your hackathon! 🚀**
