from flask import Flask, render_template, jsonify, request
from datetime import datetime
import json

app = Flask(__name__)

# Portfolio data
portfolio_data = {
    "personal_info": {
        "name": "Aditya Jadhav",
        "title": "AI Developer & Machine Learning Engineer",
        "description": "AI Developer with good Python skills. Builds machine learning models and web applications. Solves problems creatively and works well in teams to deliver smart solutions.",
        "phone": "+91-7498533304",
        "email": "aditya29jadhav@gmail.com",
        "location": "Nashik, Maharashtra",
        "linkedin": "https://www.linkedin.com/in/aditya-jadhav-588218257/",
        "github": "https://github.com/Adjadhav123"
    },
    "work_experience": [
        {
            "position": "Machine Learning Intern",
            "company": "Medhavyn Technologies",
            "duration": "2025 – Present",
            "description": "Currently working on computer vision and deep learning projects. Involved in model development, deployment, and building AI pipelines. Collaborating with the team to apply machine learning in solving real world problems."
        }
    ],
    "education": [
        {
            "degree": "Bachelor of Technology",
            "institution": "K.K.Wagh Institute Of Engineering Education & Research, Nashik",
            "duration": "2022 - Pursuing",
            "grade": "CGPA - 8.84"
        },
        {
            "degree": "Higher Secondary Certification Examination (HSC)",
            "institution": "Shramik Junior College, Sangamner",
            "duration": "2022",
            "grade": "Percentage - 84.67%"
        },
        {
            "degree": "Secondary School Certificate Examination (SSC)",
            "institution": "Adhala Vidyalay, Deothan",
            "duration": "2020",
            "grade": "Percentage - 94.40%"
        }
    ],
    "projects": [
        {
            "title": "Grape Disease Detection and Farm Planner",
            "duration": "2025 – Present",
            "description": "Web app for grape disease detection and complete farm planning.",
            "role": "AI/ML Developer",
            "technologies": ["Pretrained CNN models", "ResNet50", "InceptionV3", "Langchain", "Groq API"],
            "github": "#"
        },
        {
            "title": "RAGBOT-Talk With PDF",
            "duration": "2024-2025",
            "description": "Developed an AI-powered chatbot using RAG architecture that enables natural language conversations with PDF documents for instant information retrieval.",
            "role": "AI/ML Developer",
            "technologies": ["Langchain", "Groq API", "Vector Embeddings", "NLP"],
            "github": "RAGBOT"
        },
        {
            "title": "Training the YOLO model",
            "duration": "2024-2025",
            "description": "Training the YOLO object detection models on various mechanical parts and achieve the accuracy above 90%.",
            "role": "Machine Learning Intern",
            "technologies": ["YOLOv8", "OpenCV"],
            "github": "#"
        }
    ],
    "certificates": [
        "Complete Data Science, Machine Learning, DL, NLP Bootcamp : UDEMY",
        "Python for Data Science : NPTEL - IIT Madras",
        "Complete Generative AI Course With Langchain and Hugging Face : UDEMY",
        "Mastering Data Structure & Algorithm in C & C++ : UDEMY"
    ],
    "achievements": [
        "1st Prize Winner – GENAITHON 2K25 (National Level Hackathon)",
        "Top Performing Team — Tech Pragyan Hackathon 2025"
    ],
    "activities": {
        "co_curricular": [
            "Core Committee Member of Debugger's Club",
            "Project-Based Learning — 2nd Prize Winner"
        ],
        "extra_curricular": [
            "NSS Volunteer-KKWIEER, Nashik [2025-Present]",
            "Swapnpurti Foundation Volunteer - KKWIEE"
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)

@app.route('/api/portfolio')
def get_portfolio_data():
    return jsonify(portfolio_data)

@app.route('/api/contact', methods=['POST'])
def handle_contact():
    data = request.get_json()
    # Here you can add logic to handle contact form submissions
    # For now, we'll just return a success response
    return jsonify({
        "status": "success",
        "message": "Thank you for your message! I'll get back to you soon."
    })

@app.route('/api/download-resume')
def download_resume():
    # This endpoint can be used to track resume downloads
    return jsonify({
        "status": "success",
        "message": "Resume download initiated"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
