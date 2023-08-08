
if (document.querySelector('.login-btn')) {
    document.querySelector('.login-btn').addEventListener('click', ()=>{
        window.location.pathname = '/login'
    })
}

if (document.querySelector('.register-btn')) {
    document.querySelector('.register-btn').addEventListener('click', ()=>{
        window.location.pathname = '/register'
    })
}

if (document.querySelector('.google_btn')) {
    (document.querySelector('.google_btn')).addEventListener('click', ()=>{
        window.location.pathname = '/auth/google'
    })
}

if (document.querySelector('.fb_btn')) {
    (document.querySelector('.fb_btn')).addEventListener('click', ()=>{
        window.location.pathname = '/auth/facebook'
    })
}