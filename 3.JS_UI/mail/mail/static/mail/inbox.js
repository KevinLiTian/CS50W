document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  document.querySelector('#compose-form').onsubmit = () => {
    fetch('/emails', {
      // Send POST request to record the email
      method: 'POST',
      body: JSON.stringify({
          recipients: document.querySelector('#compose-recipients').value,
          subject: document.querySelector('#compose-subject').value,
          body: document.querySelector('#compose-body').value
      })
    })
    .then(response => response.json())
    .then(() => {load_mailbox('sent');})
    .catch(error => {
        // Catch any errors and log them to the console
        console.log('Error:', error);
    });

    return false;
  };
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    emails.forEach(email => {
      // Data
      const id = email['id'];
      const sender = email['sender'];
      const subject = email['subject'];
      const timestamp = email['timestamp'];
      const read = email['read'];

      // Create HTML Elements
      const emailDiv = document.createElement('div');
      emailDiv.dataset.emailid = id;
      emailDiv.classList.add('border', 'border-secondary', 'row', 'w-100', 'm-auto', 'align-items-center', 'my-custom-row');
      emailDiv.style.backgroundColor = read ? 'lightgrey' : 'white';

      if (mailbox === 'sent') {
        const recipients = email['recipients'];
        const recipient_str = (recipients.length == 1) ? `${recipients[0]}` : `${recipients[0]}...`; 
        const recipientsDiv = document.createElement('div');
        recipientsDiv.classList.add('col-4');
        recipientsDiv.innerHTML = `To: ${recipient_str}`;
        emailDiv.append(recipientsDiv);
      }else{
        const senderDiv = document.createElement('div');
        senderDiv.classList.add('col-4');
        senderDiv.innerHTML = `From: ${sender}`;
        emailDiv.append(senderDiv);
      }

      const subjectDiv = document.createElement('div');
      subjectDiv.classList.add('col-4');
      subjectDiv.innerHTML = subject;
      emailDiv.append(subjectDiv);

      const timestampDiv = document.createElement('div');
      timestampDiv.classList.add('col-4', 'text-end');
      timestampDiv.innerHTML = timestamp;
      emailDiv.append(timestampDiv);

      // Add to DOM
      document.querySelector('#emails-view').append(emailDiv);
    });
  });
}

/* JSON
[
    {
        "id": 100,
        "sender": "foo@example.com",
        "recipients": ["bar@example.com"],
        "subject": "Hello!",
        "body": "Hello, world!",
        "timestamp": "Jan 2 2020, 12:00 AM",
        "read": false,
        "archived": false
    },
    {
        "id": 95,
        "sender": "baz@example.com",
        "recipients": ["bar@example.com"],
        "subject": "Meeting Tomorrow",
        "body": "What time are we meeting?",
        "timestamp": "Jan 1 2020, 12:00 AM",
        "read": true,
        "archived": false
    }
]
*/
