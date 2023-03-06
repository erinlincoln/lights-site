import React from 'react'
import { useSequenceContext } from '../../contexts/sequenceContext';

export default function SelectionFooter() {
    const {room, setRoom} = useSequenceContext();

  return (
    <footer className='footer d-flex justify-content-center'>
        <div className=' dropdown'>
            <button className="btn btn-secondary btn-lg dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                {room === 'livingroom' ? 'living room' : room}
            </button>
            <div className='dropdown-menu' aria-labelledby='dropdownMenuButton'>
                {
                    ['bedroom', 'livingroom', 'hallway', 'office'].filter(r => r !== room).map(room =>
                        <a className='dropdown-item' onClick={() => setRoom(room)}>{room === 'livingroom' ? 'living room' : room}</a>
                    )
                }
            </div>
        </div>
    </footer>
  )
}
