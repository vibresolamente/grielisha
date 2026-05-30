import { createContext, useContext, useState, useCallback } from 'react'

const ToastContext = createContext()

export const useToast = () => {
  const context = useContext(ToastContext)
  if (!context) {
    throw new Error('useToast must be used within a ToastProvider')
  }
  return context
}

export const ToastProvider = ({ children }) => {
  const [toasts, setToasts] = useState([])

  const addToast = useCallback((type, message, options = {}) => {
    const id = Date.now() + Math.random()
    const newToast = {
      id,
      type,
      message,
      duration: options.duration || 5000,
      position: options.position || 'top-right',
      ...options
    }

    setToasts(prev => [...prev, newToast])
    return id
  }, [])

  const removeToast = useCallback((id) => {
    setToasts(prev => prev.filter(toast => toast.id !== id))
  }, [])

  const success = useCallback((message, options) => {
    return addToast('success', message, options)
  }, [addToast])

  const error = useCallback((message, options) => {
    return addToast('error', message, { duration: 0, ...options })
  }, [addToast])

  const warning = useCallback((message, options) => {
    return addToast('warning', message, options)
  }, [addToast])

  const info = useCallback((message, options) => {
    return addToast('info', message, options)
  }, [addToast])

  const value = {
    toasts,
    addToast,
    removeToast,
    success,
    error,
    warning,
    info
  }

  return (
    <ToastContext.Provider value={value}>
      {children}
    </ToastContext.Provider>
  )
}
