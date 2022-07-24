document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  const navLinks = document.querySelectorAll('.nav-item');
  const menuToggle = document.getElementById('navmenu');
  const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle:false});
  navLinks.forEach((l) => {
    l.addEventListener('click', () => { 
      if (window.innerWidth < 992) {
        bsCollapse.toggle() }
      }
    )  
  });

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#email-view').style.display = 'none';
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
  document.querySelector('#email-view').style.display = 'none';
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
      emailDiv.addEventListener('click', () => view_email(id, mailbox==="sent"));
      document.querySelector('#emails-view').append(emailDiv);
    });
  }).catch(error => console.log(error));
}

function view_email(email_id, sent) {
  // Show the email and hide other views
  document.querySelector('#email-view').style.display = 'block';
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  
  // Clear Out
  document.querySelector('#email-view').innerHTML = '';

  // Mark as read
  fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: true
    })
  }).then(() => {

    // fetch Info
    fetch(`/emails/${email_id}`)
    .then(response => response.json())
    .then(email => {

      // Data
      const sender = email['sender'];
      const recipients = email['recipients'];
      const subject = email['subject'];
      const timestamp = email['timestamp'];
      const body = email['body'];
      const read = email['read'];
      const archived = email['archived'];

      // Create HTML Elements
      const emailDiv= document.createElement('div');
      emailDiv.classList.add('mb-5');

      const senderP = document.createElement('p');
      senderP.innerHTML = `From: ${sender}`;

      const recipientsP = document.createElement('p');
      let recipients_str = 'To: ';
      recipients.forEach(recip => {
        recipients_str = recipients_str + recip + '; '; 
      })
      recipientsP.innerHTML = recipients_str;

      const subjectP = document.createElement('p');
      subjectP.innerHTML = `Subject: ${subject}`;

      const timestampP = document.createElement('p');
      timestampP.innerHTML = timestamp;

      const bodyP = document.createElement('p');
      bodyP.innerHTML = body;

      // All buttons
      const buttonsDiv = document.createElement('div');
      buttonsDiv.classList.add('d-flex');

      // Reply
      const reply_btn = document.createElement('button');
      reply_btn.innerHTML = 'Reply';
      reply_btn.classList.add('btn', 'btn-primary');
      reply_btn.addEventListener('click', () => reply_email(email_id));

      // Other buttons
      const other_btn = document.createElement('div');
      other_btn.classList.add('ms-auto');

      // Mark as read/Unread
      const read_btn = document.createElement('button');
      read_btn.addEventListener('click', () => setRead(read, email_id));
      read_btn.innerHTML = 'Mark as Unread';
      read_btn.classList.add('btn', 'btn-secondary', 'mx-2');
      other_btn.append(read_btn);

      // Archive/Unarchive
      if (!sent) {
        const archive_btn = document.createElement('button');
        archive_btn.addEventListener('click', () => setArchived(archived, email_id));

        if (archived) {
          archive_btn.innerHTML = 'Unarchive';
          archive_btn.classList.add('btn', 'btn-danger');
        }else{
          archive_btn.innerHTML = 'Archive';
          archive_btn.classList.add('btn', 'btn-success');
        }

        other_btn.append(archive_btn);
      }

      // Append to div
      buttonsDiv.append(reply_btn, other_btn);

      // Add to DOM
      emailDiv.append(senderP, recipientsP, subjectP, timestampP, 
        document.createElement('hr'), bodyP);
      document.querySelector('#email-view').append(emailDiv, buttonsDiv);

    }).catch(error => console.log(error));
  }).catch(error => console.log(error));
}


function setRead(read, email_id) {
  fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: read ? false : true
    })
  })
  .then(() => load_mailbox('inbox'))
  .catch(error => console.log(error));
}


function setArchived(archived, email_id) {
  fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({
      archived: archived ? false : true
    })
  })
  .then(() => load_mailbox('inbox'))
  .catch(error => console.log(error));
}


function reply_email(email_id) {

  // Display only compose view
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  fetch(`/emails/${email_id}`)
  .then(response => response.json())
  .then(email => {

    // Data
    const sender = email['sender'];
    let subject = email['subject'];
    let body = email['body'];
    const timestamp = email['timestamp'];

    // Process Data
    if (!subject.startsWith('Re: ')) {
      subject = 'Re: ' + subject;
    }

    body = `On ${timestamp} ${sender} wrote:"${body}"`;

    // Pre-fill
    document.querySelector('#compose-recipients').value = sender;
    document.querySelector('#compose-subject').value = subject;
    document.querySelector('#compose-body').value = body;
  }).catch()
}

/* JSON
Emails:
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

Email:
{
        "id": 100,
        "sender": "foo@example.com",
        "recipients": ["bar@example.com"],
        "subject": "Hello!",
        "body": "Hello, world!",
        "timestamp": "Jan 2 2020, 12:00 AM",
        "read": false,
        "archived": false
}
*/
