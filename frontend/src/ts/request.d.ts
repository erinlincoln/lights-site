import { Mode } from "./modes";

enum StripId {
    O1= 'o1',
    O2= 'o2',
    O3= 'o3',
    L1= 'l1',
    L2= 'l2',
    L3= 'l3',
    H1 = 'h1'
    // B1 = 'b1',
    // B2 = 'b2,
  }

interface ReqStrip {
    id: StripId[];
    mode: Mode
}
  
interface ReqBody {
    strips: ReqStrip[];
}

export type {StripId, ReqBody, ReqStrip};