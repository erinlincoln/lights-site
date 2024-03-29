import React from 'react'

export default function Laptop({color, hoverColor, isLaptopHover, handleMouseEnter, handleMouseLeave, handleClick}: {color: string, hoverColor: string, isLaptopHover: boolean, handleMouseEnter: any, handleMouseLeave: any, handleClick: any}) {
  return (
    <svg onClick={handleClick} onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave} id='laptop-icon' width="56px" height="56px" viewBox="-20 0 190 190" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path fillRule="evenodd" clipRule="evenodd" d="M122.57 146.53C113.98 146.53 38.06 147.7 28.68 147.7C19.3 147.7 18 141.48 18 134.07C20.09 134.07 41.12 134.22 63.84 134.4C63.84 138.89 64.22 138.96 74.68 138.96C85.14 138.96 85.4 138.73 85.4 134.56C106.63 134.72 127.31 134.85 132.02 134.85C132 139.53 130.53 146.53 122.57 146.53ZM29.57 130.41C29.57 130.32 28.88 87.78 29 82.62C29.14 75.85 31.1 73.7 37 73.7C41.72 73.7 105.2 73.81 111.26 73.94C118.16 74.08 119.15 77.33 119.15 83.6C119.15 88.17 117.91 129.73 117.91 129.73L29.57 130.41Z" fill={isLaptopHover ? hoverColor : color} />
    </svg>
  )
}
