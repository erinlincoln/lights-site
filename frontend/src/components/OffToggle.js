import React, { useContext, useEffect } from 'react';
import Toggle from 'react-toggle';
import '../style/toggle.css';

export default function OffToggle({ setColor }) {

    useEffect( () => {
        setColor('#000000')
    }, [])

    function handleToggle(e) {
        if ( e.target.checked ) {
            setColor('last')
        } else {
            setColor('#000000')
        }
    }

  return (
      <label>
        <Toggle 
            id='off-toggle'
            onChange={handleToggle}
        />
        <span className='label-text'>Turn lights on</span>
      </label>
    
  )
}
