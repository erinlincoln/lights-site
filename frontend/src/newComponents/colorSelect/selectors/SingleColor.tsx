import React, { useEffect, useState } from 'react';
import { useSequenceContext } from '../../../contexts/sequenceContext';
import ColorSelector from './ColorSelector';

export default function SingleColor({update = true} : {update: boolean}) {
  const [color, setColor] = useState('#000000');
  const {setBody} = useSequenceContext();

  useEffect(() => {
    if (update) {
      setBody({color});
    }
  }, [color])

  return (
    <ColorSelector color={color} setColor={setColor}/>
  )
}
