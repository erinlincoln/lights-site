import React, { useState } from 'react'
import { lightsSequence } from '../ts/lightsSequence.enums'
import Dashboard from './dashboard/Dashboard';
import Header from './common/Header'
import Sidebar from './common/Sidebar'
import '../newStyle/lights.css';
import { MySequenceContext, SequenceContext } from '../contexts/sequenceContext';
import ModeSelect from './ModeSelect';
import { ModeType } from '../ts/modes.d';
import ColorSelect from './colorSelect/ColorSelect';

export default function Lights() {
  const [stage, setStage] = useState(lightsSequence.DASHBOARD);
  const [room, setRoom] = useState('');
  const [mode, setMode] = useState({name: '', type: ModeType.SINGLE, description: ''});
  const [body, setBody] = useState({});
  const value: SequenceContext = {stage, setStage, room, setRoom, mode, setMode, body, setBody};

  return (
    <MySequenceContext.Provider value={value}>
      <Header />
      <div className='lights-wrapper'>
        <Sidebar items={[{ label: 'lights', iconClass: 'bi-lightbulb', onClick: () => setStage(lightsSequence.DASHBOARD) }]}/>
        {
          stage === lightsSequence.DASHBOARD && <Dashboard />
        }
        {
          stage === lightsSequence.MODESELECT && <ModeSelect />
        }
        {
          stage == lightsSequence.COLORSELECT && <ColorSelect />
        }
      </div>
      
    </MySequenceContext.Provider>
  )
}
