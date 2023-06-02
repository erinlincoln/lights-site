import { ReqBody } from "./request";

interface Preset {
    name: string,
    body: ReqBody
}

interface User {
    name: String,
    presets: Preset[]
}

export type {User, Preset};