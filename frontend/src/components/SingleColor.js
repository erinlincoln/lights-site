import React from 'react';
import { HexColorPicker } from "react-colorful";
import '../style/singleColor.css'

export default function SingleColor({color, setColor, index}) {
  return (
    <div id='color-picker'>
        <HexColorPicker color={color} onChange={setColor} />
    </div>
  )
}
