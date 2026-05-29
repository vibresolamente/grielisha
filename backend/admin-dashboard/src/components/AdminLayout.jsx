import { Link, useLocation } from 'react-router-dom'
import { LayoutDashboard, Users, ShoppingBag, Grid, Archive, LogOut } from 'lucide-react'
import { useAuth } from '../contexts/AuthContext'

const AdminLayout = ({ children }) => {
  const { user, logout } = useAuth()
  const location = useLocation()

  const navLinks = [
    { name: 'Overview', path: '/', icon: <LayoutDashboard size={20} /> },
    { name: 'Order Logs', path: '/orders', icon: <ShoppingBag size={20} /> },
    { name: 'Products DB', path: '/products', icon: <Archive size={20} /> },
    { name: 'Services Grid', path: '/services', icon: <Grid size={20} /> },
    { name: 'User CRM', path: '/users', icon: <Users size={20} /> },
  ]

  return (
    <div className="flex min-h-screen bg-[#0a0a0c] text-white font-sans overflow-hidden">
      {/* Absolute Professional Sidebar */}
      <aside className="w-64 bg-[#111116] border-r border-[#222] flex flex-col justify-between shrink-0 shadow-2xl">
        <div>
          {/* Corporate Header */}
          <div className="h-24 flex items-center px-6 border-b border-[#222]">
            <img src="/logo.png" alt="Grielisha Core" className="h-10 w-10 object-contain mr-3 filter drop-shadow-md brightness-200" />
            <div>
              <h1 className="text-xl font-bold tracking-widest uppercase text-white shadow-glow-yellow">GRIELISHA</h1>
              <p className="text-[10px] text-accent tracking-widest font-mono font-bold">COMMAND CENTER</p>
            </div>
          </div>
          
          {/* Navigation */}
          <nav className="p-4 space-y-2 mt-4">
            <div className="text-[10px] font-bold tracking-widest text-[#555] uppercase mb-4 px-2">Core Modules</div>
            {navLinks.map((link) => {
              const isActive = location.pathname === link.path
              return (
                <Link
                  key={link.name}
                  to={link.path}
                  className={`flex items-center space-x-3 px-4 py-3 rounded-md transition-all duration-200 ${
                    isActive 
                      ? 'bg-accent/10 border border-accent/20 text-accent font-bold shadow-lg' 
                      : 'text-gray-400 hover:text-white hover:bg-white/5'
                  }`}
                >
                  {link.icon}
                  <span className="text-sm tracking-wide">{link.name}</span>
                </Link>
              )
            })}
          </nav>
        </div>

        {/* Profile / Logout */}
        <div className="bg-[#0b0b0e] p-4 border-t border-[#222]">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="h-10 w-10 rounded-full bg-accent/20 border border-accent flex items-center justify-center text-accent font-bold">
                {user?.email?.[0]?.toUpperCase() || 'A'}
              </div>
              <div>
                <p className="text-sm font-bold text-white truncate max-w-[120px]">{user?.email}</p>
                <p className="text-[10px] text-gray-500 uppercase tracking-widest">Admin</p>
              </div>
            </div>
            <button 
              onClick={logout} 
              title="Terminate Session"
              className="p-2 text-red-500 hover:text-red-400 hover:bg-red-500/10 rounded-md transition-colors"
            >
              <LogOut size={18} />
            </button>
          </div>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 h-screen overflow-y-auto bg-[#0a0a0c]">
        {/* Top bar subtle indicator */}
        <header className="h-14 bg-[#111116]/80 backdrop-blur-md border-b border-[#222] sticky top-0 z-10 flex items-center justify-between px-8">
          <h2 className="text-sm text-gray-400 tracking-wider">SECURE ENVIRONMENT <span className="text-green-500 font-mono ml-2">● LIVE</span></h2>
        </header>

        {/* Dynamic Route Injection */}
        <div className="p-8">
          {children}
        </div>
      </main>
    </div>
  )
}

export default AdminLayout
