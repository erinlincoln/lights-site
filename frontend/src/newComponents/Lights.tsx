import React, { useState } from 'react'
import { lightsSequence } from '../ts/lightsSequence.enums'
import Dashboard from './dashboard/Dashboard';
import Header from './common/Header'
import Sidebar from './common/Sidebar'
import '../newStyle/lights.css';
import { MySequenceContext, SequenceContext } from '../contexts/sequenceContext';
import ModeSelect from './ModeSelect';
import { ModeType } from '../ts/modes.d';

export default function Lights() {
  const [stage, setStage] = useState(lightsSequence.DASHBOARD);
  const [room, setRoom] = useState('');
  const [mode, setMode] = useState({name: '', type: ModeType.SINGLE, description: ''});
  const value: SequenceContext = {stage, setStage, room, setRoom, mode, setMode};

  function placeholder (e: any) {
    console.log(e)
    setStage(lightsSequence.ROOMSELECT);
  }

  return (
    <MySequenceContext.Provider value={value}>
      <Header />
      <Sidebar items={[{ label: 'test', iconClass: 'bi-0-circle', onClick: {placeholder} },{ label: 'test', iconClass: 'bi-123', onClick: {placeholder} }]}/>
      {
        stage === lightsSequence.DASHBOARD && <Dashboard />
      }
      {
        stage === lightsSequence.MODESELECT && <ModeSelect />
      }
    </MySequenceContext.Provider>
  )
}
