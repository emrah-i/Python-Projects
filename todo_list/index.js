import express from 'express';
import bodyParser from 'body-parser';
import morgan from 'morgan';
import { MongoClient } from 'mongodb'

const uri = "mongodb://127.0.0.1:27017";

const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

async function run() {
    await client.connect();
    const database = client.db('todoDB');
    const all_items = database.collection('items');
    return all_items
}

const app = express();
const port = 3000;

app.use(express.static('public'))
app.use(morgan("tiny"))
app.use(bodyParser.urlencoded({extended: true}));

app.get('/', async (req, res) => {
    const all_items = await run();
    const items = await all_items.find({}).toArray();
    await client.close();

    res.render('index.ejs', { all_items: items });
});

app.post('/new', async (req, res) => {
    var item = {
        item: req.body['item'],
        date: req.body['date'],
        time: req.body['time']
    }
    
    const all_items = await run();
    await all_items.insertOne(item);
    await client.close();
    res.redirect('/')
})

app.post('/remove', async (req, res) => {
    var item = {
        item: req.body['item'],
        date: req.body['date'],
        time: req.body['time']
    }
    const all_items = await run();
    await all_items.deleteOne(item);
    await client.close();
    res.redirect('/')
})

app.listen(port, () => {
    console.log(`Server running on port ${port}.`);
})

