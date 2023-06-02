import React from 'react'
import { HexColorPicker } from 'react-colorful';
import '../../../newStyle/singleColor.css';

export default function ColorSelector({color, setColor}: {color: string, setColor: any}) {
  return (
    <div id='color-picker' style={{ background: color}}>
        <HexColorPicker color={color} onChange={setColor} />
    </div>
  )
}
