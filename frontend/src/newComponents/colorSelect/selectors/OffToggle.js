import React, { useContext, useEffect } from 'react';
import Toggle from 'react-toggle';
import '../../style/toggle.css';
import { ColorContext } from '../../../components/ColorSelect';
import { StateContext } from '../../../components/Main';

export default function OffToggle() {

    const { color, setColor } = useContext( ColorContext );
    const { data, setData } = useContext( StateContext );

    // set to off on first load
    useEffect( () => {
        setColor('#000000')
    }, [])

    // update data when toggled
    useEffect( () => {
        setData( { type: 'data', data: { ...data.data, colors : [ color ] } });
    }, [ color ])

    // when toggled, update color
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
