import React, { useEffect, useState } from 'react'
import '../newStyle/modeSelect.css'
import modes from '../data/modes';
import { Mode } from '../ts/modes';
import { useSequenceContext } from '../contexts/sequenceContext';
import { lightsSequence } from '../ts/lightsSequence.enums';
import SelectionFooter from './common/SelectionFooter';

export default function ModeSelect() {
    const {setStage, setMode} = useSequenceContext();
    const [searchTerm, setSearch] = useState('');
    const [searchModes, setSearchModes] = useState<Mode[]>(modes);
    const [searchType, setSearchType] = useState({single: false, multiple: false, gradient: false});

    // filter modes on search term or type change
    useEffect(()=>{
        let filteredModes = modes;

        // filter by search term
        if (searchTerm) {
            filteredModes = filteredModes.filter((mode) => mode.name.toLowerCase().includes(searchTerm.toLowerCase()));
        }

        // filter by search types selected
        if (Object.values(searchType).filter( i => i).length > 0) {
            filteredModes = filteredModes.filter((mode) => searchType[mode.type])
        }

        setSearchModes(filteredModes);
    }, [searchTerm, searchType])

  return (
    <div className='body-component' id='mode-select'>
        <div id='search-container'>
            <form className='d-flex' role="search" onChange={(e: any) => setSearch(e.target.value)}>
                <input name='search' className="form-control me-2" type="search" placeholder="Start typing a mode name..." aria-label="Search"/>
            </form>
            <div id='filters'>
                <button type="button" className={`btn ${searchType.single ? 'filter-btn-selected' : 'filter-btn'}`} onClick={() => setSearchType({...searchType, single: !searchType.single})}>single</button>
                <button type="button" className={`btn ${searchType.multiple ? 'filter-btn-selected' : 'filter-btn'}`} onClick={() => setSearchType({...searchType, multiple: !searchType.multiple})}>multiple</button>
                <button type="button" className={`btn ${searchType.gradient ? 'filter-btn-selected' : 'filter-btn'}`} onClick={() => setSearchType({...searchType, gradient: !searchType.gradient})}>gradient</button>
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
                            searchModes.map((mode) => {
                                return <tr onClick={() => { setMode(mode); setStage(lightsSequence.COLORSELECT)}}>
                                    <td className='fw-bold'>{mode.name}</td>
                                    <td className='fst-italic'>{mode.type}</td>
                                    <td>{mode.description}</td>
                                </tr>
                            })
                        }
                    </tbody>
                </table>
            </div>
        </div>
        <SelectionFooter />
    </div>
  )
}
