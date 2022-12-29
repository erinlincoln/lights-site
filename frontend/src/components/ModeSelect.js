import React, { useContext} from 'react';
import modeChoices from '../modes.js';
import { StateContext } from './LightsDisp.js';
import '../style/modeSelect.css';

export default function ModeSelect({ setChoices }) {

  const { setColors, setMode } = useContext( StateContext );
    
    function changeMode(e) {
        const val = e.target.value;
        const valArr = modeChoices[ val ];
        setMode({ name: val, length: modeChoices[val].length });
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
            <option value="stripped">striped</option>
        </select>
    </div>
  )
}
