
document.addEventListener('DOMContentLoaded', () => {

    if (document.querySelector('#update_button')) {
        document.querySelector('#update_button').addEventListener('click', (event) => {
            id = event.target.dataset.id;
            event.target.style.display = 'none';
            form = document.querySelector('#update_form');
            form.style.display = 'block'
        })
    }
})