import React, { useContext, useEffect } from 'react'
import Rainbow from 'rainbowvis.js';
import { ColorContext } from '../ColorSelect';
import '../../style/colorSet.css';
import { StateContext } from '../Main';


export default function ColorSlider({ colors }) {

  // setup vars
  const { color, setColor } = useContext( ColorContext );
  const { data, setData } = useContext( StateContext );

  // setup rainbow for color selection
  const rainbow = new Rainbow();
  rainbow.setNumberRange(0,100);
  rainbow.setSpectrum( ...colors );

  // set color based on position clicked
  function handleClick(e) {
      const i = Math.round(e.clientX / e.target.clientWidth * 100);
      setColor(`#${rainbow.colorAt(i)}`)
  }
  
  // update data when color changes
  useEffect( () => {
    setData( { type: 'data', data: { ...data.data, colors : [ color ] } });
  }, [ color ])

  return (
    <div style={{
        backgroundImage: `linear-gradient(to right, ${colors[0]}, ${colors[1]})`,
        height: 50,
    }} onMouseUp={handleClick} onTouchEnd={handleClick}>
    </div>
  )
}
