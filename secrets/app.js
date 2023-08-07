import 'dotenv/config'
import express from 'express';
import bodyParser from 'body-parser';
import morgan from 'morgan';
import mongoose from 'mongoose';
import bcrypt from 'bcrypt';

const uri = "mongodb://127.0.0.1:27017/secretsDB";
const salt_rounds = 10

mongoose.connect(uri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });

const userSchema = new mongoose.Schema({
    email: String,
    password: String
});

const User = new mongoose.model('User', userSchema);

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
        res.render('login.ejs', { message: '<p>Please fill out the form below:</p>' })
    })
    .post(async (req, res)=>{
        const f_email = req.body.email
        const f_password = req.body.password
        const user = await User.findOne({email: f_email})
        bcrypt.compare(f_password, user.password, function(err, result) {
            if (err) {
                console.log(err)
            }
        
            if (result === true) {
                res.redirect('/secrets')
            }
        })
    });

app.route('/register')
    .get((req, res)=>{
        res.render('register.ejs', {message: '<p>Please fill out the follow form:<p>'})
    })
    .post(async (req, res)=>{
        const f_email = req.body.email
        const f_password = req.body.password
        const confirm = req.body.confirm
        
        if (confirm !== f_password) {
            res.render('register.ejs', {message: '<p class="error">Error: passwords do not match!</p>'})
        }

        bcrypt.hash(req.body.password, salt_rounds, async function(err, hash) {
            if (err) {
                console.log(err)
            }

            const newUser = new User({
                email: f_email,
                password: hash
            });

            await newUser.save()
            res.redirect('/secrets')
        })
    });

app.get('/secrets', (req, res)=>{
    res.render('secrets.ejs')
})

app.listen(port, () => {
    console.log(`Server running on port ${port}.`);
})