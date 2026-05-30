#!/bin/bash

# GRIELISHA Development Server Startup Script
echo "🚀 Starting GRIELISHA Development Servers..."

# Check if PostgreSQL is running
if ! pg_isready -q; then
    echo "⚠️  PostgreSQL is not running. Please start PostgreSQL first."
    echo "   On Windows: Start PostgreSQL service"
    echo "   On Mac: brew services start postgresql"
    echo "   On Linux: sudo systemctl start postgresql"
    exit 1
fi

# Start Backend Server
echo "🔧 Starting Django Backend Server..."
cd backend
if [ ! -d "venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python -m venv venv
fi

source venv/bin/activate
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating backend .env file..."
    cp .env.example .env
    echo "⚠️  Please update backend/.env with your database credentials"
fi

# Run database migrations
echo "🗄️ Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Start Django server in background
echo "🌐 Starting Django server on http://localhost:8000..."
python manage.py runserver &
BACKEND_PID=$!

# Start Frontend Server
echo "⚛️ Starting React Frontend Server..."
cd ../frontend

# Install dependencies if node_modules doesn't exist
if [ ! -d "node_modules" ]; then
    echo "📦 Installing frontend dependencies..."
    npm install
fi

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating frontend .env file..."
    cp .env.example .env
fi

# Start React development server
echo "🎨 Starting React server on http://localhost:3000..."
npm run dev &
FRONTEND_PID=$!

# Wait for servers to start
sleep 5

echo ""
echo "✅ GRIELISHA Development Servers Started!"
echo ""
echo "🌐 Frontend: http://localhost:3000"
echo "🔧 Backend API: http://localhost:8000"
echo "📚 API Documentation: http://localhost:8000/api/docs/"
echo "🔐 Admin Panel: http://localhost:8000/admin/"
echo ""
echo "🛑 Press Ctrl+C to stop all servers"

# Function to cleanup background processes
cleanup() {
    echo ""
    echo "🛑 Stopping servers..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo "✅ All servers stopped"
    exit 0
}

# Trap Ctrl+C to cleanup
trap cleanup INT

# Wait for user interrupt
wait
