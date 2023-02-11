import React from 'react'

export default function Door({color, hoverColor, isDoorHover, handleMouseEnter, handleMouseLeave, handleClick}: {color: string, hoverColor: string, isDoorHover: boolean, handleMouseEnter: any, handleMouseLeave: any, handleClick: any}) {
  return (
    <svg id='door-icon' fill={isDoorHover ? hoverColor : color} onClick={handleClick} onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave} width="56px" height="56px" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M20,20H19V3a1,1,0,0,0-1-1H6A1,1,0,0,0,5,3V20H4a1,1,0,0,0,0,2H20a1,1,0,0,0,0-2ZM7,11a1,1,0,0,1,2,0v2a1,1,0,0,1-2,0Z"/></svg>
  )
}
