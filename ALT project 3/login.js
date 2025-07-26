function Db() {
    var email = document.getElementById('email').value;
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    console.log("Email:", email);
    console.log("Username:", username);
    console.log("Password:", password);

    var myDB = firebase.database().ref('credentials');

    // Query the database to check if the email or username already exists
    myDB.orderByChild('email').equalTo(email).once('value', function(emailSnapshot) {
        if (emailSnapshot.exists()) {
            // Email already exists
            console.log("Email already exists in the database.");
            alert("This email is already registered. Please use a different email or log in.");
        } else {
            // Check if the username already exists
            myDB.orderByChild('username').equalTo(username).once('value', function(usernameSnapshot) {
                if (usernameSnapshot.exists()) {
                    // Username already exists
                    console.log("Username already exists in the database.");
                    alert("This username is already taken. Please choose a different username.");
                } else {
                    // Both email and username do not exist, proceed with sign-up
                    var addRecord = myDB.push();
                    var record1 = {
                        "email": email,
                        "username": username,
                        "password": password
                    };

                    addRecord.set(record1);
                    alert("Sign-up successful! Your account has been created.");
                }
            });
        }
    });
}

function checkCredentials() {
    var email = document.getElementById('Lemail').value;
    var username = document.getElementById('Lusername').value;
    var password = document.getElementById('Lpassword').value;

    console.log("Email:", email);
    console.log("Username:", username);
    console.log("Password:", password);

    var myDB = firebase.database().ref('credentials');

    // Query the database to check if the email exists
    myDB.orderByChild('email').equalTo(email).once('value', function(snapshot) {
        if (snapshot.exists()) {
            console.log("Email exists in the database.");
            let loginSuccessful = false; // Flag to track login success

            snapshot.forEach(function(childSnapshot) {
                var data = childSnapshot.val();
                console.log("Database record:", data);

                if (data.username === username && data.password === password) {
                    alert("Login successful! Username and password match.");
                    localStorage.setItem('username', username); // Store username
                    localStorage.setItem('email', email);       // Store email
                    loginSuccessful = true; // Set flag to true
                    window.location.href = "comments.html";     // Redirect to comments page
                    return; // Exit the loop
                }
            });

            if (!loginSuccessful) {
                alert("Email exists, but username or password does not match.");
            }
        } else {
            console.log("Email does not exist in the database.");
            alert("Email does not exist. Please sign up first.");
        }
    });
}

function logout() {
    // Clear localStorage or sessionStorage
    localStorage.clear();

    // Redirect to the login page
    window.location.href = "loginPage.html";
}