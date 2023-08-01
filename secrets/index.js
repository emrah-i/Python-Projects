import express from 'express';
import bodyParser from 'body-parser';
import morgan from 'morgan';

const app = express();
const port = 3000;

app.use(express.static('public'))
app.use(morgan("tiny"))
app.use(bodyParser.urlencoded({extended: true}));

app.get('/', (req, res) => {
    app.render('index.ejs')
})

app.listen(port, () => {
    console.log(`Server running on port ${port}.`);
})