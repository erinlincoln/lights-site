import React from 'react';
import modeChoices from '../modes.js';
import '../style/modeSelect.css';

export default function ModeSelect({setColors, setMode, setChoices}) {
    
    function changeMode(e) {
        const val = e.target.value;
        const valArr = modeChoices[ val ];
        setMode(val);
        setChoices( valArr )
        setColors( [...Array(valArr.length)] )
    }

  return (
    <div id='mode-select'>
        <label htmlFor="mode-selector">Mode</label>
        <select name="mode" id="mode-selector" onChange={changeMode}>
            <option>Choose a mode</option>
            <option value="off">off</option>
            <option value="sunlight">sunlight</option>
            <option value="single">single color</option>
            {/* <option value="rainbow">rainbow</option> */}
            <option value="stripped">stripped</option>
        </select>
    </div>
  )
}
