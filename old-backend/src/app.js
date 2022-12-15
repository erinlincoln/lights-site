const express = require('express');
const app = express();
const cors = require('cors')
app.use(cors())
app.use(express.json())

const port = 3001;

app.post("/lights", ( req, res ) => {
    res.json(req.body)
})


app.listen( port, () => console.log(`Listening on port ${port}...`));