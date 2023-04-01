import React, { useEffect, useState } from 'react'
import { useSequenceContext } from '../../contexts/sequenceContext'
import SelectionFooter from '../common/SelectionFooter';
import SingleColor from './selectors/SingleColor';
import '../../newStyle/colorSelect.css'
import { lightsSequence } from '../../ts/lightsSequence.enums';
import MultipleColors from './selectors/MultipleColors';
import ColorSlider from './selectors/GradientSelector';
import { useLightsContext } from '../../contexts/lightsContext';
import { RoomStrips, StripId } from '../../ts/request.d';

export default function ColorSelect() {
  const {mode, setStage, body, room} = useSequenceContext();
  const {updateBody} = useLightsContext();
  const [autoUpdate, setAutoUpdate] = useState(true);

  useEffect( () => {
    RoomStrips[room].forEach( (id : StripId) => updateBody({type: 'update', payload: {id, mode: { name: mode.name, data: body}}}))
  }, [body])

  return (
    <div className='body-component'>
      <div id='color-select'>
        <div id='color-header' className='d-flex justify-content-between m-1 mb-4'>
          <h1 className='header-txt' onClick={() => setStage(lightsSequence.MODESELECT)}>{mode.name}</h1>
          
          <div className='dropdown'>
            <i className="header-txt bi bi-three-dots" id='dropdownMenuButton' data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false"></i>
            <div className='dropdown-menu dropdown-menu-right' aria-labelledby='dropdownMenuuButton'>
              <div className='form-check form-switch m-1'>
                <input className='form-check-input' type="checkbox" role='switch' id='auto-update-switch' checked={autoUpdate} onChange={(e : any) => setAutoUpdate(e.target.checked)}/>
                <label className='form-check-label' htmlFor="auto-update-switch">Auto Update</label>
              </div>
            </div>
          </div>
          
        </div>
        {
          mode.name === 'solid' && <SingleColor />
        }
        {
          mode.name === 'multicolor' && <MultipleColors />
        }
        {
          mode.name === 'gradient' && <ColorSlider />
        }
        {
          !autoUpdate &&
          <div className='d-flex justify-content-center'>
            <button id='update-btn' className='btn btn-large mt-3'>Update Lights</button>
          </div>
        }
      </div>
      <SelectionFooter />
    </div>
  )
}
