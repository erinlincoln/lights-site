import React, { useEffect, useState } from 'react'
import { BE_URL } from "../utils/lightsConstants";

// async function sendGenericCommand() {
//     /* TODO */
// }

export default function EventHistory() {

    const [eventHistory, setEventHistory] = useState<any[]>([]);

    async function getEventHistory() {
        return await fetch(BE_URL + "/eventhistory/", {
            method: 'GET',
            mode: 'cors',
        })
        .catch(err => console.log(err))
        .then((value) => {
            if (value && value.ok) {
                value.json().then((j) => {
                    setEventHistory(j)
                })
            }
        })
    }

    useEffect(() => {
        /* ? */
    }, [eventHistory])

    console.log(eventHistory)

    let DisplayData = eventHistory.map(
        (msg) => {
            let identifier = (msg.device_name === "")? msg.device_ip : msg.device_name + "(" + msg.device_ip + ")";
            return (
                <tr>
                    <td>{msg.timestamp}</td>
                    <td>{msg.direction === "IN"? identifier : "Backend"}</td>
                    <td>{msg.direction === "OUT"? identifier : "Backend"}</td>
                    <td>{msg.message}</td>
                    <td>{msg.id}</td>
                </tr>
        )}
    )

    return (
        <div className='body-component' id='event-history'>
            <div>
                <button type="button" className={'btn'} onClick={() => getEventHistory()}>Get Event History</button>
            </div>
            <div id='event-history-table'>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>Timestamp</th>
                            <th>From</th>
                            <th>To</th>
                            <th>Message</th>
                            <th>ID</th>
                        </tr>
                    </thead>
                    <tbody>
                        {DisplayData}
                    </tbody>
                </table>
            </div>
        </div>
    )
}