
const a_ch = document.querySelector('#about_chevron')
const p_ch = document.querySelector('#projects_chevron')
const about_element = document.querySelector('#about_section')


if (a_ch) {
    a_ch.addEventListener('click', ()=>{
        about_element.scrollIntoView()
    })
}

if (p_ch) {
    p_ch.addEventListener('click', ()=>{
        about_element.scrollIntoView()
    })
}