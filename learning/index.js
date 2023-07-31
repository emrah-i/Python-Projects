import express from 'express';
import bodyParser from 'body-parser';
import morgan from 'morgan';
import { dirname } from 'path';
import { fileURLToPath } from 'url';
const __dirname = dirname(fileURLToPath(import.meta.url))

function logger(req, res, next) {
    console.log(`Request Method: ${req.method}`);
    console.log(`Request URL: ${req.url}`);
    next();
}

const app = express();
const port = 3000;

app.use(express.static('public'))
app.use(morgan("tiny"))
app.use(logger)
app.use(bodyParser.urlencoded({extended: true}));

app.get('/', (req, res) => {
    res.render("index.ejs", {
        day: 'weekday',
        advice: 'hi'
    })
})

app.listen(port, () => {
    console.log(`Server running on port ${port}.`);
})

