import { Routes, Route } from 'react-router-dom'
import { AuthProvider } from './contexts/AuthContext'
import { ToastProvider, useToast } from './contexts/ToastContext'
import { ToastContainer } from './components/Toast'
import Login from './pages/Login'
import AdminDashboard from './pages/AdminDashboard'
import DocumentPrint from './pages/DocumentPrint'
import ProtectedRoute from './components/ProtectedRoute'
import AdminLayout from './components/AdminLayout'

function App() {
  return (
    <AuthProvider>
      <ToastProvider>
        <AppContent />
      </ToastProvider>
    </AuthProvider>
  )
}

function AppContent() {
  const { toasts, removeToast } = useToast()
  
  return (
    <div className="bg-primary">
      <Routes future={{ v7_startTransition: true, v7_relativeSplatPath: true }}>
        <Route path="/login" element={<Login />} />
        <Route path="/document/:type/:id" element={
          <ProtectedRoute requiredRole="admin">
            <DocumentPrint />
          </ProtectedRoute>
        } />
        <Route path="/*" element={
          <ProtectedRoute requiredRole="admin">
            <AdminLayout>
              <Routes>
                <Route path="/*" element={<AdminDashboard />} />
              </Routes>
            </AdminLayout>
          </ProtectedRoute>
        } />
      </Routes>
      <ToastContainer toasts={toasts} removeToast={removeToast} />
    </div>
  )
}

export default App
