import { AlertCircle, RefreshCw } from 'lucide-react'

const ErrorMessage = ({ 
  message, 
  onRetry, 
  variant = 'default',
  className = '' 
}) => {
  const variantClasses = {
    default: 'bg-red-500/20 border-red-500/50 text-red-300',
    warning: 'bg-yellow-500/20 border-yellow-500/50 text-yellow-300',
    info: 'bg-blue-500/20 border-blue-500/50 text-blue-300'
  }

  return (
    <div className={`p-4 rounded-lg border flex items-start space-x-3 ${variantClasses[variant]} ${className}`}>
      <AlertCircle size={20} className="flex-shrink-0 mt-0.5" />
      <div className="flex-1">
        <p className="text-sm">{message}</p>
        {onRetry && (
          <button
            onClick={onRetry}
            className="mt-2 flex items-center space-x-1 text-sm hover:opacity-80 transition-opacity"
          >
            <RefreshCw size={14} />
            <span>Try Again</span>
          </button>
        )}
      </div>
    </div>
  )
}

export default ErrorMessage
