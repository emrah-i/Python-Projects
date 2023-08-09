import 'dotenv/config'
import express from 'express';
import bodyParser from 'body-parser';
import morgan from 'morgan';
import mongoose from 'mongoose';
import session from "express-session";
import passport from 'passport'; 
import passportLocalMongoose from 'passport-local-mongoose';
import { Strategy as GoogleStrategy } from 'passport-google-oauth20';
import { Strategy as FacebookStrategy } from 'passport-facebook';
import findOrCreate from 'mongoose-findorcreate';

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
    saveUninitialized: false,
}));

app.use(passport.initialize());
app.use(passport.session());

mongoose.connect("mongodb://127.0.0.1:27017/secretsDB", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });

const userSchema = new mongoose.Schema({
    email: String,
    password: String,
    googleId: String,
    facebookId: String
});

const secretSchema = new mongoose.Schema({
  secret: String,
  date: {
    type: String,
    default: Date.now
  }
});

userSchema.plugin(passportLocalMongoose);
userSchema.plugin(findOrCreate);

const User = new mongoose.model('User', userSchema);
const Secret = new mongoose.model('Secret', secretSchema)

passport.use(User.createStrategy());

passport.serializeUser(function(user, cb) {
    process.nextTick(function() {
      return cb(null, {
        id: user.id,
        username: user.username,
        picture: user.picture
      });
    });
  });

passport.deserializeUser(function(user, cb) {
    process.nextTick(function() {
      return cb(null, user);
    });
  });

passport.use(new GoogleStrategy({
    clientID: process.env.CLIENT_ID,
    clientSecret: process.env.CLIENT_SECRET,
    callbackURL: "http://localhost:3000/auth/google/secrets",
    userProfileURL: "https://www.googleapis.com/oauth2/v3/userinfo"
  },
  function(accessToken, refreshToken, profile, cb) {
    User.findOrCreate({ googleId: profile.id }, function (err, user) {
      return cb(err, user);
    });
  }
));

passport.use(new FacebookStrategy({
    clientID: process.env.FB_ID,
    clientSecret: process.env.FB_SECRET,
    callbackURL: "http://localhost:3000/auth/facebook/secrets"
  },
  function(accessToken, refreshToken, profile, cb) {
    User.findOrCreate({ facebookId: profile.id }, function (err, user) {
      return cb(err, user);
    });
  }
));

// nodemon restarts sever every edit so the isAuthenticated() doesn't work after refresh

app.get('/', (req, res)=> {
    if (req.isAuthenticated()){
        res.redirect('/secrets')
    }
    else {
        res.render('index.ejs')
    }
});

app.get('/auth/facebook',
  passport.authenticate('facebook'));

app.get('/auth/facebook/secrets',
  passport.authenticate('facebook', { failureRedirect: '/login' }),
  function(req, res) {
    res.redirect('/secrets');
  });

app.get('/auth/google',
    passport.authenticate('google', { scope: ['email', 'profile'] }))

app.get('/auth/google/secrets', 
    passport.authenticate('google', { failureRedirect: '/login' }),
    function(req, res) {
      res.redirect('/secrets');
    });

app.route('/register')
    .get((req, res)=>{
        if (req.isAuthenticated()){
            res.redirect('/secrets')
        }
        else {
            res.render('register.ejs', {message: '<p>Please fill out the follow form:<p>'})
        }
    })
    .post(async (req, res)=> {
        try {
            const user = await User.register({ username: req.body.username }, req.body.password);
            req.login(user, (err) => {
            if (err) {
                console.error('Error during login:', err);
                return res.redirect('/login');
            }

            res.redirect('/secrets');
            });
        }
        catch {
            console.log(err);
            res.redirect('/register');
        }
    });

app.route('/login')
    .get((req, res)=>{
        if (req.isAuthenticated()){
            res.redirect('/secrets');
        }
        else {
            res.render('login.ejs', { message: '<p>Please fill out the form below:</p>' });
        }
    })
    .post((req, res) => {
        passport.authenticate('local', {
          successRedirect: '/secrets',
          failureRedirect: '/login',
        })(req, res);
      });

app.get('/logout', (req, res)=>{
    req.logout(()=>{
    res.redirect('/')
    })
});

app.route('/secrets')
  .get((req, res)=>{
      if (req.isAuthenticated()){
          res.render('secrets.ejs', { secrets: [
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce rhoncus enim at fringilla consectetur.",
            "Morbi sodales sit amet lacus sit amet vestibulum. Integer vel dui orci.",
            "Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
          ] })
      }
      else {
          res.redirect('/')
      }
  })
  .post((req, res)=>{
    
    const secret = req.body.text
    const new_secret = new Secret({ secret: secret })
    res.redirect('/secret')
  })

app.get('/load', (req, res)=>{

});

app.listen(port, () => {
    console.log(`Server running on port ${port}.`);
})