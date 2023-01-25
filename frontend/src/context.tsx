import { createContext, useContext } from "react";
import { ReqBody } from "./ts/request";
import { User } from "./ts/user";

export interface LightsContext {
    user: User,
    setUser: Function,
    body: ReqBody,
    updateBody: Function
}

export const MyLightsContext = createContext<LightsContext>({
    user: {name: ''},
    setUser: () => {},
    body: { strips: [] },
    updateBody: () => {}
});

export const useLightsContext = () => useContext(MyLightsContext);
