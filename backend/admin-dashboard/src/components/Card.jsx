import { motion } from 'framer-motion'
import { forwardRef } from 'react'

const Card = forwardRef(({
  children,
  className = '',
  hover = true,
  glow = false,
  glass = true,
  padding = 'normal',
  rounded = 'lg',
  onClick,
  as: Component = 'div',
  ...props
}, ref) => {
  const MotionComponent = motion[Component]

  const baseClasses = 'transition-all duration-300'
  
  const variantClasses = glass ? 'glass' : 'bg-primary'
  
  const hoverClasses = hover ? 'hover:bg-white/10 cursor-pointer' : ''
  
  const glowClasses = glow ? 'neon-glow' : ''
  
  const paddingClasses = {
    none: '',
    small: 'p-3',
    normal: 'p-6',
    large: 'p-8'
  }
  
  const roundedClasses = {
    none: '',
    sm: 'rounded',
    md: 'rounded-lg',
    lg: 'rounded-xl',
    xl: 'rounded-2xl'
  }

  return (
    <MotionComponent
      ref={ref}
      onClick={onClick}
      className={`${baseClasses} ${variantClasses} ${hoverClasses} ${glowClasses} ${paddingClasses[padding]} ${roundedClasses[rounded]} ${className}`}
      whileHover={hover ? { scale: 1.02 } : undefined}
      whileTap={onClick ? { scale: 0.98 } : undefined}
      {...props}
    >
      {children}
    </MotionComponent>
  )
})

Card.displayName = 'Card'

export default Card
