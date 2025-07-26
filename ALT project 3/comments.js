document.addEventListener('DOMContentLoaded', function() {
    const username = localStorage.getItem('username');
    const email = localStorage.getItem('email');

    if (username && email) {
        document.getElementById('name').value = username;
        loadComments(); // Load comments when the page loads
    } else {
        alert("You are not logged in!");
        window.location.href = "loginPage.html"; // Redirect to login page
    }
});

function post() {
    const username = document.getElementById('name').value;
    const title = document.getElementById('title').value;
    const comment = document.getElementById('comment').value;

    if (comment.trim() === "") {
        alert("Comment cannot be empty!");
        return;
    }

    const myDB = firebase.database().ref('comments');
    const newComment = myDB.push(); // Create a new comment entry

    newComment.set({
        username: username,
        comment: comment,
        title: title,
        timestamp: new Date().toISOString()
    });

    document.getElementById('comment').value = ""; // Clear the comment input field
    document.getElementById('title').value = ""; // Clear the title input field
    alert("Comment posted successfully!");
}

function loadComments() {
    const myDB = firebase.database().ref('comments');

    myDB.on('value', function(snapshot) {
        const commentsList = document.getElementById('comments-list');
        commentsList.innerHTML = ""; // Clear the list before appending new comments

        snapshot.forEach(function(childSnapshot) {
            const data = childSnapshot.val();
            const commentElement = document.createElement('div');
            commentElement.classList.add('comment');

            commentElement.innerHTML = `
                <p><strong>${data.username}</strong>:</p>
                <h5>${new Date(data.timestamp).toLocaleString()}</h5>
                <h4>${data.title}</h4>
                <p>${data.comment}</p>
            `;

            commentsList.appendChild(commentElement);
        });
    });
}

function logout() {
    // Clear localStorage or sessionStorage
    localStorage.clear();

    // Redirect to the login page
    window.location.href = "loginPage.html";
}