import React from 'react'
import { useLightsContext } from '../../contexts/lightsContext';
import { useSequenceContext } from '../../contexts/sequenceContext';
import '../../newStyle/header.css';
import { lightsSequence } from '../../ts/lightsSequence.enums';
import Logo from '../icons/Logo';

export default function Header() {
    const { user, setUser } = useLightsContext();
    const {setStage} = useSequenceContext();

  return (
    <header className='d-flex justify-content-start align-items-center'>
      <Logo size={'xsmall'} />
      <h1 id='header-title' className='ms-2 mt-2 mr-auto' onClick={() => setStage(lightsSequence.DASHBOARD)}>Apollo</h1>
      
      <div id='profile-dropdown' className='dropdown m-3 mt-4 ms-auto d-flex align-items-center'>
        <h5 className='text-lowercase'>hello, {user.name}</h5>
        <button className="btn dropdown-toggle mb-2" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false"></button>
        <div className='dropdown-menu dropdown-menu-right'>
          {
            <div className='dropdown-item mobile-only d-flex' onClick={() => setStage(lightsSequence.DASHBOARD)}>
              <i className="bi bi-lightbulb me-3"></i>
              <span>Lights</span>
            </div>
          }
          {/* <div className='dropdown-item d-flex'>
            <i className="bi bi-person me-3"></i>
            <span>Profile</span>
          </div> */}
          {/* <div className='dropdown-item d-flex'>
            <i className="bi bi-house-gear me-3"></i>
            <span>Presets</span>
          </div> */}
          <div className='dropdown-item d-flex' onClick={() => setUser({})}>
            <i className="bi bi-box-arrow-in-right me-3"></i>
            <span>Logout</span>
          </div>
        </div>
      </div>
      
    </header>
    
  )
}
