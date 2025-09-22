# Nirogya - AI Public Health Platform
## Complete Software Flow Chart

### Overview
This document outlines the complete flow of the Nirogya AI Public Health Platform, from user interaction to AI response and data processing.

---

## 🏠 **1. HOMEPAGE FLOW**

```
User Visits Homepage (/)
    ↓
Modern Header with Navigation
    ↓
Hero Section with "Start AI Analysis" Button
    ↓
User Clicks "Start AI Analysis"
    ↓
AI Analysis Modal Opens
    ↓
Registration Form Appears
    ↓
User Fills Registration Form
    ↓
Registration Success → Auto-redirect to Chat
```

---

## 👤 **2. USER REGISTRATION FLOW**

```
Registration Form Display
    ↓
User Inputs:
- Full Name
- Age
- Email
- Phone
- Medical History
- Emergency Contact
    ↓
Form Validation (Client-side)
    ↓
Data Stored in sessionStorage
    ↓
Success Message Display
    ↓
Auto-redirect to /chat (2 seconds)
```

---

## 💬 **3. CHAT INTERFACE FLOW**

```
User Lands on Chat Page (/chat)
    ↓
Check if User is Logged In
    ↓
If NOT Logged In → Show Login Prompt Modal
    ↓
If Logged In → Display Chat Interface
    ↓
Chat Interface Components:
- Health Dashboard Sidebar
- Chat Messages Area
- Input Field with Send Button
- Attachment Button
```

---

## 🤖 **4. AI CHAT PROCESSING FLOW**

```
User Types Message in Chat
    ↓
Client-side Validation
    ↓
Send Message to /api/chat (POST)
    ↓
Flask Backend Receives Request
    ↓
Extract User Message from JSON
    ↓
Create Full Prompt with System Context
    ↓
Send to Gemini AI (gemini-1.5-flash)
    ↓
AI Processes Health Query
    ↓
AI Returns Structured Response
    ↓
Flask Returns JSON Response
    ↓
Frontend Receives Response
    ↓
Format Response (Markdown → HTML)
    ↓
Display in Chat Interface
```

---

## 📎 **5. FILE UPLOAD FLOW**

```
User Clicks Attachment Button
    ↓
File Selection Dialog Opens
    ↓
User Selects Medical Document
    ↓
Client-side Validation:
- File Type (PDF, JPG, PNG, DOC, DOCX)
- File Size (Max 10MB)
    ↓
Show Upload Progress Message
    ↓
Send File to /api/upload (POST)
    ↓
Flask Backend Receives File
    ↓
Secure Filename and Save
    ↓
Extract Content from File
    ↓
AI Medical Document Classification
    ↓
If Medical Document:
    ↓
AI Document Analysis
    ↓
Return Structured Analysis
    ↓
If NOT Medical:
    ↓
Return Rejection Message
    ↓
Clean Up Uploaded File
    ↓
Frontend Displays Result
```

---

## 🏥 **6. DOCTOR CONNECTION FLOW**

```
User Visits /doctors
    ↓
Display Doctor Search Interface
    ↓
User Can:
- Search by Name/Specialty/Location
- Filter by Medical Specialty
- View Doctor Profiles
    ↓
User Clicks "Connect Now"
    ↓
Show Connection Modal
    ↓
Redirect to Video Call (Future Feature)
```

---

## 🏥 **7. HOSPITAL SEARCH FLOW**

```
User Visits /hospitals
    ↓
Display Hospital Search Interface
    ↓
User Can:
- Search by Name/Location/Specialty
- Filter by Hospital Type
- View Hospital Details
    ↓
User Clicks "Contact" or "Directions"
    ↓
Show Contact/Directions Modal
    ↓
Redirect to Phone/Maps (Future Feature)
```

---

## 🔧 **8. BACKEND PROCESSING FLOW**

### **Flask Application Structure:**
```
app.py (Main Flask Application)
    ↓
Routes:
- / (Homepage)
- /chat (Chat Interface)
- /doctors (Doctor Search)
- /hospitals (Hospital Search)
- /about (About & Contact)
- /api/chat (Chat API)
- /api/upload (File Upload API)
    ↓
AI Integration:
- Google Gemini API (gemini-1.5-flash)
- Medical Document Analysis
- Health Query Processing
    ↓
File Handling:
- Secure File Upload
- Content Extraction
- Temporary Storage
    ↓
Response Generation:
- Structured AI Responses
- Error Handling
- JSON API Responses
```

---

## 🧠 **9. AI PROCESSING FLOW**

### **Chat Query Processing:**
```
User Health Query
    ↓
System Prompt Application
    ↓
Gemini AI Processing
    ↓
Structured Response Generation:
- Quick Assessment
- Key Points
- Recommendations
- When to Seek Help
- Medical Disclaimer
    ↓
Response Formatting
    ↓
Return to User
```

### **Document Analysis Processing:**
```
Medical Document Upload
    ↓
Content Extraction
    ↓
AI Medical Classification
    ↓
If Medical Document:
    ↓
AI Document Analysis:
- Document Type
- Patient Information
- Key Findings
- Medications/Treatments
- Follow-up Instructions
- Important Notes
    ↓
Structured Analysis Return
    ↓
If NOT Medical:
    ↓
Rejection Message
```

---

## 📱 **10. FRONTEND COMPONENTS FLOW**

### **Homepage Components:**
```
Modern Header
    ↓
Hero Section
    ↓
AI Analysis Modal
    ↓
Registration Form
    ↓
SOS Button & Modal
    ↓
Footer
```

### **Chat Interface Components:**
```
Health Dashboard Sidebar
    ↓
Chat Header
    ↓
Chat Messages Container
    ↓
Typing Indicator
    ↓
Chat Input Container
    ↓
Attachment Button
    ↓
Send Button
```

### **Doctor/Hospital Pages:**
```
Search Interface
    ↓
Filter Buttons
    ↓
Results Grid
    ↓
Individual Cards
    ↓
Action Buttons
    ↓
Contact CTAs
```

---

## 🔄 **11. DATA FLOW DIAGRAM**

```
User Input
    ↓
Client-side Validation
    ↓
HTTP Request (POST/GET)
    ↓
Flask Backend
    ↓
AI Processing (Gemini)
    ↓
Response Generation
    ↓
JSON Response
    ↓
Frontend Processing
    ↓
UI Update
    ↓
User Feedback
```

---

## 🛡️ **12. SECURITY & VALIDATION FLOW**

```
User Input
    ↓
Client-side Validation
    ↓
Server-side Validation
    ↓
File Security Check
    ↓
API Key Validation
    ↓
Rate Limiting
    ↓
Error Handling
    ↓
Secure Response
```

---

## 📊 **13. ERROR HANDLING FLOW**

```
Error Occurs
    ↓
Error Type Detection
    ↓
Log Error Details
    ↓
User-friendly Message
    ↓
Fallback Response
    ↓
Continue Operation
```

---

## 🎯 **14. COMPLETE USER JOURNEY**

```
1. User visits Homepage
2. Clicks "Start AI Analysis"
3. Fills Registration Form
4. Auto-redirects to Chat
5. Types Health Query
6. AI Processes & Responds
7. User can Upload Documents
8. AI Analyzes Medical Files
9. User can Search Doctors
10. User can Search Hospitals
11. User can Contact Support
```

---

## 🔧 **15. TECHNICAL STACK FLOW**

```
Frontend:
- HTML5/CSS3/JavaScript
- Font Awesome Icons
- Responsive Design
    ↓
Backend:
- Flask (Python)
- Google Gemini AI
- File Upload Handling
    ↓
AI Processing:
- gemini-1.5-flash Model
- Medical Document Analysis
- Health Query Processing
    ↓
Data Storage:
- Session Storage (Client)
- Temporary File Storage
- API Key Management
```

---

## 📈 **16. PERFORMANCE OPTIMIZATION FLOW**

```
User Request
    ↓
Client-side Caching
    ↓
Optimized API Calls
    ↓
Efficient File Processing
    ↓
Minimal AI Processing Time
    ↓
Fast Response Delivery
    ↓
Smooth User Experience
```

---

## 🎨 **17. UI/UX FLOW**

```
User Interaction
    ↓
Visual Feedback
    ↓
Loading States
    ↓
Smooth Animations
    ↓
Responsive Design
    ↓
Accessibility Features
    ↓
Professional Appearance
```

---

## 📋 **18. TESTING & VALIDATION FLOW**

```
Development
    ↓
Unit Testing
    ↓
Integration Testing
    ↓
User Acceptance Testing
    ↓
Performance Testing
    ↓
Security Testing
    ↓
Production Deployment
```

---

## 🚀 **19. DEPLOYMENT FLOW**

```
Code Development
    ↓
Version Control (Git)
    ↓
Testing & Validation
    ↓
Production Build
    ↓
Server Deployment
    ↓
Domain Configuration
    ↓
SSL Certificate
    ↓
Live Application
```

---

## 📞 **20. SUPPORT & MAINTENANCE FLOW**

```
User Support Request
    ↓
Issue Identification
    ↓
Technical Analysis
    ↓
Solution Implementation
    ↓
Testing & Validation
    ↓
Deployment
    ↓
User Notification
    ↓
Follow-up
```

---

## 🔮 **21. FUTURE ENHANCEMENTS FLOW**

```
User Feedback
    ↓
Feature Analysis
    ↓
Technical Planning
    ↓
Development
    ↓
Testing
    ↓
Deployment
    ↓
User Training
    ↓
Monitoring
```

---

## 📊 **22. ANALYTICS & MONITORING FLOW**

```
User Interactions
    ↓
Data Collection
    ↓
Analytics Processing
    ↓
Performance Metrics
    ↓
Usage Statistics
    ↓
Error Tracking
    ↓
Reporting
    ↓
Optimization
```

---

## 🎯 **SUMMARY**

The Nirogya AI Public Health Platform follows a comprehensive flow from user interaction to AI response, ensuring:

1. **User-Friendly Interface** - Simple, elegant, non-scrollable pages
2. **Secure Data Handling** - Proper validation and file security
3. **AI-Powered Processing** - Gemini AI for health queries and document analysis
4. **Professional Design** - Modern, responsive, accessible interface
5. **Comprehensive Features** - Chat, file upload, doctor search, hospital search
6. **Error Handling** - Robust error management and user feedback
7. **Performance Optimization** - Fast, efficient processing and response
8. **Scalable Architecture** - Modular design for future enhancements

This flowchart provides a complete overview of how the software works from end user to final response, making it perfect for hackathon judges to understand the system architecture and user journey.
