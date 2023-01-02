import React, { useContext, useEffect } from 'react';
import { HexColorPicker } from "react-colorful";
import '../../style/singleColor.css'
import { ColorContext } from '../ColorSelect';
import { StateContext } from '../Main';

export default function SingleColor() {

  // setup vars
  const { index, color, setColor } = useContext( ColorContext );
  const { data, setData } = useContext( StateContext );
  const mode = data.mode.type;

  useEffect( () => {
    // if there is a color set
    if ( color ) {
      // assign color to different field based on mode
      switch ( mode ) {
        case 'single-color':
          setData( { type: 'data', data: { ...data.data, colors: [ color ] }});
          break;
        case 'multi-color':
          // change color at this index and update data
          const newArr = data.data.colors || [];
          newArr[ index ] = color;
          setData( { type: 'data', data: { ...data.data, colors: newArr }});
          break;
        default:
          console.log( 'INVALID mode for single color select')
      }
    }
  }, [ color ])

  return (
    <div id='color-picker'>
        <HexColorPicker color={color} onChange={setColor} />
    </div>
  )
}
