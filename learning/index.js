import express from 'express'

const app = express();
const port = 3000;

app.get('/', (req, res) => {
    res.send('<h1>Ahh Hello, World!</h1>')
})

app.listen(port, () => {
    console.log('Server running on port 3000.');
})

