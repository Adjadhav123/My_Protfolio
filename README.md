# Aditya Jadhav - Interactive Portfolio Website

A modern, responsive portfolio website built with HTML, CSS, JavaScript, and Flask backend. Features smooth animations, interactive elements, and a professional design showcasing AI/ML expertise.

## 🚀 Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Interactive Animations**: Smooth scroll animations using AOS library
- **Modern UI/UX**: Clean, professional design with gradient effects
- **Flask Backend**: RESTful API for contact form and data management
- **Fast Loading**: Optimized images and efficient code structure
- **SEO Friendly**: Semantic HTML and proper meta tags
- **Cross-browser Compatible**: Works on all modern browsers

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3 (Flexbox, Grid, Animations)
- JavaScript (ES6+)
- AOS (Animate On Scroll)
- Font Awesome Icons

### Backend
- Python 3.x
- Flask
- Jinja2 Templates

## 📁 Project Structure

```
Portfolio/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   ├── js/
│   │   └── script.js     # JavaScript functionality
│   └── images/
│       ├── profile.jpg   # Your profile photo
│       ├── about.jpg     # About section photo
│       └── README.md     # Image requirements
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```cmd
   cd "C:\Users\adity\OneDrive\Desktop\Portfolio"
   ```

2. **Install Python dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Add your photos**
   - Add your profile photo as `static/images/profile.jpg`
   - Add an about photo as `static/images/about.jpg`
   - See `static/images/README.md` for detailed requirements

4. **Run the application**
   ```cmd
   python app.py
   ```

5. **Open your browser**
   - Navigate to `http://localhost:5000`
   - Your portfolio will be live!

## 🎨 Customization

### Personal Information
Edit the `portfolio_data` dictionary in `app.py` to update:
- Personal details (name, email, phone, location)
- Work experience
- Education
- Skills
- Projects
- Achievements
- Certifications

### Styling
- Modify `static/css/style.css` to change colors, fonts, and layout
- The color scheme uses CSS custom properties for easy theming
- All animations and effects can be customized

### Content
- Update the HTML template in `templates/index.html`
- Add or remove sections as needed
- Modify the navigation menu

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px to 1199px
- **Mobile**: Below 768px

## 🌟 Interactive Features

1. **Smooth Scrolling Navigation**: Click navigation links for smooth page scrolling
2. **Mobile Menu**: Responsive hamburger menu for mobile devices
3. **Scroll Animations**: Elements animate as you scroll using AOS library
4. **Contact Form**: Functional contact form with Flask backend
5. **Back to Top**: Floating button to return to top of page
6. **Progress Bar**: Shows page scroll progress
7. **Hover Effects**: Interactive hover effects on cards and buttons
8. **Easter Egg**: Try the Konami code for a surprise! ⬆️⬆️⬇️⬇️⬅️➡️⬅️➡️BA

## 🔧 API Endpoints

- `GET /`: Main portfolio page
- `GET /api/portfolio`: Get portfolio data as JSON
- `POST /api/contact`: Submit contact form
- `GET /api/download-resume`: Track resume downloads

## 📊 Performance Optimizations

- Efficient CSS with minimal specificity
- Debounced scroll events
- Image lazy loading ready
- Minification ready for production
- Optimized animations for 60fps

## 🚀 Deployment Options

### Local Development
```cmd
python app.py
```

### Production Deployment
1. **Heroku**: Add `Procfile` with `web: python app.py`
2. **Vercel**: Configure for Flask deployment
3. **PythonAnywhere**: Upload files and configure WSGI
4. **Digital Ocean**: Deploy on droplet with nginx

## 🤝 Contributing

Feel free to fork this project and customize it for your own portfolio!

## 📄 License

This project is open source and available under the MIT License.

## 📞 Contact

**Aditya Jadhav**
- Email: aditya29jadhav@gmail.com
- LinkedIn: [aditya-jadhav-588218257](https://www.linkedin.com/in/aditya-jadhav-588218257/)
- GitHub: [Adjadhav123](https://github.com/Adjadhav123)
- Location: Nashik, Maharashtra

---

**Built with ❤️ by Aditya Jadhav**
