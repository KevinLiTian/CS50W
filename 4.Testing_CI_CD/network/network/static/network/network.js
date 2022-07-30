document.addEventListener("DOMContentLoaded", () => {

    // Edit Button Click
    document.querySelectorAll('.edit-btn').forEach(edit_btn => edit(edit_btn));

    // Like Button Click
    document.querySelectorAll('.like-btn').forEach(like_btn => like(like_btn));
});


/* Each Like Button */
function like(like_btn) {
    like_btn.addEventListener("click", () => {

        // Get Post ID
        const id = like_btn.dataset.id;

        // Get Empty Heart and fill heart
        const empty_heart = like_btn.querySelector('.bi-heart');
        const fill_heart = like_btn.querySelector('.bi-heart-fill');

        // If not liked yet
        if (fill_heart.classList.contains('d-none')) {

            fetch(`/like/${id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    like: true
                })
            }).then(response => response.json()).catch(err => console.error(err));

            empty_heart.classList.add('d-none');
            fill_heart.classList.remove('d-none');
            const like_num = like_btn.querySelector('span');
            like_num.innerHTML = parseInt(like_num.innerHTML) + 1;
            like_btn.blur();

            // Already Liked
        } else {

            fetch(`/like/${id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    like: false
                })
            }).then(response => response.json()).catch(err => console.error(err));

            empty_heart.classList.remove('d-none');
            fill_heart.classList.add('d-none');
            const like_num = like_btn.querySelector('span');
            like_num.innerHTML = parseInt(like_num.innerHTML) - 1;
            like_btn.blur();
        }
    });
}


/* Each Edit Button */
function edit(edit_btn) {
    edit_btn.addEventListener("click", () => {

        // Get Outer Div with Class "w-75 m-auto"
        const outerDiv = edit_btn.parentElement.parentElement.parentElement;

        // Get textarea
        const textarea = outerDiv.querySelector('.original-content');

        // Not Editing
        if (!textarea.classList.contains('d-none')) {

            // Retrieve original text
            const original_text = textarea.innerHTML;

            // Hide textarea
            textarea.classList.add('d-none');

            // Display input textarea and pre-fill value
            const input_textarea = outerDiv.querySelector('.new-content');
            input_textarea.innerHTML = original_text;
            input_textarea.classList.remove('d-none');
            input_textarea.focus();

            // Replace Button Value
            edit_btn.innerHTML = 'Done';

            // Done Editing
        } else {

            // Retrieve new content
            const input_textarea = outerDiv.querySelector('.new-content');
            const new_content = input_textarea.value;

            // PUT Request to edit API
            const post_id = edit_btn.dataset.id;
            fetch(`/edit/${post_id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    content: new_content
                })
            }).then(response => response.json()).catch(error => console.log(error));

            // Hide input_textarea
            input_textarea.classList.add('d-none')

            // Display textarea and pre-fill content
            textarea.innerHTML = new_content;
            textarea.classList.remove('d-none');

            // Replace Button Value
            edit_btn.innerHTML = 'Edit';
        }
    });
}
