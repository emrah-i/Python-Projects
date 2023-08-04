
const a_ch = document.querySelector('#about_chevron');
const p_ch = document.querySelector('#projects_chevron');
const resume_button = document.querySelector('button.resume')
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
        document.querySelector('#project1').scrollIntoView({ block: 'center' });
    })
}

if (resume_button) {
    resume_button.addEventListener('click', ()=>{
        window.open('https://www.docdroid.net/WyjIuyO/fake-resume-pdf', 'Resume')
    })
}

eye.addEventListener('click', (event)=> {
    let color = ''

    if (event.target.id === 'eye') {
        color = event.target.dataset.color
    }
    else {
        color = event.target.closest('#eye').dataset.color
        console.log(color)
    }

    if (color === 'light') {
        window.localStorage.setItem('color', 'dark');
        document.documentElement.style.setProperty('--main-color', darkColor);
        eye.dataset.color = 'dark';
    }
    else {
        window.localStorage.setItem('color', 'light');
        document.documentElement.style.setProperty('--main-color', lightColor);
        eye.dataset.color = 'light';
    }
})