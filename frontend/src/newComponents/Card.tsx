import React from 'react'
import '../newStyle/card.css';

export default function Card({text, onClick} : { text: String, onClick: Function}) {
  return (
    <button 
        className='card1 p-3 m-3 rounded text-center display-6 text-white text-lowercase' 
        onClick={(e) => onClick(e)}
        >
            {text}
    </button>
  )
}
