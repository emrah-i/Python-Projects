
const a_ch = document.querySelector('#about_chevron');
const p_ch = document.querySelector('#projects_chevron');
const resume_button = document.querySelector('button.resume');
const chars = document.querySelector('#chars');
const email = document.querySelector('#personal_email');
const phone = document.querySelector('#personal_phone');
const about_element = document.querySelector('#about_section');
const quote = document.querySelector('.quote')
const lightColor = '#FBF7F2';
const darkColor = '#212F3C';
const eye = document.querySelector('#eye')

if (window.localStorage.getItem('color')) {
    let color = window.localStorage.getItem('color')

    if (color === 'light') {
        document.documentElement.style.setProperty('--main-color', lightColor);
    }
    else {
        document.documentElement.style.setProperty('--main-color', darkColor);
    }
}

if (a_ch) {
    a_ch.addEventListener('click', ()=>{
        quote.scrollIntoView({block: "center", behavior: 'smooth'})
    })
}

if (p_ch) {
    p_ch.addEventListener('click', ()=>{
        document.querySelector('#project1').scrollIntoView({block: 'center'});
    })
}

if (resume_button) {
    resume_button.addEventListener('click', ()=>{
        window.open('https://www.docdroid.net/WyjIuyO/fake-resume-pdf', 'Resume')
    })
}

if (chars) {
    document.querySelector('#contact_section textarea').addEventListener('input', (event)=>{
        let char_count = chars.querySelector('#char_count');
        let current = event.target.value.length;

        char_count.innerHTML = current;
    })
}

if (email) {
    const email_info = document.querySelector('#personal_email .tooltiptext')
    document.querySelector('.email-btn').addEventListener('click', ()=> {
        email.scrollIntoView({block: 'center'});
    });

    document.querySelector('#personal_email > span').addEventListener('click', ()=> {
        navigator.clipboard.writeText('ibraem1026@gmail.com');
        email_info.innerHTML = '✔'
        setTimeout(()=>{
            email_info.innerHTML = 'Click to copy!'
        }, 1000)
    });
};

if (phone) {
    const phone_info =  document.querySelector('#personal_phone .tooltiptext')
    document.querySelector('.phone-btn').addEventListener('click', ()=> {
        phone.scrollIntoView({block: 'center'});
    });

    document.querySelector('#personal_phone > span').addEventListener('click', ()=> {
        navigator.clipboard.writeText('240-520-8934');
        phone_info.innerHTML = '✔'
        setTimeout(()=>{
            phone_info.innerHTML = 'Click to copy!'
        }, 1000)
    });
};

eye.addEventListener('click', (event)=> {
    let color = '';

    if (event.target.id === 'eye') {
        color = event.target.dataset.color
    }
    else {
        color = event.target.closest('#eye').dataset.color
        console.log(color)
    };

    if (color === 'light') {
        window.localStorage.setItem('color', 'dark');
        document.documentElement.style.setProperty('--main-color', darkColor);
        eye.dataset.color = 'dark';
    }
    else {
        window.localStorage.setItem('color', 'light');
        document.documentElement.style.setProperty('--main-color', lightColor);
        eye.dataset.color = 'light';
    };
})