import 'dotenv/config'
import express from 'express';
import bodyParser from 'body-parser';
import morgan from 'morgan';
import mongoose from 'mongoose';
import encrypt from 'mongoose-encryption';

const uri = "mongodb://127.0.0.1:27017/secretsDB";

mongoose.connect(uri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });

const userSchema = new mongoose.Schema({
    email: String,
    password: String
});

console.log(process.env.SECRET)
const secret = process.env.SECRET
userSchema.plugin(encrypt, { secret: secret, encryptedFields: ['password'] })

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

        if (user.password !== f_password) {
            res.render('/login', { message: '<p class="error">Please fill out the form below:</p>' })
        }

        res.redirect('/secrets')
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

        const newUser = new User({
            email: f_email,
            password: f_password
        })
        const save = await newUser.save()
        console.log(save)

        res.redirect('/secrets')
    });

app.get('/secrets', (req, res)=>{
    res.render('secrets.ejs')
})

app.listen(port, () => {
    console.log(`Server running on port ${port}.`);
})