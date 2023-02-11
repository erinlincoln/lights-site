import React from 'react'
import '../newStyle/modeSelect.css'
import modes from '../data/modes';

export default function ModeSelect() {
  return (
    <div className='body-component' id='mode-select'>
        <div id='search-container'>
            <form className='d-flex' role="search">
                <input className="form-control me-2" type="search" placeholder="Start typing a mode name..." aria-label="Search"/>
            </form>
            <div id='filters'>
                <button type="button" className='btn filter-btn'>single</button>
                <button type="button" className='btn filter-btn'>multiple</button>
                <button type="button" className='btn filter-btn'>gradient</button>
            </div>
            <div id='result-disp'>
                <table className='table'>
                    <thead>
                        <tr>
                            <th scope='col'>Name</th>
                            <th scope='col'>Type</th>
                            <th scope='col'>Description</th>
                        </tr>
                    </thead>
                    <tbody className='table-group-divider'>
                        {
                            modes.map((mode) => {
                                return <tr>
                                    <td className='fw-bold'>{mode.name}</td>
                                    <td className='fst-italic'>{mode.type}</td>
                                    <td>{mode.description}</td>
                                </tr>
                            })
                        }
                    </tbody>
                </table>
                <nav aria-label="Page navigation example">
                    <ul className="pagination justify-content-center">
                        <li className="page-item">
                            <a className="page-link" href="#" aria-label="Previous">
                                <span aria-hidden="true">&laquo;</span>
                            </a>
                        </li>
                        <li className="page-item"><a className="page-link" href="#">1</a></li>
                        <li className="page-item"><a className="page-link" href="#">2</a></li>
                        <li className="page-item"><a className="page-link" href="#">3</a></li>
                        <li className="page-item">
                            <a className="page-link" href="#" aria-label="Next">
                                <span aria-hidden="true">&raquo;</span>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
            
        </div>
        
    </div>
  )
}
