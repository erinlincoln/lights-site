import React, { useEffect, useState } from 'react'
import Rainbow from 'rainbowvis.js';
import '../../../newStyle/gradientSelect.css';
import { useSequenceContext } from '../../../contexts/sequenceContext';
import Slider from './Slider';
import tinycolor from "tinycolor2";


export default function ColorSlider() {

  // setup vars

  const {mode} = useSequenceContext();
  const colors = mode.data.colors;
  const [ color, setColor ] = useState(colors[0]);
  const [pureColor, setPureColor] = useState(colors[0])
  const [currColors, setCurrColors] = useState(colors);
  const [dim, setDim] = useState(0);
  const rainbow = new Rainbow();
  rainbow.setNumberRange(0,100);
  rainbow.setSpectrum( ...colors );
  
  useEffect(() => {
    //update gradient
    const newColors = colors.map((c : any) => tinycolor(c).darken(dim).toString());
    setCurrColors(newColors);
    rainbow.setSpectrum( ...newColors );

    // update dimness
    setColor(tinycolor(pureColor).darken(dim).toString());
  }, [dim])

  // set color based on position clicked
  function handleClick(e: any) {
      const i = Math.round(e.clientX / e.target.clientWidth * 100);
      setColor(`#${rainbow.colorAt(i)}`)
      setPureColor(`#${rainbow.colorAt(i)}`)
  }

  return (
    <div className='row'>
      <div className='col-9 col-sm-11'>
        <div className='gradient mb-1' style={{
                backgroundImage: `linear-gradient(to right, ${currColors[0]}, ${currColors[1]})`,
                height: 50,
            }} onMouseUp={handleClick} onTouchEnd={handleClick}>
        </div>
        <div className='choice-container' style={{background: color}}></div>
      </div>
      <div className='col col-sm-1'>
        <Slider dim={dim} setDim={setDim}/>
      </div>
    </div>
    
    
  )
}
