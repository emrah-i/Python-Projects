import 'dotenv/config'
import express from 'express';
import bodyParser from 'body-parser';
import morgan from 'morgan';
import mongoose from 'mongoose';
import session from 'express-session';
import passport from 'passport';
import { Strategy as LocalStrategy } from 'passport-local';
import passportLocalMongoose from 'passport-local-mongoose';

const app = express();
const port = 3000;

app.use(express.static("public"));
app.set('view engine', 'ejs');
app.use(morgan("short"));
app.use(bodyParser.urlencoded({
    extended: true
}))

app.use(session({
    secret: 'ilovetosleep',
    resave: false,
    saveUninitialized: false
}));

app.use(passport.initialize());
app.use(passport.session())

mongoose.connect("mongodb://127.0.0.1:27017/secretsDB", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });


const userSchema = new mongoose.Schema({
    email: String,
    password: String
});

userSchema.plugin(passportLocalMongoose);

const User = new mongoose.model('User', userSchema);

passport.use(User.createStrategy());

passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

app.get('/', (req, res)=> {
    res.render('index.ejs')
})

app.route('/login')
    .get((req, res)=>{
        res.render('login.ejs', { message: '<p>Please fill out the form below:</p>' })
    })
    .post(async (req, res)=>{
        
    });

app.route('/register')
    .get((req, res)=>{
        res.render('register.ejs', {message: '<p>Please fill out the follow form:<p>'})
    })
    .post(async (req, res)=> {
        try {
            const user = await User.register({ username: req.body.email }, req.body.password);
            passport.authenticate('local', { failureRedirect: '/register'}),
            function(req, res) {
                res.redirect('/secrets');
            }
        } catch (err) {
            console.log(err);
            res.redirect('/register');
        }
    });

app.get('/secrets', async (req, res)=>{
    console.log(req.user)
    if (req.user) {
        res.render('secrets.ejs')
    }
    else {
        res.redirect('/')
    }
})

app.listen(port, () => {
    console.log(`Server running on port ${port}.`);
})