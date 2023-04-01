import { StripId } from "./request";

enum BodyActionKind {
    SETUP = 'setup',
    UPDATE = 'update'
  }

interface BodyAction {
    type: BodyActionKind,
    payload: ReqStrip
}

export type { BodyActionKind, BodyAction };