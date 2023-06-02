import { createContext, useContext } from "react";
import { lightsSequence } from "../ts/lightsSequence.enums";
import { Mode, ModeType } from "../ts/modes.d";

export interface SequenceContext {
    stage: lightsSequence,
    setStage: Function,
    room: 'livingroom' | 'hallway' | 'office' | 'bedroom',
    setRoom: Function,
    mode: Mode,
    setMode: Function,
    body: any,
    setBody: Function
}

export const MySequenceContext = createContext<SequenceContext>({
    stage: lightsSequence.DASHBOARD, 
    setStage: () => {},
    room: 'livingroom',
    setRoom: () => {},
    mode: {type: '', name: ModeType.SOLID, description: ''},
    setMode: () => {},
    body: {},
    setBody: () => {}});

export const useSequenceContext = () => useContext(MySequenceContext);