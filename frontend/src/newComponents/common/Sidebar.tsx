import React from 'react'
import '../../newStyle/sidebar.css';
import { SidebarItem } from '../../ts/sidebarItem';

export default function Sidebar({items}: {items: SidebarItem[]}) {
  return (
    <aside id='sidebar'>
        <div className='component d-flex flex-column justify-content-start align-items-start p-2 pt-4'>
            {
                items.map((item) =>
                    <div className='sidebar-item p-2 d-flex flex-row align-items-center' onClick={item.onClick}>
                        <i className={`bi ${item.iconClass} me-3`}></i>
                        <span className='text-lowercase'>{item.label}</span>
                    </div>
                )
            }

            <div className='mt-auto sidebar-item p-2 d-flex flex-row align-items-center ml-auto mr-auto'>
                <i className={`bi bi-box-arrow-in-right me-3`}></i>
                <span className='text-lowercase'>Logout</span>
            </div>
        </div>
    </aside>
  )
}