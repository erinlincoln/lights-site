import { ReqBody } from "../ts/request";
import { BE_URL } from "./lightsConstants";

async function sendLightsReq(req : ReqBody) {
    await fetch(BE_URL + '/lights/', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify( req )
        })
        .catch(err => console.log(err))
}

export {sendLightsReq};