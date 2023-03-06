import { createContext, useContext } from "react";
import { lightsSequence } from "../ts/lightsSequence.enums";
import { Mode, ModeType } from "../ts/modes.d";

export interface SequenceContext {
    stage: lightsSequence,
    setStage: Function,
    room: string,
    setRoom: Function,
    mode: Mode,
    setMode: Function,
    body: any,
    setBody: Function
}

export const MySequenceContext = createContext<SequenceContext>({
    stage: lightsSequence.DASHBOARD, 
    setStage: () => {},
    room: '',
    setRoom: () => {},
    mode: {name: '', type: ModeType.SINGLE, description: ''},
    setMode: () => {},
    body: {},
    setBody: () => {}});

export const useSequenceContext = () => useContext(MySequenceContext);