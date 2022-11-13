const express = require('express');
const app = express();

const port = 3000;

app.use("/test", ( req, res ) => {
    res.send( 'Success!')
})


app.listen( port, () => console.log(`Listening on port ${port}...`));