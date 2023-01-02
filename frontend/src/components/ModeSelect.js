import React, { createContext, useContext} from 'react';
import modeChoices from '../modes.js';
import { StateContext } from './Main.js';
import '../style/modeSelect.css';

export default function ModeSelect() {

  const { setData, setChoices } = useContext( StateContext );
    
  function changeMode(e) {
      const val = e.target.value;
      const valArr = modeChoices[ val ].choices;
      setData( { type: 'mode', mode: { name: val, type: modeChoices[ val ].mode } } );
      // setMode({ name: val, length: modeChoices[val].length });
      setChoices( valArr )
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
              <option value="striped">striped</option>
          </select>
      </div>
    
  )
}
