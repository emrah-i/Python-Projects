import express from 'express';
import bodyParser from 'body-parser';
import morgan from 'morgan';
import { MongoClient } from 'mongodb'

const app = express();
const port = 3000;

app.use(express.static("public"));
app.set('view engine', 'ejs');
app.use(morgan("short"));
app.use(bodyParser.urlencoded({
    extended: true
}))

app.get('/', (req, res)=> {
    res.render('index.ejs')
})

app.route('/login')
    .get((req, res)=>{
        res.render('login.ejs')
    })
    .post((req, res)=>{
        res.redirect('/')
    });

app.route('/register')
    .get((req, res)=>{
        res.render('register.ejs')
    })
    .post((req, res)=>{
        res.redirect('/')
    });

app.listen(port, () => {
    console.log(`Server running on port ${port}.`);
})