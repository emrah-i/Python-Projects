
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