/**
 * AI Public Health Chatbot - Frontend JavaScript
 * Smart India Hackathon 2025
 * 
 * This script handles the chat interface, API communication,
 * and user interactions for the health chatbot.
 */

class HealthChatbot {
    constructor() {
        this.chatMessages = document.getElementById('chatMessages');
        this.messageInput = document.getElementById('messageInput');
        this.sendButton = document.getElementById('sendButton');
        this.typingIndicator = document.getElementById('typingIndicator');
        this.welcomeSection = document.getElementById('welcomeSection'); // May not exist
        this.suggestionsGrid = document.getElementById('suggestionsGrid'); // May not exist
        
        this.isTyping = false;
        this.messageHistory = [];
        
        this.init();
    }
    
    init() {
        this.setupEventListeners();
        this.loadSuggestions();
        this.focusInput();
    }
    
    setupEventListeners() {
        // Send message on button click
        this.sendButton.addEventListener('click', () => this.sendMessage());
        
        // Send message on Enter key
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
        
        // Handle input changes
        this.messageInput.addEventListener('input', () => {
            this.updateSendButton();
        });
        
        // Prevent sending empty messages
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && this.messageInput.value.trim() === '') {
                e.preventDefault();
            }
        });
    }
    
    async loadSuggestions() {
        try {
            const response = await fetch('/api/suggestions');
            const data = await response.json();
            
            if (data.suggestions) {
                this.displaySuggestions(data.suggestions);
            }
        } catch (error) {
            console.error('Error loading suggestions:', error);
        }
    }
    
    displaySuggestions(suggestions) {
        if (!this.suggestionsGrid) {
            return; // Skip if suggestions grid doesn't exist
        }
        
        this.suggestionsGrid.innerHTML = '';
        
        suggestions.forEach(suggestion => {
            const suggestionElement = document.createElement('div');
            suggestionElement.className = 'suggestion-item';
            suggestionElement.textContent = suggestion;
            suggestionElement.addEventListener('click', () => {
                this.messageInput.value = suggestion;
                this.sendMessage();
            });
            
            this.suggestionsGrid.appendChild(suggestionElement);
        });
    }
    
    async sendMessage() {
        const message = this.messageInput.value.trim();
        
        if (!message || this.isTyping) {
            return;
        }
        
        // Hide welcome section and show chat
        this.hideWelcomeSection();
        this.showChatMessages();
        
        // Add user message to chat
        this.addMessage(message, 'user');
        
        // Clear input and disable send button
        this.messageInput.value = '';
        this.updateSendButton();
        
        // Show typing indicator
        this.showTypingIndicator();
        
        try {
            // Send message to backend
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });
            
            const data = await response.json();
            
            // Hide typing indicator
            this.hideTypingIndicator();
            
            if (data.status === 'success') {
                // Add bot response to chat
                this.addMessage(data.response, 'bot');
            } else {
                // Handle error
                this.addMessage(
                    'Sorry, I encountered an error. Please try again or rephrase your question.',
                    'bot'
                );
            }
            
        } catch (error) {
            console.error('Error sending message:', error);
            this.hideTypingIndicator();
            this.addMessage(
                'Sorry, I\'m having trouble connecting. Please check your internet connection and try again.',
                'bot'
            );
        }
    }
    
    addMessage(text, sender) {
        const messageElement = document.createElement('div');
        messageElement.className = `message ${sender} fade-in`;
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        avatar.innerHTML = sender === 'user' ? '<i class="fas fa-user"></i>' : '<i class="fas fa-robot"></i>';
        
        const content = document.createElement('div');
        content.className = 'message-content';
        
        const messageText = document.createElement('div');
        messageText.className = 'message-text';
        messageText.textContent = text;
        
        const messageTime = document.createElement('div');
        messageTime.className = 'message-time';
        messageTime.textContent = this.getCurrentTime();
        
        content.appendChild(messageText);
        content.appendChild(messageTime);
        
        messageElement.appendChild(avatar);
        messageElement.appendChild(content);
        
        this.chatMessages.appendChild(messageElement);
        
        // Scroll to bottom
        this.scrollToBottom();
        
        // Store in history
        this.messageHistory.push({
            text: text,
            sender: sender,
            timestamp: new Date()
        });
    }
    
    showTypingIndicator() {
        this.isTyping = true;
        this.typingIndicator.style.display = 'flex';
        this.scrollToBottom();
    }
    
    hideTypingIndicator() {
        this.isTyping = false;
        this.typingIndicator.style.display = 'none';
    }
    
    hideWelcomeSection() {
        if (this.welcomeSection) {
            this.welcomeSection.style.display = 'none';
        }
    }
    
    showChatMessages() {
        if (this.chatMessages) {
            this.chatMessages.classList.add('active');
        }
    }
    
    updateSendButton() {
        const hasText = this.messageInput.value.trim().length > 0;
        this.sendButton.disabled = !hasText || this.isTyping;
        
        if (this.isTyping) {
            this.sendButton.innerHTML = '<div class="loading"></div>';
        } else {
            this.sendButton.innerHTML = '<i class="fas fa-paper-plane"></i>';
        }
    }
    
    scrollToBottom() {
        setTimeout(() => {
            this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
        }, 100);
    }
    
    getCurrentTime() {
        const now = new Date();
        return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }
    
    focusInput() {
        this.messageInput.focus();
    }
    
    // Utility method to clear chat (for development)
    clearChat() {
        this.chatMessages.innerHTML = '';
        this.messageHistory = [];
        this.welcomeSection.style.display = 'block';
        this.chatMessages.classList.remove('active');
    }
}

// Initialize the chatbot when the page loads
document.addEventListener('DOMContentLoaded', () => {
    const chatbot = new HealthChatbot();
    
    // Add some helpful console messages for development
    console.log('🏥 HealthBot AI initialized successfully!');
    console.log('💡 Tip: Try asking about common health topics like symptoms, prevention, or wellness advice.');
    
    // Make chatbot globally available for debugging
    window.healthChatbot = chatbot;
});

// Handle page visibility changes
document.addEventListener('visibilitychange', () => {
    if (!document.hidden) {
        // Refocus input when user returns to tab
        const messageInput = document.getElementById('messageInput');
        if (messageInput) {
            messageInput.focus();
        }
    }
});

// Handle online/offline status
window.addEventListener('online', () => {
    console.log('🌐 Connection restored');
});

window.addEventListener('offline', () => {
    console.log('📡 Connection lost');
    // You could show a notification to the user here
});
