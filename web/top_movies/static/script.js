
document.addEventListener('DOMContentLoaded', () => {

    if (document.querySelector('#update_button')) {
        document.querySelectorAll('#update_button').forEach((element) => {
            element.addEventListener('click', (event) => {
                id = event.target.dataset.id;
                document.querySelector('#back_items' + id).style.display = 'none';
                form = document.querySelector('#update_form' + id);
                form.style.display = 'block';
                form.querySelector('input').value = event.target.dataset.rating;
                form.querySelector('textarea').value = event.target.dataset.comments;

                document.querySelectorAll('#update_cancel_button').forEach((element) => {
                    element.addEventListener('click', () => { 
                        if (confirm('Are you sure you would like to cancel this edit?')) {
                            location.reload()
                        }
                    })
                })

                document.querySelectorAll('#update_submit_button').forEach((element) => {
                    element.addEventListener('click', (event) => { 
                        event.target.closest('form').submit()
                    })
                })
            })
        })
    }

    if (document.querySelector('#delete_button')) {
        document.querySelectorAll('#delete_button').forEach((element) => {
            element.addEventListener('click', (event) => {
                if (confirm("Are you sure you would like to delete this movie?")) {
                    event.target.closest('form').submit()
                }
            })
        })
    }
})