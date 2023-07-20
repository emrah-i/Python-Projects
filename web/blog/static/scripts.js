
all_counter = 0
cat_counter = 0

document.addEventListener('DOMContentLoaded', ()=>{
    CKEDITOR.replace('editor');
    CKEDITOR.replace('editor2');

    if (document.querySelector('#all-posts-load-button')) {
      document.querySelector('#all-posts-load-button').addEventListener('click', ()=>{
        main_div = document.querySelector('.album_rows')
        all_counter += 6
        fetch('/load?start=' + all_counter)
          .then(response => response.json())
          .then(data => {

            if (data.length === 0) {
              alert('No more blog posts.')
              exit()
            }

            for (i=0;i<data.length;i++) {
              id = data[i]['id']
              title = data[i]['title']
              subtitle = data[i]['subtitle']
              author = data[i]['author']
              date = data[i]['date']
              body = data[i]['body']
              img_src = data[i]['img_src']

              new_element = document.createElement('div')
              new_element.className = "col" 
              new_element.addEventListener('click', ()=> {
                window.location.pathname = '/post/' + id
              })

              new_element.innerHTML = `
              <div class="card all_posts_container">
                <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false">
                    <image href="${img_src}" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" />
                </svg>
    
                <div class="card-body">
                    <p class="card-text"><b>${title}</b></p>
                    <small class="text-muted">${date}</small>
                </div>
              </div>
              `

              main_div.append(new_element)
            }
          })
          .catch(error => {
            console.error('Error:', error);
          });
      })
    }

    if (document.querySelector('#category-load-button')) {
      document.querySelector('#category-load-button').addEventListener('click', (event)=>{
        category = event.target.dataset.category
        main_div = document.querySelector('.album_rows')
        cat_counter += 6
        fetch(`/category_load/${category}?start=` + cat_counter)
          .then(response => response.json())
          .then(data => {

            if (data.length === 0) {
              alert('No more blog posts in this category.')
              return
            }

            for (i=0;i<data.length;i++) {
              id = data[i]['id']
              title = data[i]['title']
              subtitle = data[i]['subtitle']
              author = data[i]['author']
              date = data[i]['date']
              body = data[i]['body']
              img_src = data[i]['img_src']

              new_element = document.createElement('div')
              new_element.className = "col" 
              new_element.addEventListener('click', ()=> {
                window.location.pathname = '/post/' + id
              })

              new_element.innerHTML = `
              <div class="card all_posts_container">
                <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false">
                    <image href="${img_src}" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" />
                </svg>
    
                <div class="card-body">
                    <p class="card-text"><b>${title}</b></p>
                    <small class="text-muted">${date}</small>
                </div>
              </div>
              `

              main_div.append(new_element)
            }
          })
          .catch(error => {
            console.error('Error:', error);
          });
      })
    }

    if (document.querySelector('#make_comment')) {
      document.querySelector('#make_comment').addEventListener('click', (event) => {
        event.target.style.display = 'none'
        make_comment = document.querySelector('#ind-post-comments')
        make_comment.className = "d-flex justify-content-center"
        make_comment.style.display = 'block'
      })
    }
    
    if (document.querySelector('#edit_post')) {
      document.querySelector('#edit_post').addEventListener('click', (event)=>{
        postid = event.target.dataset.id
        window.location.pathname = '/update/' + postid
      })
    }

    if (document.querySelector('#update_post_button')) {
      document.querySelector('#update_post_button').addEventListener('click', (event)=>{
        postid = event.target.dataset.id
        update_post(postid)
      })
    }

    if (document.querySelector('#delete_post')) {
      document.querySelector('#delete_post').addEventListener('click', (event)=>{
        if (confirm("Are you sure you want to delete this post?")) {
          postid = event.target.dataset.id
          delete_post(postid)
        }
      })
    }

    if (document.querySelector('#edit_profile_button')) {
      document.querySelector('#edit_profile_button').addEventListener('click', (event) => {
        event.target.style.display = 'none'
        document.querySelector('#change_pw_button').style.display = 'none'
        document.querySelector('#confirm_edit_button').style.display = 'block'
        
        form = document.querySelector('#edit_profile_form')
        form.querySelector('input[name="f_name"]').disabled = false,
        form.querySelector('input[name="l_name"]').disabled = false,
        form.querySelector('input[name="email"]').disabled = false,
        form.querySelector('input[name="username"]').disabled = false
      })
    }

    if (document.querySelector('#change_pw_button')) {
      document.querySelector('#change_pw_button').addEventListener('click', () => {
        window.location.pathname = '/password'
      })
    }

    if (document.querySelector('#confirm_pw_button')) {
      document.querySelector('#confirm_pw_button').addEventListener('click', (event)=>{
        event.preventDefault()
        update_pw()
      })
    }
  });


  async function getCSRF() {
    const response = await fetch("/csrf_token", {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })

    const data = await response.json();
    const csrfToken = data.csrf_token;
    return csrfToken
  }

  async function update_post(postid) {
    csrf = await getCSRF()
    form = document.querySelector('#update_post_form')

    data = {
      'title': form.querySelector('input[name="title"]').value,
      'subtitle': form.querySelector('input[name="subtitle"]').value,
      'author': form.querySelector('input[name="author"]').value,
      'img_src': form.querySelector('input[name="img"]').value,
      'category': form.querySelector('select[name="category"]').value,
      'body': form.querySelector('textarea[name="body"]').value
    }

    fetch(`/update/${postid}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': csrf
        },
        body: JSON.stringify(data)
      })
      .then(response => response.json())
      .then(data => {
        window.location.pathname = `/post/${postid}`
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }

  async function delete_post(postid) {
    csrf = await getCSRF()

    fetch(`/delete/${postid}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': csrf
        }
      })
      .then(response => response.json())
      .then(data => {
        window.location.pathname = '/all'
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }

  async function update_pw() {
    csrf = await getCSRF()
    form = document.querySelector('#change_pw_form')

    data = {
      'password': form.querySelector('input[name="password"]').value,
      'confirm': form.querySelector('input[name="confirm"]').value,
    }

    fetch(`/password`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': csrf
        },
        body: JSON.stringify(data)
      })
      .then(response => response.json())
      .then(data => {
        if (data.success){
          window.location.pathname = '/'
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }