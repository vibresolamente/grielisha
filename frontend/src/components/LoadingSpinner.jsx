import { Loader2 } from 'lucide-react'

const LoadingSpinner = ({ size = 'medium', text = 'Loading...' }) => {
  const sizeClasses = {
    small: 'w-4 h-4',
    medium: 'w-8 h-8',
    large: 'w-12 h-12'
  }

  return (
    <div className="flex flex-col items-center justify-center space-y-2">
      <Loader2 className={`animate-spin text-accent ${sizeClasses[size]}`} />
      {text && (
        <p className="text-gray-300 text-sm animate-pulse">{text}</p>
      )}
    </div>
  )
}

export default LoadingSpinner
