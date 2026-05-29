import { useState, useEffect } from 'react'
import { Link, useNavigate, useLocation } from 'react-router-dom'
import { ShoppingCart, User, Menu, X, LogOut, Heart } from 'lucide-react'
import { useAuth } from '../contexts/AuthContext'

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false)
  const [scrolled, setScrolled] = useState(false)
  const { user, logout } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20)
    }
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const handleLogout = () => {
    logout()
    navigate('/')
  }

  return (
    <nav className={`fixed top-0 w-full z-50 transition-all duration-300 ${
      scrolled ? 'glass-dark shadow-lg' : 'glass'
    }`}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <Link 
            to="/" 
            className="flex items-center space-x-2 group"
          >
            <img 
              src="/logo.png" 
              alt="GRIELISHA Logo" 
              className="w-10 h-10 object-contain neon-glow rounded-lg transform group-hover:scale-110 group-hover:rotate-6 transition-all duration-300" 
            />
            <span className="text-2xl font-bold text-glow group-hover:text-accent transition-all tracking-tight">
              GRIELISHA
            </span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-8">
            <Link 
              to="/shop" 
              className={`text-white hover:text-accent transition-colors ${
                location.pathname === '/shop' ? 'text-accent' : ''
              }`}
            >
              Shop
            </Link>
            <Link 
              to="/services" 
              className={`text-white hover:text-accent transition-colors ${
                location.pathname === '/services' ? 'text-accent' : ''
              }`}
            >
              Services
            </Link>
            
            <Link 
              to="/wishlist" 
              className="relative p-2 text-white hover:text-red-500 transition-colors group"
            >
              <Heart size={24} className={location.pathname === '/wishlist' ? 'fill-red-500 text-red-500 shadow-glow-red' : ''} />
            </Link>

            <Link 
              to="/cart" 
              className="relative p-2 text-white hover:text-accent transition-colors"
            >
              <ShoppingCart size={24} />
              <span className="absolute -top-1 -right-1 bg-accent text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
                0
              </span>
            </Link>

            {/* User Menu */}
            {user ? (
              <div className="flex items-center space-x-4">
                <Link 
                  to="/dashboard" 
                  className="text-white hover:text-accent transition-colors"
                >
                  <User size={24} />
                </Link>
                {user.role === 'admin' && (
                  <Link 
                    to="/admin" 
                    className="text-glow hover:text-accent transition-colors text-sm"
                  >
                    Admin
                  </Link>
                )}
                <button
                  onClick={handleLogout}
                  className="text-white hover:text-accent transition-colors"
                >
                  <LogOut size={24} />
                </button>
              </div>
            ) : (
              <div className="flex items-center space-x-4">
                <Link 
                  to="/login" 
                  className="text-white hover:text-accent transition-colors"
                >
                  Login
                </Link>
                <Link 
                  to="/register" 
                  className="bg-accent hover:bg-orange-600 text-white px-4 py-2 rounded-lg transition-colors neon-glow-accent"
                >
                  Register
                </Link>
              </div>
            )}
          </div>

          {/* Mobile menu button */}
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="md:hidden text-white hover:text-accent transition-colors"
          >
            {isOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>

        {/* Mobile Navigation */}
        {isOpen && (
          <div className="md:hidden glass-dark rounded-lg mt-2 p-4">
            <div className="flex flex-col space-y-4">
              <Link 
                to="/shop" 
                className="text-white hover:text-accent transition-colors"
                onClick={() => setIsOpen(false)}
              >
                Shop
              </Link>
              <Link 
                to="/services" 
                className="text-white hover:text-accent transition-colors"
                onClick={() => setIsOpen(false)}
              >
                Services
              </Link>
              <Link 
                to="/cart" 
                className="text-white hover:text-accent transition-colors"
                onClick={() => setIsOpen(false)}
              >
                Cart
              </Link>
              <Link 
                to="/wishlist" 
                className="text-white hover:text-red-500 transition-colors"
                onClick={() => setIsOpen(false)}
              >
                Wishlist
              </Link>
              
              {user ? (
                <>
                  <Link 
                    to="/dashboard" 
                    className="text-white hover:text-accent transition-colors"
                    onClick={() => setIsOpen(false)}
                  >
                    Dashboard
                  </Link>
                  {user.role === 'admin' && (
                    <Link 
                      to="/admin" 
                      className="text-glow hover:text-accent transition-colors"
                      onClick={() => setIsOpen(false)}
                    >
                      Admin Panel
                    </Link>
                  )}
                  <button
                    onClick={() => {
                      handleLogout()
                      setIsOpen(false)
                    }}
                    className="text-white hover:text-accent transition-colors text-left"
                  >
                    Logout
                  </button>
                </>
              ) : (
                <>
                  <Link 
                    to="/login" 
                    className="text-white hover:text-accent transition-colors"
                    onClick={() => setIsOpen(false)}
                  >
                    Login
                  </Link>
                  <Link 
                    to="/register" 
                    className="bg-accent hover:bg-orange-600 text-white px-4 py-2 rounded-lg transition-colors text-center"
                    onClick={() => setIsOpen(false)}
                  >
                    Register
                  </Link>
                </>
              )}
            </div>
          </div>
        )}
      </div>
    </nav>
  )
}

export default Navbar
