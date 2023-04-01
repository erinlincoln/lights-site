// import logo from './logo.svg';
// import logo from './images/apollo-2.png'
import React, { useEffect, useReducer, useState } from 'react';
// import LightsDisp from './components/Main';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import Login from './newComponents/Login';
import Lights from './newComponents/Lights';
import { LightsContext, MyLightsContext } from './contexts/lightsContext';
import { ReqBody, ReqStrip } from './ts/request';
import { BodyAction } from './ts/bodyAction';
import { User } from './ts/user';
import { sendLightsReq } from './utils/sendLightsReq';


const bodyReducer = (state: ReqBody, action: BodyAction) : ReqBody => {
  switch(action.type) {
    case "setup":
      return { strips: [...state.strips, action.payload]};
    case "update":
      return { strips: state.strips.map( (strip : ReqStrip) => strip.id === action.payload.id ? action.payload : strip )};
    default:
      return state;
  }
}

function App() {
  const [user, setUser] : [user: User, setUser: Function] = useState({name: '', presets: []});
  const [body, updateBody] = useReducer(bodyReducer, {strips: []});
  const value: LightsContext = { user, setUser, body, updateBody}

  useEffect(() => {
    if (body.strips[0]?.mode.data && Object.keys(body.strips[0].mode.data).length > 0) {
      sendLightsReq(body);
    }
  }, [body])

  return (
    <div className='app'>
      <MyLightsContext.Provider value={value}>
        <BrowserRouter >
          <Routes>
            <Route index element={ user.name ? <Lights /> : <Login /> }/>
            <Route path='/login' element={<Login />} />
            <Route path='/lights' element={<Lights />}/>
          </Routes>
        </BrowserRouter>
      </MyLightsContext.Provider> 
    </div>
    
    // <div className="App">
    //   <LightsDisp />
    //   {/* <img src={logo} alt="Apollo logo" /> */}
    // </div>
  );
}

export default App;
