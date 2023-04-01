import { ReqBody } from "../ts/request";

async function sendLightsReq(req : ReqBody) {
    await fetch('http://localhost:3001/lights/', {
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