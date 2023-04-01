import React, { useEffect, useState } from 'react';
import { useSequenceContext } from '../../../contexts/sequenceContext';
import ColorSelector from './ColorSelector';

export default function SingleColor() {
  const [color, setColor] = useState('');
  const {setBody} = useSequenceContext();

  useEffect(() => {
    if (color) {
      setBody({'colors': [color]});
    }
  }, [color])

  return (
    <ColorSelector color={color? color : '#000000'} setColor={setColor}/>
  )
}
