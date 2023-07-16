
document.addEventListener('DOMContentLoaded', () => {

    if (document.querySelector('#update_button')) {
        document.querySelectorAll('#update_button').forEach((element) => {
            element.addEventListener('click', (event) => {
                id = event.target.dataset.id;
                console.log(id)
                document.querySelector('#delete_button[data-id="' + id + '"]').style.display = 'none';
                event.target.style.display = 'none';
                form = document.querySelector('#update_form' + id);
                form.style.display = 'block'
            })
        })
    }

    if (document.querySelector('#delete_button')) {
        document.querySelectorAll('#delete_button').forEach((element) => {
            element.addEventListener('click', (event) => {
                if (confirm("Are you sure you would like to delete this movie?")) {

                }
            })
        })
    }
})