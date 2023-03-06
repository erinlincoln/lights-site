import React, { useState } from 'react'
import ColorSelector from './ColorSelector';
import '../../../newStyle/multipleColors.css';

export default function MultipleColors() {
    const [colorArr, updateColorArr] = useState<string[]>(['#000000', '#000000', '#000000']);


  return (
      <div className='accordion'>
        {
            colorArr.map(
                (color, i) => 
                    <div className='accordion-item mult-container'>
                        <h1 className='accordion-header' id={`accordion-heading-${i}`}>
                            <button className='btn btn-secondary accordion-button mult-btn' id={`dropdownMenuButton-${i}`} type="button" data-bs-toggle="collapse" data-bs-target={`#accordion-collapse-${i}`} aria-expanded="true" aria-controls="panelsStayOpen-collapseOne" style={{ background: color }}>Color {i + 1}</button>
                        </h1>
                        
                        <div id={`accordion-collapse-${i}`} className='accordion-collapse collapse mult-dropdown-menu' aria-labelledby={`accordion-heading-${i}`}>
                            <div className='accordion-body'>
                                <ColorSelector color={color} setColor={(newColor : string) => updateColorArr(() => { const clone = colorArr.slice(); clone.splice(i, 1, newColor); return clone; })} />
                            </div>
                        </div>
                    </div>
            )
        }
      </div>
  )
}
