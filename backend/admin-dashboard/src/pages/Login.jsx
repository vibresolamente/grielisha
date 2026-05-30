import { useState, useEffect } from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import { motion } from 'framer-motion'
import { Eye, EyeOff, Mail, Lock, AlertCircle, ShieldCheck } from 'lucide-react'
import { useAuth } from '../contexts/AuthContext'

const Login = () => {
  const [formData, setFormData] = useState({ email: '', password: '' })
  const [showPassword, setShowPassword] = useState(false)
  const [errors, setErrors] = useState({})
  const [isLoading, setIsLoading] = useState(false)

  const { login, isAuthenticated } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()
  const from = location.state?.from?.pathname || '/'

  useEffect(() => {
    if (isAuthenticated) navigate(from, { replace: true })
  }, [isAuthenticated, navigate, from])

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({ ...prev, [name]: value }))
    if (errors[name]) setErrors(prev => ({ ...prev, [name]: '' }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    const newErrors = {}
    if (!formData.email) newErrors.email = 'Email is required'
    else if (!/\S+@\S+\.\S+/.test(formData.email)) newErrors.email = 'Invalid email format'
    if (!formData.password) newErrors.password = 'Password is required'

    if (Object.keys(newErrors).length > 0) { setErrors(newErrors); return }

    setIsLoading(true)
    setErrors({})
    try {
      const result = await login(formData.email, formData.password)
      if (!result.success) setErrors({ general: result.error || 'Access denied. Admin credentials required.' })
    } catch {
      setErrors({ general: 'Connection to server failed. Is the backend running?' })
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-[#08080a] flex">
      {/* Left Branding Panel */}
      <div className="hidden lg:flex w-1/2 bg-[#0d0d10] border-r border-[#1a1a20] flex-col justify-between p-12">
        <div className="flex items-center space-x-3">
          <img src="/logo.png" alt="Grielisha" className="h-10 w-10 object-contain brightness-200" />
          <div>
            <h1 className="text-xl font-bold tracking-widest uppercase text-white">GRIELISHA</h1>
            <p className="text-[10px] text-accent tracking-widest font-mono">COMMAND CENTER</p>
          </div>
        </div>

        <div>
          <div className="mb-8">
            <div className="inline-flex items-center space-x-2 bg-accent/10 border border-accent/20 text-accent text-xs px-3 py-1.5 rounded-full mb-6">
              <ShieldCheck size={12} />
              <span className="font-mono tracking-wider">AUTHORISED PERSONNEL ONLY</span>
            </div>
            <h2 className="text-4xl font-bold text-white leading-tight mb-4">
              Ecosystem<br />Operations Hub
            </h2>
            <p className="text-gray-500 text-sm leading-relaxed max-w-sm">
              Centralised management of orders, logistics, inventory, customer relationships, and business analytics for the Grielisha Eco-Systems enterprise platform.
            </p>
          </div>

          <div className="grid grid-cols-2 gap-4">
            {[
              { label: 'Orders', value: 'Live Sync' },
              { label: 'Documents', value: 'Auto-Gen' },
              { label: 'Products', value: 'Full CRUD' },
              { label: 'Analytics', value: 'Real-Time' },
            ].map(item => (
              <div key={item.label} className="bg-[#111114] border border-[#222] rounded-lg p-4">
                <p className="text-[10px] text-gray-500 uppercase tracking-widest mb-1">{item.label}</p>
                <p className="text-white font-semibold text-sm">{item.value}</p>
              </div>
            ))}
          </div>
        </div>

        <p className="text-gray-600 text-xs">© 2024 Grielisha Eco-Systems. All rights reserved.</p>
      </div>

      {/* Right Login Panel */}
      <div className="flex-1 flex items-center justify-center p-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="w-full max-w-md"
        >
          {/* Mobile logo */}
          <div className="lg:hidden flex items-center space-x-3 mb-10">
            <img src="/logo.png" alt="Grielisha" className="h-9 w-9 object-contain brightness-200" />
            <div>
              <h1 className="text-lg font-bold tracking-widest uppercase text-white">GRIELISHA</h1>
              <p className="text-[10px] text-accent tracking-widest font-mono">COMMAND CENTER</p>
            </div>
          </div>

          <div className="mb-8">
            <h2 className="text-2xl font-bold text-white mb-2">Administrator Sign In</h2>
            <p className="text-gray-500 text-sm">Enter your admin credentials to access the management dashboard.</p>
          </div>

          {errors.general && (
            <motion.div
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              className="mb-6 p-4 bg-red-900/20 border border-red-700/40 rounded-lg flex items-start space-x-3"
            >
              <AlertCircle className="text-red-400 shrink-0 mt-0.5" size={16} />
              <span className="text-red-300 text-sm">{errors.general}</span>
            </motion.div>
          )}

          <form onSubmit={handleSubmit} className="space-y-5" autoComplete="on">
            {/* Email */}
            <div>
              <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-2">
                Email Address
              </label>
              <div className="relative">
                <Mail className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-600" size={16} />
                <input
                  type="email"
                  name="email"
                  autoComplete="email"
                  value={formData.email}
                  onChange={handleChange}
                  className={`w-full pl-10 pr-4 py-3 bg-[#0d0d10] border rounded-lg text-white text-sm placeholder-gray-600 focus:outline-none focus:ring-1 focus:ring-accent transition-all ${
                    errors.email ? 'border-red-700' : 'border-[#222] focus:border-accent'
                  }`}
                  placeholder="admin@grielisha.com"
                />
              </div>
              {errors.email && <p className="mt-1.5 text-xs text-red-400">{errors.email}</p>}
            </div>

            {/* Password */}
            <div>
              <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-2">
                Password
              </label>
              <div className="relative">
                <Lock className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-600" size={16} />
                <input
                  type={showPassword ? 'text' : 'password'}
                  name="password"
                  autoComplete="current-password"
                  value={formData.password}
                  onChange={handleChange}
                  className={`w-full pl-10 pr-12 py-3 bg-[#0d0d10] border rounded-lg text-white text-sm placeholder-gray-600 focus:outline-none focus:ring-1 focus:ring-accent transition-all ${
                    errors.password ? 'border-red-700' : 'border-[#222] focus:border-accent'
                  }`}
                  placeholder="••••••••••••"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-500 hover:text-gray-300 transition-colors"
                >
                  {showPassword ? <EyeOff size={16} /> : <Eye size={16} />}
                </button>
              </div>
              {errors.password && <p className="mt-1.5 text-xs text-red-400">{errors.password}</p>}
            </div>

            {/* Submit */}
            <button
              type="submit"
              disabled={isLoading}
              className="w-full mt-2 bg-accent hover:bg-orange-600 text-white py-3 rounded-lg text-sm font-semibold transition-all disabled:opacity-40 disabled:cursor-not-allowed flex items-center justify-center"
            >
              {isLoading ? (
                <>
                  <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2" />
                  Authenticating...
                </>
              ) : (
                <>
                  <ShieldCheck size={16} className="mr-2" />
                  Access Command Center
                </>
              )}
            </button>
          </form>

          <div className="mt-8 p-4 bg-[#0d0d10] border border-[#1a1a20] rounded-lg">
            <p className="text-[10px] text-gray-600 uppercase tracking-wider mb-1">Secure Access Notice</p>
            <p className="text-xs text-gray-500">This portal is restricted to authorised Grielisha administrators. Unauthorised access attempts are logged.</p>
          </div>
        </motion.div>
      </div>
    </div>
  )
}

export default Login
