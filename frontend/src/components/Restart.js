import React, { useContext } from 'react'
import { StateContext } from './Main';

export default function Restart() {

  const { setPickingRoom } = useContext( StateContext );

  return (
    <div>
        <h4 onClick={() => setPickingRoom(true)}>choose another room</h4>
    </div>
  )
}
