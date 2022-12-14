import React from 'react'

export default function Restart({setPickingZone, zone}) {
  return (
    <div>
        <h4 onClick={() => setPickingZone(true)}>zone: {zone}</h4>
    </div>
  )
}
