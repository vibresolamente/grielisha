# GRIELISHA MVP - Digital Marketplace Platform

A hybrid digital platform that integrates e-commerce, service marketplace, and digital solutions with an aggressive, modern UI design.

## 🚀 Features

### Core Functionality
- **E-commerce System**: Product browsing, cart management, checkout, and order tracking
- **Service Booking**: Professional service booking with scheduling capabilities
- **User Authentication**: JWT-based authentication with role-based access control
- **Admin Dashboard**: Comprehensive admin panel with analytics and management tools
- **User Dashboard**: Personal dashboard for managing orders and bookings

### UI/UX Design
- **Aggressive Dark Theme**: Modern, futuristic design with glassmorphism effects
- **Neon Glow Effects**: Vibrant accent colors with animated glow effects
- **Responsive Design**: Fully responsive across all device sizes
- **Smooth Animations**: Micro-interactions and page transitions

### Security Features
- **Authentication Security**: JWT tokens with refresh mechanism
- **API Security**: Input validation, rate limiting, CORS protection
- **Common Attack Prevention**: XSS, CSRF, and SQL injection protection
- **Environment Security**: Secure configuration management

## 🛠 Tech Stack

### Frontend
- **Framework**: React 18 with Vite
- **Styling**: TailwindCSS with custom glassmorphism effects
- **Routing**: React Router v6
- **State Management**: React Context API
- **Animations**: Framer Motion
- **Icons**: Lucide React

### Backend
- **Framework**: Django 4.2 with Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: Django REST Framework Simple JWT
- **Documentation**: drf-spectacular (OpenAPI/Swagger)
- **Security**: Django CORS Headers, built-in protections

## 📁 Project Structure

```
GRIELISHA/
├── frontend/                 # React frontend
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── contexts/        # React contexts
│   │   ├── pages/           # Page components
│   │   ├── App.jsx          # Main App component
│   │   └── main.jsx         # Entry point
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
├── backend/                  # Django backend
│   ├── grielisha/          # Main Django project
│   ├── accounts/           # User management app
│   ├── products/           # Product management app
│   ├── services/           # Service management app
│   ├── orders/             # Order management app
│   ├── bookings/           # Booking management app
│   ├── manage.py
│   └── requirements.txt
└── README.md
```

## 🚀 Setup Instructions

### Prerequisites
- Node.js 16+ and npm
- Python 3.8+ and pip
- PostgreSQL 12+
- Git

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials and secret key
   ```

5. **Set up database**
   ```bash
   # Create PostgreSQL database
   createdb grielisha_db
   
   # Run migrations
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API URL
   ```

4. **Start development server**
   ```bash
   npm run dev
   ```

## 🌐 Access Points

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/api/docs/
- **Admin Panel**: http://localhost:8000/admin/

## 📊 API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `GET /api/auth/profile/` - User profile

### Products
- `GET /api/products/` - List products
- `POST /api/products/` - Create product (admin only)
- `GET /api/products/{id}/` - Product details
- `PUT /api/products/{id}/` - Update product (admin only)
- `DELETE /api/products/{id}/` - Delete product (admin only)

### Services
- `GET /api/services/` - List services
- `POST /api/services/` - Create service (admin only)
- `GET /api/services/{id}/` - Service details
- `PUT /api/services/{id}/` - Update service (admin only)
- `DELETE /api/services/{id}/` - Delete service (admin only)

### Orders
- `GET /api/orders/` - List user orders
- `POST /api/orders/create/` - Create order
- `GET /api/orders/{id}/` - Order details
- `GET /api/orders/cart/` - View cart
- `POST /api/orders/cart/add/` - Add to cart

### Bookings
- `GET /api/bookings/` - List bookings
- `POST /api/bookings/` - Create booking
- `GET /api/bookings/{id}/` - Booking details
- `PUT /api/bookings/{id}/` - Update booking

## 🔐 Security Implementation

### Authentication
- JWT access tokens (1 hour expiry)
- JWT refresh tokens (7 days expiry)
- Token rotation and blacklisting
- Role-based access control

### API Security
- Input validation and sanitization
- SQL injection prevention (Django ORM)
- XSS prevention (template escaping)
- CSRF protection (built-in Django)
- Rate limiting (configurable)
- CORS configuration

### Environment Security
- Environment variable configuration
- No hardcoded secrets
- Secure cookie settings
- HTTPS enforcement in production

## 🎨 UI Components

### Design System
- **Primary Color**: #0A0F1C (Dark blue)
- **Accent Color**: #FF6A00 (Orange)
- **Glow Color**: #00C2FF (Cyan)
- **Glass Effect**: Backdrop blur with transparency
- **Neon Glow**: Animated shadow effects

### Key Components
- **Navbar**: Glass morphism with neon branding
- **Product Cards**: Hover effects with glow animation
- **Service Cards**: Interactive booking interface
- **Dashboard Panels**: Data visualization components
- **Forms**: Glass input fields with validation

## 📱 Responsive Design

- **Mobile**: 320px and up
- **Tablet**: 768px and up
- **Desktop**: 1024px and up
- **Large Desktop**: 1280px and up

## 🚀 Deployment

### Frontend (Vercel/Netlify)
```bash
npm run build
# Deploy dist/ folder
```

### Backend (Heroku/DigitalOcean)
```bash
# Set environment variables
# Collect static files
python manage.py collectstatic
# Deploy with gunicorn
gunicorn grielisha.wsgi:application
```

## 🔄 Future Enhancements

- **M-Pesa Integration**: Mobile payment integration
- **Staff/Worker Module**: Service provider management
- **Notification System**: Email and SMS notifications
- **Real-time Chat**: Customer support chat
- **Analytics Dashboard**: Advanced analytics and reporting
- **Mobile App**: React Native mobile application

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 📞 Support

For support and inquiries:
- Email: info@grielisha.com
- Phone: +254 700 000 000
- Location: Nairobi, Kenya

---

**GRIELISHA MVP** - Your premier digital marketplace platform 🚀
