import { motion } from 'framer-motion'
import { Loader2 } from 'lucide-react'

const Button = ({ 
  children, 
  variant = 'primary', 
  size = 'medium', 
  loading = false, 
  disabled = false, 
  className = '', 
  icon: Icon,
  iconPosition = 'left',
  onClick,
  type = 'button',
  ...props 
}) => {
  const baseClasses = 'font-semibold rounded-lg transition-all transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-accent/50 disabled:transform-none disabled:cursor-not-allowed'
  
  const variantClasses = {
    primary: 'bg-accent hover:bg-orange-600 text-white neon-glow-accent',
    secondary: 'glass hover:bg-white/20 text-white border border-white/20',
    danger: 'bg-red-500 hover:bg-red-600 text-white',
    success: 'bg-green-500 hover:bg-green-600 text-white',
    ghost: 'text-accent hover:bg-accent/10 hover:text-orange-600'
  }
  
  const sizeClasses = {
    small: 'px-3 py-1.5 text-sm',
    medium: 'px-4 py-2 text-base',
    large: 'px-6 py-3 text-lg'
  }

  const MotionButton = motion.button

  return (
    <MotionButton
      type={type}
      onClick={onClick}
      disabled={disabled || loading}
      className={`${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]} ${className}`}
      whileHover={{ scale: disabled || loading ? 1 : 1.05 }}
      whileTap={{ scale: disabled || loading ? 1 : 0.95 }}
      {...props}
    >
      <span className="flex items-center justify-center">
        {loading && (
          <Loader2 className="animate-spin mr-2" size={size === 'small' ? 14 : size === 'large' ? 20 : 16} />
        )}
        
        {Icon && iconPosition === 'left' && !loading && (
          <Icon className="mr-2" size={size === 'small' ? 14 : size === 'large' ? 20 : 16} />
        )}
        
        <span className={loading ? 'opacity-70' : ''}>
          {children}
        </span>
        
        {Icon && iconPosition === 'right' && !loading && (
          <Icon className="ml-2" size={size === 'small' ? 14 : size === 'large' ? 20 : 16} />
        )}
      </span>
    </MotionButton>
  )
}

export default Button
