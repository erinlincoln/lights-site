import React from 'react'
import '../../newStyle/dashboard.css';

export default function DashboardItem({id, text} : {id: string, text: string}) {
  return (
    <div id={id} className='dashboard-item g-col rounded p-4 m-3 d-flex flex-column align-content-center justify-content-center'>
        <h4>{text}</h4>
    </div>
  )
}
