## Specification

Using JavaScript, HTML, and CSS, complete the implementation of your single-page-app email client inside of inbox.js (and not additional or other files; for grading purposes, we’re only going to be considering inbox.js!). You must fulfill the following requirements:

- Send Mail: When a user submits the email composition form, add JavaScript code to actually send the email
  - You’ll likely want to make a POST request to /emails, passing in values for recipients, subject, and body
  - Once the email has been sent, load the user’s sent mailbox
- Mailbox: When a user visits their Inbox, Sent mailbox, or Archive, load the appropriate mailbox
  - You’ll likely want to make a GET request to /emails/<mailbox> to request the emails for a particular mailbox
  - When a mailbox is visited, the application should first query the API for the latest emails in that mailbox
  - When a mailbox is visited, the name of the mailbox should appear at the top of the page (this part is done for you)
  - Each email should then be rendered in its own box (e.g. as a <div> with a border) that displays who the email is from, what the subject line is, and the timestamp of the email
  - If the email is unread, it should appear with a white background. If the email has been read, it should appear with a gray background
- View Email: When a user clicks on an email, the user should be taken to a view where they see the content of that email
  - You’ll likely want to make a GET request to /emails/<email_id> to request the email
  - Your application should show the email’s sender, recipients, subject, timestamp, and body
  - You’ll likely want to add an additional div to inbox.html (in addition to emails-view and compose-view) for displaying the email. Be sure to update your code to hide and show the right views when navigation options are clicked
  - See the hint in the Hints section about how to add an event listener to an HTML element that you’ve added to the DOM.
    Once the email has been clicked on, you should mark the email as read. Recall that you can send a PUT request to /emails/<email_id> to update whether an email is read or not
- Archive and Unarchive: Allow users to archive and unarchive emails that they have received
  - When viewing an Inbox email, the user should be presented with a button that lets them archive the email
  - When viewing an Archive email, the user should be presented with a button that lets them unarchive the email. This requirement does not apply to emails in the Sent mailbox
  - Recall that you can send a PUT request to /emails/<email_id> to mark an email as archived or unarchived
  - Once an email has been archived or unarchived, load the user’s inbox
- Reply: Allow users to reply to an email
  - When viewing an email, the user should be presented with a “Reply” button that lets them reply to the email
  - When the user clicks the “Reply” button, they should be taken to the email composition form
  - Pre-fill the composition form with the recipient field set to whoever sent the original email
  - Pre-fill the subject line. If the original email had a subject line of foo, the new subject line should be Re: foo. (If the subject line already begins with Re: , no need to add it again.)
  - Pre-fill the body of the email with a line like "On Jan 1 2020, 12:00 AM foo@example.com wrote:" followed by the original text of the email.

## API Documentation

You’ll get mail, send mail, and update emails by using this application’s API. We’ve written the entire API for you (and documented it below), so that you can use it in your JavaScript code. (In fact, note that we have written all of the Python code for you for this project. You should be able to complete this project by just writing HTML and JavaScript).

This application supports the following API routes:

#### `GET /emails/<str:mailbox>`

Sending a `GET` request to `/emails/<mailbox>` where `<mailbox>` is either `inbox`, `sent`, or `archive` will return back to you (in JSON form) a list of all emails in that mailbox, in reverse chronological order. For example, if you send a `GET` request to `/emails/inbox`, you might get a JSON response like the below (representing two emails):

```JSON
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
```

How would you send a `GET` request? You can do it via AJAX, particularly the `fetch` function:

```JS
fetch('/emails/inbox')
.then(response => response.json())
.then(emails => {
    // Print emails
    console.log(emails);

    // ... do something else with emails ...
});
```

#### `GET /emails/<int:email_id>`

Sending a `GET` request to `/emails/<int:email_id>` will return back to you all the information regardig one email with Django model id of `email_id`. The JavaScript code to fetch will be:

```JS
fetch('/emails/100')
.then(response => response.json())
.then(email => {
    // Print email
    console.log(email);

    // ... do something else with email ...
});
```

The JSON response will look like:

```JSON
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
```

#### `POST /emails`

Other than `GET` email information, you can also send an email via `POST` request. The JavaScript code to send will be:

```JS
fetch('/emails', {
  method: 'POST',
  body: JSON.stringify({
      recipients: 'baz@example.com',
      subject: 'Meeting time',
      body: 'How about we meet tomorrow at 3pm?'
  })
})
.then(response => response.json())
.then(result => {
    // Print result
    console.log(result);
});
```

#### `PUT /emails/<int:email_id>`

We introduce a new request which is to modify existing data. In order to modify the `read` or `archived` boolean in email objects, we use `PUT` request with a body:

```JS
fetch('/emails/100', {
  method: 'PUT',
  body: JSON.stringify({
      archived: true
  })
})
```

## Hints

- To create an HTML element and add an event handler to it, you can use JavaScript code like the below:

```JS
const element = document.createElement('div');
element.innerHTML = 'This is the content of the div.';
element.addEventListener('click', function() {
    console.log('This element has been clicked!')
});
document.querySelector('#container').append(element);
```

This code creates a new `div` element, sets its `innerHTML`, adds an event handler to run a particular function when that div is clicked on, and then adds it to an HTML element whose `id` is `container` (this code assumes that there is a HTML element whose `id` is `container`: you’ll likely want to change the argument to `querySelector` to be whichever element you’d like to add an element to)

- You may find it helpful to edit `mail/static/mail/styles.css` to add any CSS you need for the application
- Recall that if you have a JavaScript array, you can loop over each element of that array using [`forEach`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
- Recall that normally, for `POST` and `PUT` requests, Django requires a CSRF token to guard against potential cross-site request forgery attacks. For this project, we’ve intentionally made the API routes CSRF-exempt, so you won’t need a token. In a real-world project, though, always best to guard against such potential vulnerabilities!
