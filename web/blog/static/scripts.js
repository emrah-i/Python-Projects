
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

    if (document.querySelector('#edit_post')) {}

    if (document.querySelector('#delete_post')) {
      document.querySelector('#delete_post').addEventListener('click', (event)=>{
        if (confirm("Are you sure you want to delete this post?")) {
          id = event.target.dataset.id
          fetch(`/delete/${id}`, {
            method: 'DELETE',
            headers: {
              'Content-Type': 'application/json'
              }
            })
            .then(response => response.json())
            .then(data => {
              console.log(data);
              window.location.pathname = '/'
            })
            .catch(error => {
              console.error('Error:', error);
            });
        }
      })
    }
    
  });