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

var all_items = []

const app = express();
const port = 3000;

app.use(express.static('public'))
app.use(morgan("tiny"))
app.use(logger)
app.use(bodyParser.urlencoded({extended: true}));

app.get('/', (req, res) => {
    res.render("index.ejs", {
        all_items: all_items
    })
})

app.post('/new', (req, res) => {
    var item = {
        item: req.body['item'],
        date: req.body['date'],
        time: req.body['time']
    }
    all_items.push(item)
    res.redirect('/')
})

app.post('/remove', (req, res) => {
    var item = {
        item: req.body['item'],
        date: req.body['date'],
        time: req.body['time']
    }
    var index = all_items.indexOf(item)
    all_items.splice(index, 1)
    res.redirect('/')
})

app.listen(port, () => {
    console.log(`Server running on port ${port}.`);
})

