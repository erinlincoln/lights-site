import React, { useState } from 'react'
import { useLightsContext } from '../contexts/lightsContext'
import Card from './common/Card'
import '../newStyle/login.css';
import Logo from './icons/Logo';

export default function Login() {
  const { setUser } = useLightsContext();
  const [hasAcct, setHasAcct] = useState(true);
  const hour: Number = new Date().getHours();

  function message(hour: Number) {
    if ( hour < 6 ) {
      return 'Good night. Or is it morning...';
    } else if ( hour < 12 ) {
      return 'Good morning.';
    } else if ( hour < 17 ) {
      return 'Good afternoon';
    } else if ( hour < 20 ) {
      return 'Good evening.';
    } else {
      return 'Good night.';
    }
  }

  function clickUser(e: any) {
    const name = e.target.textContent;

    setUser({name});
  }

  function submitName(e: any) { 
    e.preventDefault();
    const name = e.target.name.value;

    setUser({name});
  }

  return (
    <div className='component row justify-content-center align-items-center'>
      <div id='message-container' className='component col-6 order-2 d-flex flex-column justify-content-center'>
        <h1 className='text-white display-3 text-center text-lowercase p-3'>
          { message(hour) }
        </h1>
        <Logo size={'medium'} />
        <h5 className='text-center text-white mt-3'>what is your name?</h5>
      </div>
      <div className={` ${ hasAcct ? 'col order-3' : 'col-6 order-1'} component d-flex flex-column justify-content-between`}>
        <div></div>
        {
          hasAcct
            ? <div id='user-container' className='d-flex flex-wrap justify-content-center align-content-center'>
                <Card text='Erin' onClick={clickUser}/>
                <Card text='Quintin' onClick={clickUser}/>
              </div>
          : <form onSubmit={submitName} id='signup-container' className='d-flex flex-column justify-content-start p-3'>
              <label htmlFor="signup">name</label>
              <input type="text" name="name" id="signup-field" />
              <input id='signup-submit' type="submit" value="sign up" className='mt-3 text-white rounded'/>
            </form>
        }
        <button id='new-profile-btn' onClick={() => setHasAcct(!hasAcct)} className='m-3 rounded justify-self-end'>
          { hasAcct? 'sign in as a guest' : 'choose an existing user'}
        </button>
      </div>
      
      
    </div>
  )
}
