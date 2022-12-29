import React, { useContext } from 'react'
import { StateContext } from './LightsDisp';

export default function Restart() {

  const { setPickingRoom } = useContext( StateContext );

  return (
    <div>
        <h4 onClick={() => setPickingRoom(true)}>choose another room</h4>
    </div>
  )
}
