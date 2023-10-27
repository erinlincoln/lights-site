import { StripId } from "./request";

enum BodyActionKind {
    SETUP = 'setup',
    UPDATE = 'update',
    RESET = 'reset'
  }

interface BodyAction {
    type: BodyActionKind,
    payload: ReqStrip
}

export type { BodyActionKind, BodyAction };