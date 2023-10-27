import { ReqBody } from "../ts/request";

async function sendLightsReq(req : ReqBody) {
    await fetch('http://192.168.0.6:3001/lights/', {
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