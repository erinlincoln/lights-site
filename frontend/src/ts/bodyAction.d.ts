import { StripId } from "./request";

enum BodyActionKind {
    SETUP = 'setup',
    UPDATE = 'update'
  }
  
interface BodyActionPayload {
    strip: StripId,
    mode: Mode
}

interface BodyAction {
    type: BodyActionKind,
    payload: BodyActionPayload
}

export type { BodyActionKind, BodyActionPayload, BodyAction };