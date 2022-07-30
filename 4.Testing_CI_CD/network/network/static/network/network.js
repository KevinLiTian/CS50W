document.addEventListener("DOMContentLoaded", () => {

    // Edit Button Click
    document.querySelectorAll(".edit-btn").forEach(edit_btn => edit(edit_btn));
});

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

            // Hide input_textarea
            input_textarea.classList.add('d-none')

            // Display textarea and pre-fill content
            textarea.innerHTML = new_content;
            textarea.classList.remove('d-none');

            // Replace Button Value
            edit_btn.innerHTML = 'Edit';

            // PUT Request to edit API
            const post_id = edit_btn.dataset.id;
            fetch(`/edit/${post_id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    content: new_content
                })
            }).then(response => response.json()).catch(error => console.log(error));
        }
    });
}
