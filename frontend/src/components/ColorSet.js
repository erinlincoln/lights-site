import React from 'react'
import Rainbow from 'rainbowvis.js';
import '../style/colorSet.css';


export default function ColorSet({setColor, colorArr}) {

    const rainbow = new Rainbow();
    rainbow.setNumberRange(0,100);
    rainbow.setSpectrum('FCF9D9', 'D9EEFC');

    function handleClick(e) {
        const i = Math.round(e.clientX / e.target.clientWidth * 100);
        setColor(`#${rainbow.colorAt(i)}`)
    }

  return (
    <div style={{
        backgroundImage: `linear-gradient(to right, ${colorArr[0]}, ${colorArr[1]})`,
        height: 50,
    }} onMouseUp={handleClick} onTouchEnd={handleClick}>
    </div>
  )
}
